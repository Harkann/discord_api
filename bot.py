from user import User
import json as js
import websocket # websockets
import threading
import time
from parser import parse_response
from config import VERSION
from termcolor import cprint

class Bot():

    def __init__(self, token):
        self.debug = True
        self.token = token
        self.user = User(token=token)
        self.guilds = []
        self.gateway_url = js.loads(self.user.get_gateway())["url"]
        self.sequence = None
        self.running = False
        self.routine_thread = None
        self.receive_thread = None
        self.session_id = None

    def start(self):
        self.running = self.connect()
        if self.running:
            self.routine_thread = threading.Thread(group=None, target=self.routine)
            self.routine_thread.start()
            self.ws.send(self._identify())

        self.receive_thread = threading.Thread(group=None, target=self.receive)

        self.receive_thread.start()

    def connect(self):
        self.ws = websocket.create_connection("{}?v={}&encoding=json".format(self.gateway_url, VERSION))
        parse_response(self.ws.recv(), self)
        return True



    def receive(self):
        while(self.running):
            response = self.ws.recv()
            parse_response(response, self)

    def routine(self):
        while(self.running):
            self.ws.send(self._heartbeat())
            cprint("Heartbeat sent with", "blue")
            cprint("| s:{}".format(self.sequence), "blue")
            # print(self.ws.recv())
            time.sleep(self.heartbeat_interval//1000)


    def on_message_create(self, message):
        pass

    def _heartbeat(self):
        return js.dumps({
            "op": 1,
            "d": (self.sequence if type(self.sequence) == int() else "null")
        })

    def _resume(self):
        return js.dumps({
            "op": 6,
            "d": {
                "token": self.token,
                "session_id": self.session_id,
                "seq": self.sequence
            }
        })

    def _identify(self):
        return js.dumps({
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
        })

    def _request_guild_members(self, guild_id, query="", limit=0):
        return js.dumps({
            "op": 8,
            "d": {
                "guild_id": str(guild_id),
                "query": query,
                "limit": limit
            }
        })

    def _update_voice_state(self, guild_id, channel_id, self_mute, self_deaf):
        return js.dumps({
            "op": 4,
            "d": {
                "guild_id": guild_id,
                "channel_id": channel_id,
                "self_mute": self_mute,
                "self_deaf": self_deaf
            }
        })

    def _update_status(self, game, status, afk, since="null"):
        pass
