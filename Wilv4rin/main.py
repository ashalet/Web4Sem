import logging
from typing import Optional, List

import requests
import telebot
import types
import sqlite3

TOKEN = '5643030605:AAEb6UirhSaiKaWa3hCk_cRxvlamYphlQYQ'
bot = telebot.TeleBot(TOKEN)
API_LINK = f'https://api.telegram.org/bot{TOKEN}'
db = sqlite3.connect('PyBot.db', check_same_thread=False)
cur = db.cursor()


@bot.message_handler(['start', 'go'])
def say_hello(message):
    try:
        cur.execute(f"INSERT INTO user (userID) VALUES ('{message.from_user.id}')")
        db.commit()
        return bot.reply_to(message, 'Теперь Вы будете получать оповещения о'
                                     ' новых работах на сайте \nhttps://localhost:8000/home'
                            )
    except Exception as e:
        return bot.reply_to(message, 'Вероятно, Вы уже получаете оповещения от этого бота😎'
                            )


@bot.message_handler(content_types=['text'])
def check_admin(message):
    if 'рассылка' in message.text.lower():
        # try:
        if message.from_user.id == 736884954:
            num_of_asset = message.text.split()[-1]
            mailing_list(int(num_of_asset))
        #     else:
        #         bot.send_message(message.from_user.id, 'Что то не так')
        # except:
        #     bot.send_message(message.from_user.id, 'Что то не так')


def mailing_list(num: int):
    users = cur.execute('SELECT userID FROM user').fetchall()
    data = requests.get(f'http://localhost:8000/api/mailing/{num}').json()
    print(data)

    imageURL = open(f'/home/kirill/PycharmProjects/VerMaks/portfolio/static/portfolio/img{data["asset"][0]["image"][30:]}', 'rb')
    #/home/kirill/PycharmProjects/VerMaks/portfolio/static/portfolio/img/Снимок_экрана_от_2022-10-16_13-57-47.png
    print(imageURL)
    asset = data['asset']
    # work = data['work']
    for user in range(0, len(users)):
        bot.send_photo(chat_id=users[user][0], photo=imageURL)
        requests.get(
            API_LINK + f'/sendMessage?chat_id={users[user][0]}&text=На сайте-портфолио «Wilv4rin» вышла новая работа под '
                       f'названием "{asset[0]["name_of_work"]}".'
                       f'\nСроки выполнения: {asset[0]["duration"]} дней.'
                       f'\nhttp://localhost:8000/work/{asset[0]["id"]}'

        )
        #'chat_id': chat_id, 'photo': photo_url, 'caption': caption_text

bot.polling()

# for user in range(0, len(users)):
#     requests.get(
#         API_LINK + f'/sendMessage?chat_id={users[user][0]}&text=На сайте-портфолио «Wilv4rin» вышла новая работа под '
#                    f'названием "{asset[0]["name_of_work"]}".'
#                    f'\nСроки выполнения: {asset[0]["duration"]} дней.'
#                    f'\nhttp://localhost:8000/work/{asset[0]["id"]}'
#
#     )
