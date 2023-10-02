import telebot

token = '6581936876:AAElLtR8UnsxPQ0IL-Rjbb4AY_k0mhfZn4Y'

shopbot = telebot.TeleBot(token)

words_1 = ["товари", "njdfhb", "товары"]
words_2 = ["кошик", "кошику", "rjibr", "корзина", "корзине"]
words_3 = ["контакти", "rjynfrnb", "контакты"]


@shopbot.message_handler(content_types=["text"])
def menu_check(message):
    user = message.from_user.username
    answer = message.text.lower()
    if any(item in answer for item in words_1):
        shopbot.send_message(message.chat.id, f'Привіт, {user} ! Оберіть будь ласка категорії товарів')
    elif any(item in answer for item in words_2):
        shopbot.send_message(message.chat.id, f"Та ви, {user} ще нічого не вибрали")
    elif any(item in answer for item in words_3):
        shopbot.send_message(message.chat.id,
                             f"Ось тобі, {user} наші контакти. \n ☎️ Тел.:0 800 300 500, \n 📫e-mail: mail@mail.com")
    else:
        shopbot.send_message(message.chat.id, f'Слухай, {user}, в тебе все нормально з пальцями? Бо ти щось таке пишеш, що я тебе не розумію!')


shopbot.polling(none_stop=True, interval=0)
