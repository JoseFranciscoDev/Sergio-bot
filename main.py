from google.genai import types

import bot.commands as commands  # noqa: F401
from bot.db import add_message, get_history
from bot.gemini_client import GeminiClient
from bot_instance import bot, telebot
from bot.utils import is_valid_command
from os import getenv

client = GeminiClient(
    api_key=getenv("gemini_api_key"),
    instructions="Você é um chatbot que ajuda usuarios com questões do dia a dia, criado pelo José",
    model="gemini-2.5-flash",
)


@bot.message_handler()
def echo_user_message(msg: telebot.types.Message):
    user_message = str(msg.text)
    if is_valid_command(user_message):
        print("É um comando válido")
        print(user_message)
        chat_id = msg.chat.id
        add_message(chat_id=chat_id, message=user_message, role="user")

        history = get_history(chat_id=chat_id)

        gemini_history = [
            types.Content(role=message.role, parts=[types.Part(text=message.text)])
            for message in history
        ]

        response = client.question(contents=gemini_history)

        add_message(chat_id=chat_id, message=response, role="model")

        bot.reply_to(msg, response)
        return
    bot.reply_to(
        msg,
        'Esse não é um comando válido. Experimente usar "/commands" para ver os comandos disponíveis',
    )


bot.infinity_polling()
