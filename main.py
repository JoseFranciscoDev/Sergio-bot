from os import getenv

from dotenv import load_dotenv
from google.genai import types

import bot.commands as commands  # noqa: F401
from bot.db import add_message, get_history
from bot.gemini_client import GeminiClient
from bot_instance import bot, telebot

load_dotenv()

client = GeminiClient(api_key=getenv('gemini_api_key'),
                      instructions="Você é um chatbot que ajuda usuarios com questões do dia a dia, criado pelo José",
                      model='gemini-2.5-flash',
                      )

@bot.message_handler()
def echo_user_message(msg: telebot.types.Message):
    # response = client.question(contents=msg)
    # print(msg.text)
    # bot.reply_to(msg, str(response))
    user_message = msg.text
    print(user_message)
    chat_id = msg.chat.id
    add_message(chat_id=chat_id, message=user_message, role="user")
    
    history = get_history(chat_id=chat_id)
    
    gemini_history = [
        types.Content(role=message.role, parts=[types.Part(text=message.text)])
        for message in history
    ]
    
    response = client.question(contents=gemini_history)

    add_message(msg.chat.id, response, role="model")

    bot.reply_to(msg, str(response))
    
@bot.message_handler(['start'])
def start(msg: telebot.types.Message):
    bot.reply_to(msg, "Prazer, eu sou o chatbot do zé e caso queira que eu 'pense' e te responda algo que não está na lista de comandos, basta perguntar sem usar '/'")


bot.infinity_polling()