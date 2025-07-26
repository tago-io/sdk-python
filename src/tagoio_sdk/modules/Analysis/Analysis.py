import json
import os
from typing import Any, Callable, Optional

from tagoio_sdk.common.tagoio_module import TagoIOModule
from tagoio_sdk.infrastructure.api_sse import openSSEListening
from tagoio_sdk.modules.Analysis.Analysis_Type import AnalysisEnvironment
from tagoio_sdk.modules.Services import Services

T_ANALYSIS_CONTEXT = os.environ.get("T_ANALYSIS_CONTEXT") or None


class Analysis(TagoIOModule):
    def init(self, analysis: Callable):
        self._analysis = analysis

        if T_ANALYSIS_CONTEXT is None:
            self.__localRuntime()
        else:
            self.__runOnTagoIO()

    def __runOnTagoIO(self):
        def context():
            pass

        setattr(context, "log", print)
        setattr(context, "token", os.environ["T_ANALYSIS_TOKEN"])
        setattr(context, "analysis_id", os.environ["T_ANALYSIS_ID"])
        try:
            setattr(context, "environment", json.loads(os.environ["T_ANALYSIS_ENV"]))
        except:
            setattr(context, "environment", [])

        try:
            data = json.loads(os.environ["T_ANALYSIS_DATA"])
        except:
            data = []

        self._analysis(context, data)

    def __runLocal(self, environment: list[AnalysisEnvironment], data: list[Any], analysis_id: str, token: str):
        """ Run Analysis @internal"""
        def log(*args: any):
            print(*args)
            Services.Services({"token": token}).console.log(str(args)[1:][:-2])

        def context():
            pass

        setattr(context, "log", log)
        setattr(context, "token", token)
        setattr(context, "environment", environment)
        setattr(context, "analysis_id", analysis_id)

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
            sse = openSSEListening({
                "token": self.token,
                "region": self.region,
                "channel": "analysis_trigger"
            })
            print(f"\n¬ Connected to TagoIO :: Analysis [{analysis['name']}]({tokenEnd}) is ready.")
            print("¬ Waiting for analysis trigger...\n")
        except Exception as e:
            print("¬ Connection was closed, trying to reconnect...")
            print(f"Error: {e}")
            return

        for event in sse.events():
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

    @staticmethod
    def use(analysis: Callable, params: Optional[str] = {"token": "unknown"}):
        if not os.environ.get("T_ANALYSIS_TOKEN"):
            os.environ["T_ANALYSIS_TOKEN"] = params.get("token")
            Analysis(params).init(analysis)
        else:
            Analysis({"token": os.environ["T_ANALYSIS_TOKEN"]}).init(analysis)
