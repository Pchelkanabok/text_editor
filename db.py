import sqlite3

class Datebase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))


    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))


    def get_user_id(self, prog):
        user_id_s = []
        with self.connection:
            result = self.cursor.execute("SELECT `user_id` FROM `users` WHERE `programm` = ?", (prog,)).fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            return user_id_s

    def get_user_id_year(self):
        user_id_s = []
        with self.connection:
            result = self.cursor.execute('SELECT `user_id` FROM `users` WHERE `year_p` = strftime("%Y", date("now"))').fetchall()
            for row in result:
                user_id_s.append(int(row[0]))
            return user_id_s


    def set_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `name` = ? WHERE `user_id` = ?", (name, user_id,))


    def get_name(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `name` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                name = str(row[0])
            return name


    def set_phone(self, user_id, phone):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `phone` = ? WHERE `user_id` = ?", (phone, user_id,))


    def get_phone(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `phone` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                phone = str(row[0])
            return phone


    def set_adm_post(self, user_id, adm_post):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `adm_post` = ? WHERE `user_id` = ?", (adm_post, user_id,))

    def get_adm_post(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `adm_post` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                adm_post = str(row[0])
            return adm_post


    def set_programm(self, user_id, programm):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `programm` = ? WHERE `user_id` = ?", (programm, user_id,))


    def get_programm(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `programm` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                programm = str(row[0])
            return programm


    def set_year_p(self, user_id, year_p):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `year_p` = ? WHERE `user_id` = ?", (year_p, user_id,))


    def get_year_p(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `year_p` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                year_p = str(row[0])
            return year_p


    def set_mail(self, user_id, mail):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `mail` = ? WHERE `user_id` = ?", (mail, user_id,))


    def get_mail(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `mail` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                mail = str(row[0])
            return mail


    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `signup` FROM `users` WHERE `user_id` = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `signup` = ? WHERE `user_id` = ?", (signup, user_id,))


    def kill_user(self, user_id):
        with self.connection:
            self.cursor.execute("DELETE FROM `users` WHERE `user_id` = ?", (user_id,))


