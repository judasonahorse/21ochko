import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def get_game1(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT game_id FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_game_old_id(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT game_old_id FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_card(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT card FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_card_old(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_card FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_message(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT message FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_message_old(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT message_old FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_game_old_number(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT game_old_number FROM `userdata` WHERE `user_id` = ?',
                                       (user_id,)).fetchall()

    def get_game_number(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT game_number FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_card1(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_card1 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_card2(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_card2 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_card3(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_card3 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_card4(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_card4 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_1_card1(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_1_card1 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_1_card2(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_1_card2 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_1_card3(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_1_card3 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_old_1_card4(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT old_1_card4 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def update_game1(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `game_id` = ? WHERE `user_id` = ?", (status, user_id))

    def update_old_card(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_card` = ? WHERE `user_id` = ?", (status, user_id))

    def update_game_old_id(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `game_old_id` = ? WHERE `user_id` = ?", (status, user_id))

    def update_card(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `card` = ? WHERE `user_id` = ?", (status, user_id))

    def update_message(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `message` = ? WHERE `user_id` = ?", (status, user_id))

    def update_message_old(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `message_old` = ? WHERE `user_id` = ?", (status, user_id))

    def update_game_old_number(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `game_old_number` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_game_number(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `game_number` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_card1(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_card1` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_card2(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_card2` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_card3(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_card3` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_card4(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_card4` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_1_card(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_1_card1` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_1_card2(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_1_card2` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_1_card3(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_1_card3` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_old_1_card4(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `old_1_card4` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
