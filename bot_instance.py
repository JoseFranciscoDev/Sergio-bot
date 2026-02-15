from os import getenv

import telebot
from dotenv import load_dotenv

load_dotenv()

bot_api_key = getenv("bot_api_key")

bot = telebot.TeleBot(
    str(bot_api_key),
)
