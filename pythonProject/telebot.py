import telebot
from telebot import types

bot = telebot.TeleBot("1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM")


@bot.message_handler(commands=["start"])
def start(message):
    kboard = types.InlineKeyboardMarkup(row_width=2)
    c1 = types.InlineKeyboardButton(text="1D", callback_data="1")
    c2 = types.InlineKeyboardButton(text="2C", callback_data="2")
    c3 = types.InlineKeyboardButton(text="3S", callback_data="3")
    c4 = types.InlineKeyboardButton(text="4E", callback_data="4")
    c5 = types.InlineKeyboardButton(text="5H", callback_data="5")
    c6 = types.InlineKeyboardButton(text="6A", callback_data="6")
    kboard.add(c1, c2, c3, c4, c5, c6)
    bot.send_message(message.chat.id, "Select your group", reply_markup=kboard)

