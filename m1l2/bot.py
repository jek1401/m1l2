from config import token
from config import facts
import telebot
import random
from random import choice


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет, я QuantumnBot\
""")

@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, "Я простой бот, написанный на Python. Используй /start или /help, чтобы узнать мое имя!")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    bot.reply_to(message, "Спасибо за фото! Оно крутое!")


@bot.message_handler(commands=['fact'])
def handle_fact_command(message):
    fact = random.choice(facts)
    bot.reply_to(message, fact)

jokes = [
    "Почему программисты не могут выбраться из леса? Потому что они всегда находят баги!",
    "Я бы рассказал вам шутку про SQL, но она может быть с ошибкой в запросе.",
    "Почему птицы не пользуются интернетом? Потому что боятся вирусов!"
]


@bot.message_handler(commands=['joke'])
def send_joke(message):
    joke = random.choice(jokes)
    bot.reply_to(message, joke)  

bot.infinity_polling()