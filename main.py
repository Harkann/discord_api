#! /usr/bin/env python3
import requests
import secrets
from user import User
from bot import Bot
TOKEN = secrets.TOKEN

user = User(TOKEN)

user.patch_user(username="Coucou les amis")

bot = Bot(TOKEN)
# bot.identify()
