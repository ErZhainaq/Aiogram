import telebot
from telebot import types

bot = telebot.TeleBot("1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.from_user.id, "Footbal")

    keyboard = types.ReplyKeyboardMarkup(True,True,True)
    keyboard.row("1", "2" , "3"),
    keyboard.row("3", "4", "5"),
    keyboard.row("5", "6", "7")
    keyboard.row("7", "8", "9"),
    keyboard.row("0")
    bot.send_message(message.chat.id, "Barcelona [1], Bayern [2]", reply_markup=keyboard)
    bot.send_message(message.chat.id, "PSG [3], Man City [4]",reply_markup=keyboard)
    bot.send_message(message.chat.id, "Atletico Madrid [5],Juventus [6]",reply_markup=keyboard)
bot.polling()