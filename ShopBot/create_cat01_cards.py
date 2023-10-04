from telebot import types

def create_cards():
    cards_keyb = types.InlineKeyboardMarkup()
    cards = open("category01_alco-list.csv", "r")
    db_alco = cards.readlines()
    cards.close()
    for alco_cards in db_alco:
        alco_pars = alco_cards.split(";")
        button = types.InlineKeyboardButton(text=f'{alco_pars[0]}, {alco_pars[1]}, витримка: {alco_pars[2]}, ціна: {alco_pars[3]}', callback_data=cards)
        cards_keyb.add(button)
        print(alco_pars)
