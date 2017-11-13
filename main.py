#! /usr/bin/env python3
import requests
import secrets
from user import User
from bot import Bot
TOKEN = secrets.TOKEN

user = User(TOKEN)
print(user.get_user())
print(user.get_user_from_id("151353859208380418"))
print(user.get_servers())
print(user.get_connections())
print(user.get_gateway())
#patch_user(TOKEN,username="Plibidi")

bot = Bot(TOKEN)
# bot.identify()
