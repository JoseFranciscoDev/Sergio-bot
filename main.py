from os import getenv

from dotenv import load_dotenv
from google import genai
from google.genai import types

import bot.commands as commands  # noqa: F401
from bot_instance import bot, telebot

load_dotenv()

client = genai.Client(api_key=getenv('gemini_api_key'), )

@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, "Oieee")


@bot.message_handler()
def echo_user_messa(msg: telebot.types.Message):
    response = client.models.generate_content(model='gemini-2.5-flash', contents=str(msg), config=types.GenerateContentConfig(
        system_instruction="Você é um chatbot que ajuda usuarios com questões do dia a dia e é um escravo virtual do zé"
    ))
    bot.reply_to(msg, str(response.text))
    
bot.infinity_polling()