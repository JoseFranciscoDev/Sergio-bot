from settings import env_file
from dotenv import load_dotenv
from os import getenv
import telebot

load_dotenv(dotenv_path=env_file, override=True)

bot_api_key = getenv("bot_api_key")

bot = telebot.TeleBot(
    str(bot_api_key),
)
