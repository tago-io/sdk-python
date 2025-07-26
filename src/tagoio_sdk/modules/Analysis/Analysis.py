import json
import os
import signal
import sys

from typing import Any
from typing import Callable
from typing import Optional

from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.infrastructure.api_sse import openSSEListening
from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisEnvironment
from tagoio_sdk.modules.Services import Services


T_ANALYSIS_CONTEXT = os.environ.get("T_ANALYSIS_CONTEXT") or None


class Analysis(TagoIOModule):
    def __init__(self, params):
        super().__init__(params)
        self._running = True

    def _signal_handler(self, signum, frame):
        """Handle Ctrl+C gracefully"""
        print("\n¬ Analysis stopped by user. Goodbye!")
        self._running = False
        sys.exit(0)

    def init(self, analysis: Callable):
        self._analysis = analysis

        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        if T_ANALYSIS_CONTEXT is None:
            self.__localRuntime()
        else:
            self.__runOnTagoIO()

    def __runOnTagoIO(self):
        def context():
            pass

        context.log = print
        context.token = os.environ["T_ANALYSIS_TOKEN"]
        context.analysis_id = os.environ["T_ANALYSIS_ID"]
        try:
            context.environment = json.loads(os.environ["T_ANALYSIS_ENV"])
        except (KeyError, json.JSONDecodeError):
            context.environment = []

        try:
            data = json.loads(os.environ["T_ANALYSIS_DATA"])
        except (KeyError, json.JSONDecodeError):
            data = []

        self._analysis(context, data)

    def __runLocal(
        self,
        environment: list[AnalysisEnvironment],
        data: list[Any],
        analysis_id: str,
        token: str,
    ):
        """Run Analysis @internal"""

        def log(*args: any):
            print(*args)
            log_message = " ".join(str(arg) for arg in args)
            Services.Services({"token": token}).console.log(log_message)

        def context():
            pass

        context.log = log
        context.token = token
        context.environment = environment
        context.analysis_id = analysis_id

        self._analysis(context, data or [])

    def __localRuntime(self):
        analysis = self.doRequest({"path": "/info", "method": "GET"})

        if not analysis:
            print("¬ Error :: Analysis not found or not active.")
            return

        if analysis.get("run_on") != "external":
            print("¬ Warning :: Analysis is not set to run on external")

        tokenEnd = self.token[-5:]

        try:
            sse = openSSEListening(
                {
                    "token": self.token,
                    "region": self.region,
                    "channel": "analysis_trigger",
                }
            )
            print(
                f"\n¬ Connected to TagoIO :: Analysis [{analysis['name']}]({tokenEnd}) is ready."
            )
            print("¬ Waiting for analysis trigger... (Press Ctrl+C to stop)\n")
        except Exception as e:
            print("¬ Connection was closed, trying to reconnect...")
            print(f"Error: {e}")
            return

        try:
            for event in sse.events():
                if not self._running:
                    break

                try:
                    data = json.loads(event.data).get("payload")

                    if not data:
                        continue

                    self.__runLocal(
                        data["environment"],
                        data["data"],
                        data["analysis_id"],
                        self.token,
                    )
                except RuntimeError:
                    print("¬ Connection was closed, trying to reconnect...")
                    pass
        except KeyboardInterrupt:
            print("\n¬ Analysis stopped by user. Goodbye!")
        except Exception as e:
            print(f"\n¬ Unexpected error: {e}")
        finally:
            self._running = False

    @staticmethod
    def use(analysis: Callable, params: Optional[str] = {"token": "unknown"}):
        if not os.environ.get("T_ANALYSIS_TOKEN"):
            os.environ["T_ANALYSIS_TOKEN"] = params.get("token")
            Analysis(params).init(analysis)
        else:
            Analysis({"token": os.environ["T_ANALYSIS_TOKEN"]}).init(analysis)
