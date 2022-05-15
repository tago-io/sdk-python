from tagoio_sdk.common.tagoio_module import TagoIOModule
import os
import json
from typing import Callable

T_ANALYSIS_CONTEXT = os.environ.get("T_ANALYSIS_CONTEXT") or None

if T_ANALYSIS_CONTEXT is None:
    from tagoio_sdk.infrastructure.api_socket import APISocket
    import asyncio

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


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

    def __runLocal(self, environment, data, analysis_id, token):
        def log(*args: any):
            print(*args)
            # Services(token).console.log(str(args)[1:][:-2])

        def context():
            pass

        setattr(context, "log", log)
        setattr(context, "token", token)
        setattr(context, "environment", environment)
        setattr(context, "analysis_id", analysis_id)

        self._analysis(context, data or [])

    def __localRuntime(self):
        tagoSocket = APISocket({"region": self.region, "token": self.token})
        sio = tagoSocket.sio

        async def connectSocket():
            def ready(analysisObj):
                print(
                    "Analysis [{AnalysisName}] Started.\n".format(
                        AnalysisName=analysisObj["name"]
                    )
                )

            def connect():
                print("Connected to TagoIO, Getting analysis information...")

            def disconnect():
                print("\nDisconnected from TagoIO.\n\n")

            def error(e: any):
                print("Connection error", e)

            def analysisTrigger(scope: any):
                self.__runLocal(
                    scope["environment"],
                    scope["data"],
                    scope["analysis_id"],
                    scope["token"],
                )

            sio.on("ready", ready)
            sio.on("error", error)
            sio.on("connect", connect)
            sio.on("disconnect", disconnect)
            sio.on("analysis::trigger", analysisTrigger)

            await tagoSocket.connect()

        try:
            loop.run_until_complete(connectSocket())
        except RuntimeError:
            pass

    @staticmethod
    def use(analysis: Callable, token: str = "unknown"):
        Analysis(token).init(analysis)
