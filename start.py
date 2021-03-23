import json
import random
import time
import os
import requests
import telebot
from fake_useragent import UserAgent

from sqlighter import SQLighter


def main():
    карты = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A"

    }
    карты_номер_по_названию = {
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14

    }

    def get(x):
        return int(x[0][0])

    url = "https://m.melbet6.com/LiveFeed/Get1x2_VZip?sports=146&champs=1643503&count=50&mode=4&country=1&partner=8&getEmpty=true&mobi=true"

    chat_id = "-1001242785018"
    db = SQLighter('user.db')
    bot = telebot.TeleBot(str(os.environ.get('BOT_TOKEN')))
    cookie = {'session': '17ab96bd8ffbe8ca58a78657a918558'}

    while True:
        time.sleep(10)
        page = requests.get(url)

        if page.status_code == 200:

            response = requests.get(url, headers={'User-Agent': UserAgent().chrome}, cookies=cookie)

            data = json.loads(json.dumps(response.json()))

            try:

                number_game1 = data["Value"][1]

                if get(db.get_game1(1)) != number_game1['I'] and get(db.get_game_old_id(1)) != number_game1['I']:

                    link_game = f"https://m.melbet6.com/LiveFeed/GetGameZip?id={get(db.get_game_old_id(1))}&tzo=5&isSubGames=true&GroupEvents=true&countevents=50&partner=8&grMode=2&country=1&marketType=1&mobi=true"

                    response2 = requests.get(link_game, headers={'User-Agent': UserAgent().chrome}, cookies=cookie)

                    data2 = json.loads(json.dumps(response2.json()))

                    def score(command):
                        try:
                            number_game_stats = str(data2['Value']['SC']['S'][command]["Value"]).replace("[",
                                                                                                         "").replace(
                                "]", "").replace(" ", "").replace("}", "").replace("{", " ")
                        except TypeError:
                            db.update_game_old_id(1, get(db.get_game1(1)))
                            db.update_game_old_number(1, get(db.get_game_number(1)))
                            db.update_old_card(1, get(db.get_card(1)))
                            return

                        try:
                            карта1 = int(number_game_stats.split(',')[1].replace('"CV":', ""))

                        except IndexError:
                            карта1 = 0

                        try:
                            карта2 = int(number_game_stats.split(',')[4].replace('"CV":', ""))

                        except IndexError:
                            карта2 = 0
                        try:
                            карта3 = int(number_game_stats.split(',')[7].replace('"CV":', ""))

                        except IndexError:
                            карта3 = 0
                        try:
                            карта4 = int(number_game_stats.split(',')[10].replace('"CV":', ""))

                        except IndexError:
                            карта4 = 0
                        if command == 1:
                            db.update_old_card1(1, карта1)
                            db.update_old_card2(1, карта2)
                            db.update_old_card3(1, карта3)
                            db.update_old_card4(1, карта4)
                        elif command == 0:
                            db.update_old_1_card(1, карта1)
                            db.update_old_1_card2(1, карта2)
                            db.update_old_1_card3(1, карта3)
                            db.update_old_1_card4(1, карта4)

                        карты = карта1, карта2, карта3, карта4

                        return карты

                    def проверка_карт():

                        if score(0) is not None and score(1) is not None:
                            for i in score(0) + score(1):
                                if i == get(db.get_card_old(1)):
                                    try:
                                        message_edit = f"🎮Игра:{get(db.get_game_old_number(1))}🎮\n🎲Значение: {карты[get(db.get_card_old(1))]} обоим🎲\n ✅"
                                        bot.edit_message_text(chat_id=chat_id, message_id=get(db.get_message_old(1)),
                                                          text=message_edit)
                                    except: 
                                        print(1)
                                    return 1
                        else:
                            return 0

                    if проверка_карт() != 1:
                        try:
                            message_edit = f"🎮Игра: {get(db.get_game_old_number(1))}🎮\n🎲Значение: {карты[get(db.get_card_old(1))]} обоим🎲\n ❌"
                            bot.edit_message_text(chat_id=chat_id, message_id=get(db.get_message_old(1)),
                                              text=message_edit)
                        except: 
                            print(1)

                    db.update_game_old_id(1, get(db.get_game1(1)))

                    db.update_game1(1, number_game1['I'])

                    db.update_old_card(1, get(db.get_card(1)))

                    db.update_message_old(1, get(db.get_message(1)))

                    db.update_game_old_number(1, get(db.get_game_number(1)))

                    db.update_game_number(1, number_game1['DI'])

                    карты_прошлой_игры = get(db.get_old_card1(1)), get(db.get_old_card2(1)), get(
                        db.get_old_card3(1)), get(db.get_old_card4(1)), get(db.get_old_1_card1(1)), get(
                        db.get_old_1_card2(1)), get(
                        db.get_old_1_card3(1)), get(db.get_old_1_card4(1))

                    print(карты_прошлой_игры)

                    def send_stavka(x):
                        message_for_chat = f"🎮Игра: {number_game1['DI']}🎮\n🎲Значение: {карты[x]} обоим🎲\n✨Догон: 1 игра✨\n⚠80%⚠"
                        db.update_card(1, x)
                        db.update_message(1, bot.send_message(chat_id, message_for_chat).id)


                    def стратегия(x,y):
                        for i in карты_прошлой_игры:
                            if i == x:
                                send_stavka(y)
                                main()

                    стратегия(14, 11)
                    стратегия(11, 12)
                    стратегия(12,14)
                    стратегия(13, 13)



            except IndexError:
                print()


if __name__ == '__main__':
    main()
