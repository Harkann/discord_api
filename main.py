#! /usr/bin/env python3
import requests
import random
import secrets
from user import User
from bot import Bot

TOKEN = secrets.TOKEN
ALLOWED_CHANS = []
ALLOWED_SERVERS = []
user = User(TOKEN)

user.patch_user(username="Coucou les amis")

class MyBot(Bot):
    def __init__(self, token):
        super().__init__(token)

    def on_message_create(self, message):
        if int(message.channel_id) in ALLOWED_CHANS or int(message.guild_id) in ALLOWED_SERVERS:
            if message.content == "!rand":
                self.user.send_message(message.channel_id, str(random.randint(0,100)))


bot = MyBot(TOKEN)


bot.start()
