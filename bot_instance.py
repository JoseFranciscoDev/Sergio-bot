from os import getenv
import telebot

bot_api_key = getenv("bot_api_key")

bot = telebot.TeleBot(
    str(bot_api_key),
)
