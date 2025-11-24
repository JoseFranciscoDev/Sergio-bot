from datetime import datetime

from bot_instance import bot, telebot


@bot.message_handler(['hora_atual'])
def command_hora_atual(msg: telebot.types.Message) -> None:
    hora_atual:datetime = datetime.now()
    print(msg) 
    bot.reply_to(msg, f"Agora é {hora_atual}")
    
@bot.message_handler(['quem_e'])
def command_quem_voce_e(msg: telebot.types.Message) -> None:
    bot.reply_to(msg, "Eu sou o Sérgio Bot e fui feito pelo Zé pra ser seu escravo digital")
