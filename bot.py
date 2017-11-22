from user import User
import json as js
import websocket # websockets
import threading
import time
from parser import parse_response
from termcolor import cprint

class Bot():

    def __init__(
        self,
        token,
        on_message = None,
        on_error = None,
        on_close = None
    ):
        self.debug = True
        self.token = token
        self.user = User(token=token)
        self.guilds = []
        self.gateway_url = js.loads(self.user.get_gateway())["url"]
        self.sequence = None
        self.heartbeat = js.dumps({
            "op": 1,
            "d": self.sequence
        })
        self.running = self.connect()
        if self.running:
            self.routine_thread = threading.Thread(group=None, target=self.routine)
            self.routine_thread.start()
            self.identify()
        self.heartbeat = js.dumps({
            "op": 1,
            "d": (self.sequence if type(self.sequence) == int() else "null")
        })
        self.receive_thread = threading.Thread(group=None, target=self.receive)

        self.receive_thread.start()

    def connect(self):
        self.ws = websocket.create_connection("%s?v=6&encoding=json" % self.gateway_url)
        parse_response(self.ws.recv(), self)
        return True



    def receive(self):
        while(self.running):
            response = self.ws.recv()
            parse_response(response, self)

    def routine(self):
        while(self.running):
            self.ws.send(self.heartbeat)
            cprint("Heartbeat sent with", "blue")
            cprint("| s:{}".format(self.sequence), "blue")
            # print(self.ws.recv())
            time.sleep(self.heartbeat_interval//1000)



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
                        "name": "Coder un bot",
                        "type": 1,
                    },
                    "status": "online",
                    #"since":
                    "afk": "false"
                }
            }
        }
        )
        self.ws.send(payload)
