import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from telebot import types

cred = credentials.Certificate('Era.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://project-1-f389b-default-rtdb.firebaseio.com"
})
ref = db.reference()

bot = telebot.TeleBot('1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    user_markup.row('Oda Tandau')
    bot.send_message(message.from_user.id,'Salam Aleikum', reply_markup=user_markup)
    sent = bot.send_message(message.chat.id, 'Bul Jatahana akimshiligi.Bugingi Kungi programmga qai odany tandaisyz''\n'
                                                'Bugin bizde bos odalar tizimi:')
    bot.register_next_step_handler(sent, Subject)


@bot.message_handler(content_types=['next'])
def Subject(message):
        if message.text == 'Oda Tandau':
            key = types.InlineKeyboardMarkup()
            bt = types.InlineKeyboardButton(text='210', callback_data='210')
            bt1 = types.InlineKeyboardButton(text='kitaphana', callback_data='kitaphana')
            bt2 = types.InlineKeyboardButton(text='Abay', callback_data='Abay')
            bt3 = types.InlineKeyboardButton(text='Ruhani Jangyru', callback_data='Ruhani Jangyru')
            bt4 = types.InlineKeyboardButton(text='Tabigat', callback_data='Tabigat')
            bt5 = types.InlineKeyboardButton(text='105', callback_data='105')
            bt6 = types.InlineKeyboardButton(text='107', callback_data='107')
            key.add(bt, bt1,bt2,bt3,bt4,bt5,bt6)
            sent1 = bot.send_message(message.chat.id, 'Kerek bolmeni tandanyz', reply_markup=key)
            bot.register_next_step_handler(sent1, inline)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    contains = ref.child('Oda Tandau').child(c.data).get()
    a = c.from_user.username
    ref.child('Oda Tandau').child(c.data).set({'name':'@'+a})


    bot.send_message(c.message.chat.id, 'Oda tandaly, bul oda bugin sizde')

bot.polling()