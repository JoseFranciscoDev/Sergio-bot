from datetime import datetime

from bot_instance import bot, telebot

@bot.message_handler(["start"])
def start(msg: telebot.types.Message):
    bot.reply_to(
        msg,
        "Prazer, eu sou o chatbot do zé e caso queira que eu 'pense' e te responda algo que não está na lista de comandos, basta perguntar sem usar '/'",
    )


@bot.message_handler(["hora_atual"])
def command_hora_atual(msg: telebot.types.Message) -> None:
    hora_atual: datetime = datetime.now()
    print(msg)
    bot.reply_to(msg, f"Agora é {hora_atual}")


@bot.message_handler(["quem_e"])
def command_quem_voce_e(msg: telebot.types.Message) -> None:
    bot.reply_to(
        msg,
        'Eu sou o Sérgio Bot e fui feito pelo Zé, quer saber o que eu consigo fazer? Digite " /commands "',
    )


@bot.message_handler(["commands"])
def commands(msg: telebot.types.Message) -> None:
    bot.reply_to(
        msg,
        'Todos os comandos devem iniciar com "/"Atualmente os comandos disponíveis são: \n/quem_e\n/hora_atual',
    )


"""
Comandos:
    adicionar_receita
    adicionar_despesa
    saldo_do_mes
"""
