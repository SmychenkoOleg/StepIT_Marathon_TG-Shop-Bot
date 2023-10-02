import telebot

token = '6581936876:AAElLtR8UnsxPQ0IL-Rjbb4AY_k0mhfZn4Y'

shopbot = telebot.TeleBot(token)


@shopbot.message_handler(content_types=["text"])
def menu_check(message):
    if message.text == "Товари" or "товари" or "товары":
        shopbot.send_message(message.chat.id, "Оберіть будь ласка категорії товарів")
    if message.text == "Кошик":
        shopbot.send_message(message.chat.id, "Та ви ще нічого не вибрали")
    if message.text == "Контакти":
        shopbot.send_message(message.chat.id, "тел.:0 800 300 500")


shopbot.polling(none_stop=True, interval=0)
