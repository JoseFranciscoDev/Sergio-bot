from datetime import datetime

from bot_instance import bot, telebot
from bot.decorators import add_command
from settings import COMMANDS


@bot.message_handler(["start"])
@add_command
def command_start(msg: telebot.types.Message):
    bot.reply_to(
        msg,
        "Prazer, eu sou o chatbot do zé e caso queira que eu 'pense' e te responda algo que não está na lista de comandos, basta perguntar sem usar '/'",
    )


@bot.message_handler(["hora_atual"])
@add_command
def command_hora_atual(msg: telebot.types.Message) -> None:
    hora_atual: datetime = datetime.now()
    bot.reply_to(msg, f"Agora é {hora_atual.hour}:{hora_atual.minute}")


@bot.message_handler(["quem_e"])
@add_command
def command_quem_voce_e(msg: telebot.types.Message) -> None:
    bot.reply_to(
        msg,
        'Eu sou o Sérgio Bot e fui feito pelo Zé, quer saber o que eu consigo fazer? Digite " /commands "',
    )


@bot.message_handler(["commands"])
@add_command
def command_commands(msg: telebot.types.Message) -> None:
    bot.reply_to(
        msg,
        f'Todos os comandos devem iniciar com "/". Atualmente os comandos disponíveis são: \n/{"\n/".join(str(command) for command in COMMANDS)}',
    )


@bot.message_handler(["chat_info"])
def command_chat_info(msg: telebot.types.Message) -> None:
    bot.reply_to(
        msg,
        f"Chat ID: {msg.chat.id}\n"
        f"Chat Type: {msg.chat.type}\n"
        f"Chat Title: {msg.chat.title}\n"
        f"User ID: {msg.from_user.id}\n"
        f"Username: {msg.from_user.username}\n"
        f"First_name: {msg.from_user.first_name}\n",
    )


"""
Comandos:
    adicionar_receita
    adicionar_despesa
    saldo_do_mes
"""
