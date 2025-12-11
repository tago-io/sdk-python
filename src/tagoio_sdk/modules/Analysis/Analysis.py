import asyncio
import inspect
import json
import os
import sys

from typing import Any
from typing import List
from typing import Optional

from tagoio_sdk.common.JSON_Parse_Safe import JSONParseSafe
from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.infrastructure.api_sse import openSSEListening
from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisConstructorParams
from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisEnvironment
from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisFunction
from tagoio_sdk.modules.Services.Console import ConsoleService
from tagoio_sdk.regions import getConnectionURI as getRegionObj
from tagoio_sdk.regions import setRuntimeRegion


T_ANALYSIS_CONTEXT = os.environ.get("T_ANALYSIS_CONTEXT") or None


class Analysis(TagoIOModule):
    """
    Analysis execution context for TagoIO

    This class provides the runtime environment for executing analysis scripts in TagoIO.
    It manages environment variables, console outputs, and analysis execution lifecycle.
    Analyses can run locally for development or in the TagoIO cloud platform.

    Example: Basic analysis usage
        ```python
        from tagoio_sdk import Analysis

        def my_analysis(context, scope):
            # Get analysis environment variables
            environment = context.environment

            # Use console service for logging
            context.log("Analysis started")

            # Your analysis logic here
            print("Processing data...")

        Analysis.use(analysis=my_analysis, params={"token": "your-analysis-token"})
        ```

    Example: Analysis with EU region
        ```python
        from tagoio_sdk import Analysis

        def my_analysis(context, scope):
            context.log("Running in EU region")
            print("Environment:", context.environment)

        # Using Analysis.use() method
        Analysis.use(analysis=my_analysis, params={"token": "your-analysis-token", "region": "eu-w1"})
        ```

    Example: Analysis with Tago Deploy
        ```python
        from tagoio_sdk import Analysis

        def my_analysis(context, scope):
            context.log("Running in TDeploy")
            print("Scope:", scope)

        # Tago Deploy requires a dictionary with tdeploy ID
        Analysis.use(
            analysis=my_analysis,
            params={
                "token": "your-analysis-token",
                "region": {"tdeploy": "your-tdeploy-id"}
            }
        )
        ```

    Example: Environment variables
        ```python
        def my_analysis(context, scope):
            env = context.environment
            api_key = next((e["value"] for e in env if e["key"] == "API_KEY"), None)

        Analysis.use(analysis=my_analysis, params={"token": "your-analysis-token"})
        ```
    """

    def __init__(self, params: Optional[AnalysisConstructorParams] = None):
        if params is None:
            params = {"token": "unknown"}

        super().__init__(params)
        self.params = params
        self._running = True

    def init(self, analysis: AnalysisFunction):
        self.analysis = analysis

        if not os.environ.get("T_ANALYSIS_TOKEN") and self.params.get("token"):
            os.environ["T_ANALYSIS_TOKEN"] = self.params.get("token")

        # Configure runtime region
        runtimeRegion = getRegionObj(self.params["region"]) if self.params.get("region") else None
        if runtimeRegion:
            setRuntimeRegion(runtimeRegion)

        if T_ANALYSIS_CONTEXT is None:
            self._localRuntime()
        else:
            self._runOnTagoIO()

    def _runOnTagoIO(self) -> None:
        if not self.analysis or not callable(self.analysis):
            raise TypeError("Invalid analysis function")

        def context():
            pass

        context.log = print
        context.token = os.environ.get("T_ANALYSIS_TOKEN", "")
        context.analysis_id = os.environ.get("T_ANALYSIS_ID", "")
        context.environment = JSONParseSafe(os.environ.get("T_ANALYSIS_ENV", "[]"), [])

        data = JSONParseSafe(os.environ.get("T_ANALYSIS_DATA", "[]"), [])

        self.analysis(context, data)

    def _stringifyMsg(self, msg: Any) -> str:
        if isinstance(msg, dict) and not isinstance(msg, list):
            return json.dumps(msg)
        return str(msg)

    def _runLocal(
        self,
        environment: List[AnalysisEnvironment],
        data: List[Any],
        analysisID: str,
        token: str,
    ) -> None:
        if not self.analysis or not callable(self.analysis):
            raise TypeError("Invalid analysis function")

        tagoConsole = ConsoleService({"token": token, "region": self.params.get("region")})

        def log(*args: Any) -> None:
            """Log messages to console and TagoIO"""
            # Only print locally if not auto-running
            if not os.environ.get("T_ANALYSIS_AUTO_RUN"):
                print(*args)

            # Handle error objects with stack trace
            processedArgs = []
            for arg in args:
                if hasattr(arg, "stack"):
                    processedArgs.append(arg.stack)
                else:
                    processedArgs.append(arg)

            # Convert all arguments to strings
            argsStrings = [self._stringifyMsg(arg) for arg in processedArgs]

            # Send to TagoIO console
            try:
                tagoConsole.log(" ".join(argsStrings))
            except Exception as e:
                print(f"Console error: {e}", file=sys.stderr)

        def context():
            pass

        context.log = log
        context.token = token
        context.environment = environment
        context.analysis_id = analysisID

        # Execute analysis function
        if inspect.iscoroutinefunction(self.analysis):
            # Async function
            try:
                asyncio.run(self.analysis(context, data or []))
            except Exception as error:
                log(error)
        else:
            # Sync function
            try:
                self.analysis(context, data or [])
            except Exception as error:
                log(error)

    def _localRuntime(self) -> None:
        """Set up local runtime environment for development"""
        if self.params.get("token") == "unknown":
            raise ValueError("To run analysis locally, you need a token")

        try:
            analysis = self.doRequest({"path": "/info", "method": "GET"})
        except Exception:
            analysis = None

        if not analysis:
            print("¬ Error :: Analysis not found or not active or invalid analysis token.", file=sys.stderr)
            return

        if analysis.get("run_on") != "external":
            print("¬ Warning :: Analysis is not set to run on external")

        # Open SSE connection
        try:
            sse = openSSEListening(
                {
                    "token": self.params.get("token"),
                    "region": self.params.get("region"),
                    "channel": "analysis_trigger",
                }
            )
        except Exception as e:
            print(f"¬ Connection error: {e}", file=sys.stderr)
            return

        tokenEnd = str(self.params.get("token", ""))[-5:]

        print(f"\n¬ Connected to TagoIO :: Analysis [{analysis.get('name', 'Unknown')}]({tokenEnd}) is ready.")
        print("¬ Waiting for analysis trigger... (Press Ctrl+C to stop)\n")

        try:
            for event in sse.events():
                if not self._running:
                    break

                try:
                    parsed = JSONParseSafe(event.data, {})
                    payload = parsed.get("payload")

                    if not payload:
                        continue

                    self._runLocal(
                        payload.get("environment", []),
                        payload.get("data", []),
                        payload.get("analysis_id", ""),
                        self.token,
                    )
                except Exception as e:
                    print(f"¬ Error processing event: {e}", file=sys.stderr)
                    continue

        except KeyboardInterrupt:
            print("\n¬ Analysis stopped by user. Goodbye!")
        except Exception as e:
            print(f"¬ Connection was closed: {e}", file=sys.stderr)
            print("¬ Trying to reconnect...")
        finally:
            self._running = False

    @staticmethod
    def use(
        analysis: AnalysisFunction,
        params: Optional[AnalysisConstructorParams] = None,
    ) -> "Analysis":
        """
        Create and configure Analysis instance with environment setup

        This static method provides a convenient way to create an Analysis instance
        while automatically configuring environment variables and runtime region.

        Example:
            ```python
            def my_analysis(context, scope):
                context.log("Hello from analysis!")

            analysis = Analysis.use(my_analysis, {"token": "my-token"})
            ```
        """
        if params is None:
            params = {"token": "unknown"}

        return Analysis(params).init(analysis)
