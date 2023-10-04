import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup

category_menu = types.ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True
alco = types.KeyboardButton("Бухло")
smoke = types.KeyboardButton("Цигарки")
main = types.KeyboardButton("Назад ⬅️")
category_menu.add(alco, smoke, main)
