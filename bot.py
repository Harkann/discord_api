from user import User
import json as js
import websocket # websockets
import _thread as thread
import time


class Bot():

    def __init__(
        self,
        token,
        on_message = None,
        on_error = None,
        on_close = None
    ):

        self.token = token
        self.user = User(token)
        self.gateway_url = js.loads(self.user.get_gateway())["url"]
        self.ws = websocket.create_connection(self.gateway_url)
        self.identify()
        self.response = self.ws.recv()

    def receive(self):
        pass
    def routine(self):
        pass

    def identify(self):
        payload = js.dumps(
        {
            "op": 2,
            "d": {
                "token": self.token,
                "properties": {
                    "$os": "linux",
                    "$browser": "test_api",
                    "$device":  "test_api",
                },
                "compress": "true",
                "large_thresold": 250,
                "shard": [0, 1],
                "presence": {
                    "game": {
                        "name": "test",
                        "type": 0,
                    },
                    "status": "online",
                    #"since":
                    "afk": "false"
                }
            }
        }
        )
        self.ws.send(payload)
