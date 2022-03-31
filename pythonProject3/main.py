
import telebot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

crd = credentials.Certificate('Era.json')
firebase_admin.initialize_app(crd, {
    'databaseURL' : 'https://project-1-f389b-default-rtdb.firebaseio.com'
})
ref = db.reference()

bot = telebot.TeleBot("1891880035:AAFzKUhcoYvKxL-6Ddz7JegOqspPZL2xzHM")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'What is your name?')

@bot.message_handler(content_types=['text'])
def soz(message):
    if message == "Jasorken":
        bot.send_message(message.chat.id, "Youre from best place")
    else:
        user = message.text
        print(user)
        contains = ref.child('Registration').child('name').get()
        cStr = "" + str(contains)
        if cStr == "None":
            user_ref = ref.child('Registration').child('name')
            user_ref.set(user)
            bot.reply_to(message, "Thanks")

bot.polling()
