import telebot
from telebot import types

first_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
products = types.KeyboardButton("Товари")
cart = types.KeyboardButton("Кошик")
contacts = types.KeyboardButton("Контакти")
first_menu.add(products, cart, contacts)