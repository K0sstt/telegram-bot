import telebot

bot = telebot.TeleBot("1258885982:AAHoO--kqaVSloky2EEa1QpvHGfdBciJ-Fc")


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
