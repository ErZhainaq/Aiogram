import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from telebot import types

cred = credentials.Certificate('era.json')
firebase_admin.initialize_app(cred, {
    "databaseURL":"http://project-1-f389b-default-rtdb.firebaseio.com/"
})

ref = db.reference()

bot = telebot.TeleBot('1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM')


@bot.message_handler(commands=['start'])
def start(message):
    keyb = telebot.types.ReplyKeyboardMarkup(True)
    keyb.row(("Jazylu"))
    keyb.row("Bos uaqyt")
    bot.send_message(message.from_user.id, "Salam", reply_markup=keyb)
    sent = bot.send_message(message.chat.id, "Bizge online jazyla alasyz")
    bot.register_next_step_handler(sent, uaqyt)

@bot.message_handler(content_types=['text'])
def uaqyt(message):
    if message.text == "Jazylu":
        key = types.InlineKeyboardMarkup()
        bt1 = types.InlineKeyboardButton(text="10.000", callback_data="10:00")
        bt2 = types.InlineKeyboardButton(text="11.000", callback_data="11:00")
        bt3 = types.InlineKeyboardButton(text="12.000", callback_data="12:00")
        bt4 = types.InlineKeyboardButton(text="13.000", callback_data="13:00")
        bt5 = types.InlineKeyboardButton(text="14.000", callback_data="14:00")
        bt6 = types.InlineKeyboardButton(text="15.000", callback_data="15:00")
        bt7 = types.InlineKeyboardButton(text="16.000", callback_data="16:00")
        key.add(bt1, bt2, bt3, bt4, bt5, bt6, bt7)
        sent1 = bot.send_message(message.chat.id, "Bos uaqytty tandanyz", reply_markup=key)
        bot.register_next_step_handler(sent1, firebase)

@bot.callback_query_handler(func=lambda c: True)
def firebase(c):
    contains = ref.child('jazba').child(c.data).get()
    cSTR = '' + str(contains)

    if cSTR == 'None':
        a = c.from_user.username
        user_ref = ref.child('jazba').child(c.data)

        user_ref.set({'name': '@zhainaqov' + a})
        bot.send_message(c.message.chat.id, "Siz Jazyldynyz")
    else:
        bot.send_message(c.message.chat.id, " pwel ty. Sagan bos uaqyt jok!!!")

bot.polling()