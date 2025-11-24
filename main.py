from os import getenv

from dotenv import load_dotenv

import bot.commands as commands  # noqa: F401
from bot.gemini_client import GeminiClient
from bot_instance import bot, telebot

load_dotenv()

client = GeminiClient(api_key=getenv('gemini_api_key'),
                      instructions="Você é um chatbot que ajuda usuarios com questões do dia a dia e é um escravo virtual do zé",
                      model='gemini-2.5-flash',
                      )

@bot.message_handler()
def echo_user_messa(msg: telebot.types.Message):
    response = client.question(contents=msg)
    bot.reply_to(msg, str(response))
    
@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, "Prazer, eu sou o chatbot do zé e caso queira que eu 'pense' e te responda algo que não está na lista de comandos, basta perguntar sem usar '/'")


bot.infinity_polling()