import logging

from aiogram import Bot, Dispatcher, executor, types

import markups as nav

from db import Datebase

import config

import numbers

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram_broadcaster import MessageBroadcaster



logging.basicConfig(level = logging.INFO)


bot = Bot(config.TOKEN)
dp = Dispatcher(bot)

db = Datebase('database2.db')


async def message_handler(msg: types.Message):
    if db.get_programm(msg.from_user.id) == 'Всем':
        db.set_adm_post(msg.from_user.id, 0)
        db.set_programm(msg.from_user.id, "Буду поступать на все")
        users_1 = db.get_user_id("Журналистка")
        users_2 = db.get_user_id("Медиакоммуникации в Москве")
        users_3 = db.get_user_id("Буду поступать на обе в Москве")
        users_4 = db.get_user_id("Медиакоммуникации в Питере")
        users_5 = db.get_user_id("Буду поступать на все")
        await MessageBroadcaster(users_1, msg).run()
        await MessageBroadcaster(users_2, msg).run()
        await MessageBroadcaster(users_3, msg).run()
        await MessageBroadcaster(users_4, msg).run()
        await MessageBroadcaster(users_5, msg).run()
    elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
        db.set_adm_post(msg.from_user.id, 0)
        db.set_programm(msg.from_user.id, "Буду поступать на все")
        users_1 = db.get_user_id("Журналистка")
        users_2 = db.get_user_id("Буду поступать на обе в Москве")
        users_3 = db.get_user_id("Медиакоммуникации в Москве")
        users_4 = db.get_user_id("Буду поступать на все")
        await MessageBroadcaster(users_1, msg).run()
        await MessageBroadcaster(users_2, msg).run()
        await MessageBroadcaster(users_3, msg).run()
        await MessageBroadcaster(users_4, msg).run()
    elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
        db.set_adm_post(msg.from_user.id, 0)
        db.set_programm(msg.from_user.id, "Буду поступать на все")
        db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
        users = db.get_user_id(db.get_programm(msg.from_user.id))
        users_ = db.get_user_id("Буду поступать на все")
        await MessageBroadcaster(users, msg).run()
        await MessageBroadcaster(users_, msg).run()
    elif db.get_programm(msg.from_user.id) == 'Абитуриенты этого года':
        db.set_adm_post(msg.from_user.id, 0)
        db.set_programm(msg.from_user.id, "Буду поступать на все")
        users = db.get_user_id_year()
        await MessageBroadcaster(users, msg).run()
    else:
        db.set_adm_post(msg.from_user.id, 0)
        users = db.get_user_id(db.get_programm(msg.from_user.id))
        users_ = db.get_user_id("Буду поступать на все")
        users__ = db.get_user_id("Буду поступать на обе в Москве")
        await MessageBroadcaster(users, msg).run()
        await MessageBroadcaster(users_, msg).run()
        await MessageBroadcaster(users__, msg).run()
async def message_handler_all(msg: types.Message):
    db.set_adm_post(message.from_user.id, 0)
    users = db.get_user_id(db.get_programm(msg.from_user.id))  # Your users list
    await MessageBroadcaster(users, msg).run()

@dp.message_handler(commands = ['restart'])
async def rest(message: types.Message):
    await bot.send_message(message.chat.id, "Вы уверены, что хотите стереть данные о себе и перезапустить бота?",
                           reply_markup = nav.RestYN)
    #dp.register_message_handler (rest, content_types=types.ContentTypes.ANY)
    db.set_signup(message.from_user.id, 'restart')

@dp.message_handler(commands = ['help'])
async def halp(message: types.Message):
    await bot.send_message(message.chat.id, "/start - Начать работу с ботом\n"
                                            "/restart - Перезапустить бота и стереть данные о себе\n"
                                            "/help - Доступные команды")
'''
async def rest(msg: types.Message):
    if msg.text == "Да":
        db.kill_user(msg.from_user.id)
        await bot.send_message(message.chat.id, "Отправь /start\nЧтобы начать всё сначала.",
                               reply_markup = types.ReplyKeyboardMarkup())
    else:
        await bot.send_message(message.chat.id, "Главное меню...",
                               reply_markup=nav.mainMenu)
'''

@dp.message_handler(commands = ['start'])
async def start(message: types.Message):
    if (not db.user_exists(message.from_user.id)):
        db.add_user(message.from_user.id)
        await bot.send_message(message.chat.id,
                         "Привет, {0.first_name}!\nЭто бот Школы медиа Вышки. \n\n"
                         "Он поможет абитуриентам получать все важные новости про поступление удобнее,"
                         " чем в электронной почте или на сайте. \n\n"
                         "Чтобы все заработало, пожалуйста, пройдите регистрацию.\n\n"
                         "Напишите фамилию и имя — это нужно, чтобы в дальнейшем регистрировать вас на события "
                         "Школы медиа.".format(
                             message.from_user, bot.get_me()),
                         parse_mode='html', reply_markup = types.ReplyKeyboardRemove())
        #await bot.send_message(message.from_user.id, "Напишите ваше ФИО")
    elif db.get_signup(message.from_user.id) != 'done' and db.get_signup(message.from_user.id) != 'admin_true':
        await bot.send_message(message.from_user.id, "Нажмите продолжить", reply_markup = nav.Next)
    else:
        await bot.send_message(message.from_user.id, "Вы уже зарегистрированы!", reply_markup = nav.mainMenu)

@dp.message_handler(commands = ['admin'])
async def admin(message: types.Message):
    if db.get_signup(message.from_user.id) != 'admin_true':
        await bot.send_message(message.from_user.id, "Вы не вошли, как админ", reply_markup = nav.mainMenu)
    else:
        await bot.send_message(message.from_user.id, "Меню админа!", reply_markup=nav.AdmMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        print(message.message_id)
        print(message.chat.id)
        if message.text == 'Профиль':

            str = "Данные вашего профиля:\n" \
                  "Вас зовут: " + db.get_name(message.from_user.id) +\
                  "\n" + "Телефон: " + db.get_phone(message.from_user.id) +\
                  "\n" + "Email: " + db.get_mail(message.from_user.id) +\
                  "\n" + "Программа: " + db.get_programm(message.from_user.id) +\
                  "\n" + "Год поступления: " + db.get_year_p(message.from_user.id)

            await bot.send_message(message.from_user.id, str, reply_markup = nav.Prof)

        elif message.text == 'Задать вопрос':
            url = "https://t.me/hsemediasupport"
            await bot.send_message(message.from_user.id, url, parse_mode="html")

        elif message.text == 'Полезные ссылки':
            urls = "<strong>Журналистика:</strong> \n" \
                   "🔹<a href='https://www.hse.ru/ba/journ/about'>О программе</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/tracks'>Траектория поступления</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/requirements'>Подготовка</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/key-disciplines'>Ключевые дисциплины</a>\n" \
                    "🔹<a href='https://cmd.hse.ru/mediaday/'>Расписание дней открытых дверей</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/journ/foreign_students'>Важная информация для иностранных студентов</a>\n" \
                    "🔹<a href='https://chat.hse.media/'>Записаться на индивидуальную консультацию</a>\n\n" \
                    "<strong>Медикоммуникации:</strong> \n" \
                    "🔹<a href='https://www.hse.ru/ba/media/about'>О программе</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/tracks'>Траектория поступления</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/requirements'>Подготовка</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/career'>Будущая профессия</a>\n" \
                    "🔹<a href='https://cmd.hse.ru/mediaday/'>Расписание дней открытых дверей</a>\n" \
                    "🔹<a href='https://www.hse.ru/ba/media/foreign_students'>Важная информация для иностранных студентов</a>\n" \
                    "🔹<a href='https://chat.hse.media/'>Записаться на индивидуальную консультацию</a>\n" \
                    "🔹<a href='https://spb.hse.ru/ba/mediacom/tracks'>Программа «Медиакоммуникации» в Питере</a>\n"
            await bot.send_message(message.from_user.id, urls, parse_mode="html")

        elif message.text == 'Назад в меню':
            await bot.send_message(message.from_user.id, "Главное меню...", reply_markup = nav.mainMenu)

        elif  message.text == 'Заполнить заново':
            db.set_signup(message.from_user.id, 'setname')
            await bot.send_message(message.from_user.id, "Напишите фамилию и имя")

        elif message.text == 'Выйти из меню админа' and db.get_signup(message.from_user.id) == 'admin_true':
            await bot.send_message(message.from_user.id, "Главное меню...", reply_markup=nav.mainMenu)

        elif message.text == 'Пост' and db.get_signup(message.from_user.id) == 'admin_true':
            await bot.send_message(message.from_user.id, "Выберите какой группе людей отправить пост...",
                                   reply_markup=nav.AdmPostMenu)

        elif (message.text == 'Медиакоммуникации в Москве_' or
              message.text == 'Журналистика_' or
              message.text == 'Всем_' or
              message.text == 'Всем в Москве_' or
              message.text == 'Абитуриенты этого года_' or
              message.text == 'Медиакоммуникации в Питере_') and \
                db.get_signup(message.from_user.id) == 'admin_true':
            group = message.text[:-1]
            db.set_programm(message.from_user.id, group)
            str = "Выбрано: " + group + "\n" + "Отправьте теперь сам пост..."
            db.set_adm_post(message.from_user.id, 1)
            await bot.send_message(message.from_user.id, str, reply_markup = nav.AdmPostProgBack)
            dp.register_message_handler(message_handler, content_types=types.ContentTypes.ANY)
        elif message.text == 'Назад к выбору факультета' and db.get_signup(message.from_user.id) == 'admin_true':
            await bot.send_message(message.from_user.id, "Выберите какой группе людей отправить пост...",
                                   reply_markup=nav.AdmPostMenu)

        else:
            if db.get_signup(message.from_user.id) == 'setname':
                if '@' in message.text or '/' in message.text:
                    await bot.send_message(message.from_user.id, "Вы ввели запрещённыый символ")
                else:
                    if message.text == 'admin_log': #ЛОГИН ДЛЯ АДМИНА
                        db.set_signup(message.from_user.id, 'admin')
                        await bot.send_message(message.from_user.id, "Введите пароль для админа")
                    else:
                        db.set_name(message.from_user.id, message.text)
                        db.set_signup(message.from_user.id, 'setphone')
                        await bot.send_message(message.from_user.id, "Укажите номер телефона в формате 89*********"
                                                                     " — это нужно, чтобы держать с вами оперативную"
                                                                     " связь во время вступительной кампании.",
                                               reply_markup = types.ReplyKeyboardRemove())

            elif db.get_signup(message.from_user.id) == 'setphone':
                if message.text[0] != '8':
                    await bot.send_message(message.from_user.id, 'Введите телефон, начиная с 8')
                elif not message.text.isnumeric():
                    await bot.send_message(message.from_user.id, 'Введите только цифры без пробелов и других символов')
                else:
                    if len(message.text) != 11:
                        await bot.send_message(message.from_user.id,
                                               'Кажется, телефон должен содержать ровно 11 цифр')
                    else:
                        db.set_phone(message.from_user.id, int(message.text))
                        db.set_signup(message.from_user.id, 'setmail')
                        await bot.send_message(message.from_user.id, 'Укажите почту. \nЕсли вы уже подписаны на'
                                                                     ' <a href="https://forms.sendpulse.com/8952ed9f6b/">'
                                                                     'дайджест Школы медиа</a>'
                                                                     ' НИУ ВШЭ на эту почту, мы не будем дублировать рассылки:'
                                                                     ' будем присылать все новости здесь.',parse_mode="HTML")

            elif db.get_signup(message.from_user.id) == 'setyear':
                if len(message.text) != 4 and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Что-то не так с годом')
                elif not message.text.isnumeric() and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Введите только цифры без пробелов и других символов')
                elif message.text < '2022' and message.text != 'Позже':
                    await bot.send_message(message.from_user.id, 'Что-то не так с годом. Кажется, вы не абитуриент')
                else:
                    if message.text != 'Позже':
                        db.set_year_p(message.from_user.id, int(message.text))
                    else:
                        db.set_year_p(message.from_user.id, 2024)
                    db.set_signup(message.from_user.id, 'setprogramm')
                    await bot.send_message(message.from_user.id, "На какую программу вы планируете поступать?",
                                               reply_markup = nav.ProgMenu)

            elif db.get_signup(message.from_user.id) == 'setprogramm':
                if not (message.text == "Медиакоммуникации в Москве" or
                        message.text == "Журналистика" or
                        message.text == "Медиакоммуникации в Питере" or
                        message.text == "Буду поступать на обе в Москве" or
                        message.text == "Буду поступать на все" ):
                    await bot.send_message(message.from_user.id, 'Выберите ответ из предложенного списка',
                                           reply_markup = nav.ProgMenu)
                else:
                    db.set_programm(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.from_user.id, "Поздравляю! Вы успешно зарегистрировались!"
                                                                 " Заодно советуем подписаться на наш "
                                                                 "телеграм-журнал про медиа, диджитал "
                                                                 "и студенческую жизнь Вышки: https://t.me/hsemedia",
                                           reply_markup=nav.mainMenu)
            elif db.get_signup(message.from_user.id) == 'setmail':
                if "@" in message.text:
                    db.set_mail(message.from_user.id, message.text)
                    db.set_signup(message.from_user.id, 'setyear')
                    await bot.send_message(message.from_user.id, "В каком году вы планируете поступать?",
                                           reply_markup = nav.YEAR_BTN)
                else:
                    await bot.send_message(message.from_user.id, 'Это что-то не похоже на электронную почту')


            elif db.get_signup(message.from_user.id) == 'admin':
                db.set_signup(message.from_user.id, 'done')
                if message.text == 'qwerty': #ПАРОЛЬ ДЛЯ АДМИНА
                    db.set_signup(message.from_user.id, 'admin_true')
                    db.set_adm_post(message.from_user.id, 0)
                    await bot.send_message(message.from_user.id, "Вы успешно вошли в меню админа!", reply_markup= nav.AdmMenu)
                else:
                    db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.from_user.id, "У вас нет доступа!!!")

            elif db.get_signup(message.from_user.id) == 'restart':
                if message.text == "Да":
                    db.kill_user(message.from_user.id)

                    await bot.send_message(message.chat.id, "Отправь /start\nЧтобы начать всё сначала.",
                                           reply_markup = nav.Start_)
                else:
                    if db.get_adm_post(message.from_user.id) == '0':
                        db.set_signup(message.from_user.id, 'admin_true')
                    else:
                        db.set_signup(message.from_user.id, 'done')
                    await bot.send_message(message.chat.id, "Главное меню...",
                                           reply_markup=nav.mainMenu)


            else:
                if db.get_adm_post(message.from_user.id) == '1': #СДЕЛАЙ В БД ФЛАГ НА ДАННОЕ ИСКЛЮЧЕНИЕ
                    msg = message
                    if db.get_programm(msg.from_user.id) == 'Всем':
                        db.set_adm_post(msg.from_user.id, 0)
                        db.set_programm(msg.from_user.id, "Буду поступать на все")
                        users_1 = db.get_user_id("Журналистка")
                        users_2 = db.get_user_id("Медиакоммуникации в Москве")
                        users_3 = db.get_user_id("Буду поступать на обе в Москве")
                        users_4 = db.get_user_id("Медиакоммуникации в Питере")
                        users_5 = db.get_user_id("Буду поступать на все")
                        await MessageBroadcaster(users_1, msg).run()
                        await MessageBroadcaster(users_2, msg).run()
                        await MessageBroadcaster(users_3, msg).run()
                        await MessageBroadcaster(users_4, msg).run()
                        await MessageBroadcaster(users_5, msg).run()
                    elif db.get_programm(msg.from_user.id) == 'Всем в Москве':
                        db.set_adm_post(msg.from_user.id, 0)
                        db.set_programm(msg.from_user.id, "Буду поступать на все")
                        users_1 = db.get_user_id("Журналистка")
                        users_2 = db.get_user_id("Буду поступать на обе в Москве")
                        users_3 = db.get_user_id("Медиакоммуникации в Москве")
                        users_4 = db.get_user_id("Буду поступать на все")
                        await MessageBroadcaster(users_1, msg).run()
                        await MessageBroadcaster(users_2, msg).run()
                        await MessageBroadcaster(users_3, msg).run()
                        await MessageBroadcaster(users_4, msg).run()
                    elif db.get_programm(msg.from_user.id) == 'Медиакоммуникации в Питере':
                        db.set_adm_post(msg.from_user.id, 0)
                        db.set_programm(msg.from_user.id, "Буду поступать на все")
                        db.set_programm(msg.from_user.id, "Медиакоммуникации в Питере")
                        users = db.get_user_id(db.get_programm(msg.from_user.id))
                        users_ = db.get_user_id("Буду поступать на все")
                        await MessageBroadcaster(users, msg).run()
                        await MessageBroadcaster(users_, msg).run()
                    elif db.get_programm(msg.from_user.id) == 'Абитуриенты этого года':
                        db.set_adm_post(msg.from_user.id, 0)
                        db.set_programm(msg.from_user.id, "Буду поступать на все")
                        users = db.get_user_id_year()
                        await MessageBroadcaster(users, msg).run()
                    else:
                        db.set_adm_post(msg.from_user.id, 0)
                        users = db.get_user_id(db.get_programm(msg.from_user.id))
                        users_ = db.get_user_id("Буду поступать на все")
                        users__ = db.get_user_id("Буду поступать на обе в Москве")
                        await MessageBroadcaster(users, msg).run()
                        await MessageBroadcaster(users_, msg).run()
                        await MessageBroadcaster(users__, msg).run()
                else:
                    await bot.send_message(message.from_user.id, "Вы ввели что-то не то(\n"
                                                                 "Напишите /help, чтобы узнать о доступных командах")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)