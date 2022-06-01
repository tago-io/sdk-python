import os

tagoSDKconfig = {
    "requestAttempts": int(os.environ.get("TAGOIO_REQUEST_ATTEMPTS") or 5),
    "requestTimeout": 60,  # seconds
    "socketOpts": {
        "reconnectionDelay": 10,  # seconds
        "reconnection": True,
        "transports": ["websocket"],
    },
}
