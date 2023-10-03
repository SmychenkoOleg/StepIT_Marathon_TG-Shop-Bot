import telebot
import dataArray

token = '6581936876:AAElLtR8UnsxPQ0IL-Rjbb4AY_k0mhfZn4Y'

shopbot = telebot.TeleBot(token)



@shopbot.message_handler(content_types=["text"])
def menu_check(message):
    user = message.from_user.username
    answer = message.text.lower()
    if any(item in answer for item in dataArray.words_0):
        shopbot.send_message(message.chat.id, f'Привіт, {user} ! Якими шляхами тебе завело до мене в гості?')
    elif any(item in answer for item in dataArray.words_1):
        shopbot.send_message(message.chat.id, f'Добре ! Тож обирай, будь ласка категорії товарів - в мене є бухло та цигарки !')
    elif any(item in answer for item in dataArray.words_2):
        shopbot.send_message(message.chat.id, f"Та ти ж, {user} ще нічого не вибрав та не поклав у кошик! \n І навіщо ото питати про кошик?")
    elif any(item in answer for item in dataArray.words_3):
        shopbot.send_message(message.chat.id,
                             f"Нарешті спитав! Ось тобі, {user} наші контакти. \n ☎️ Тел.:0 800 300 500, \n 📫e-mail: mail@mail.com")
    else:
        shopbot.send_message(message.chat.id,
                             f'Слухай, {user}, в тебе все нормально з пальцями? Бо ти щось таке пишеш, що я тебе не розумію!')


shopbot.polling(none_stop=True, interval=0)
