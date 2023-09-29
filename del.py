'''
import logging

from aiogram import Bot, Dispatcher, executor, types

import markups as nav

from db import Datebase

import config

import numbers

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram_broadcaster import MessageBroadcaster


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)
db = Datebase('database2del.db')

'''
'''
from telebot import TeleBot
import config
from db import Datebase

BOT_TOKEN = config.TOKEN
bot = TeleBot(BOT_TOKEN)
db = Datebase('database2del.db')
users = []

#users_1 = db.get_user_id("Журналистка")
#users_2 = db.get_user_id("Медиакоммуникации в Москве")
users_3 = db.get_user_id("Буду поступать на обе в Москве")
users_4 = db.get_user_id("Медиакоммуникации в Питере")
users_5 = db.get_user_id("Буду поступать на все")
users = users_5 + users_4 + users_3
print (len(users))
print (users)
for message_id in range(1,1000):
        print(message_id)
        try:
            bot.delete_message(
                chat_id=484623073,
                message_id=message_id,
            )
        except Exception as ex:
            print(ex)
'''


'''
for user_id in users:
    print('----------------------------------------------------------------------------------')
    print(user_id)
    print('----------------------------------------------------------------------------------')
    for message_id in range(1,1000):
        print(message_id)
        try:
            bot.delete_message(
                chat_id=user_id,
                message_id=message_id,
            )
        except Exception as ex:
            print(ex)
'''
from telebot import TeleBot
import config
from db import Datebase
import telebot

BOT_TOKEN = config.TOKEN
bot = TeleBot(BOT_TOKEN)
db = Datebase('database2del.db')

users = []
#users_1 = db.get_user_id("Журналистка")
#users_2 = db.get_user_id("Медиакоммуникации в Москве")
users_3 = db.get_user_id("Буду поступать на обе в Москве")
users_4 = db.get_user_id("Медиакоммуникации в Питере")
users_5 = db.get_user_id("Буду поступать на все")
users = users_5 + users_4 + users_3
print (len(users))
for user_id in users:
    print('----------------------------------------------------------------------------------')
    print(user_id)
    print('----------------------------------------------------------------------------------')
    for message_id in range(1,1000):
        print(message_id)
        try:
            bot.delete_message(
                chat_id=user_id,
                message_id=message_id,
            )
        except Exception as ex:
            print(ex)