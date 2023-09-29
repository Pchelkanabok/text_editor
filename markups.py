from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



btnProfile = KeyboardButton ('Профиль')
btnurl = KeyboardButton ('Полезные ссылки')
btPod = KeyboardButton ('Задать вопрос')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnurl, btPod)


btnMedia = KeyboardButton("Медиакоммуникации в Москве")
btnJur = KeyboardButton("Журналистика")
btnMedia_Jur = KeyboardButton("Буду поступать на обе в Москве")
btnMediaSpb = KeyboardButton("Медиакоммуникации в Питере")
btnAll = KeyboardButton("Буду поступать на все")

ProgMenu = ReplyKeyboardMarkup(resize_keyboard = True)
ProgMenu.add(btnMedia, btnJur, btnMedia_Jur, btnMediaSpb,btnAll)


btnNext = KeyboardButton("Продолжить")

Next = ReplyKeyboardMarkup(resize_keyboard = True)
Next.add(btnNext)


btnProfLast = KeyboardButton("Назад в меню")
btnProNew = KeyboardButton("Заполнить заново")

Prof = ReplyKeyboardMarkup(resize_keyboard = True)
Prof.add(btnProfLast, btnProNew)


btnPost = KeyboardButton("Пост")
btnExAdm = KeyboardButton("Выйти из меню админа")

AdmMenu = ReplyKeyboardMarkup(resize_keyboard = True)
AdmMenu.add(btnPost, btnExAdm)


btnMedia_Adm = KeyboardButton("Медиакоммуникации в Москве_")
btnJur_Adm = KeyboardButton("Журналистика_")
btnMedia_Jur_Adm = KeyboardButton("Всем_")
btnMedia_allMsk = KeyboardButton("Всем в Москве_")
btnMedia_Spb = KeyboardButton("Медиакоммуникации в Питере_")
btnNowYear_Adm = KeyboardButton("Абитуриенты этого года_")

AdmPostMenu = ReplyKeyboardMarkup(resize_keyboard = True)
AdmPostMenu.add(btnMedia_Adm, btnJur_Adm, btnMedia_Jur_Adm, btnMedia_allMsk, btnMedia_Spb, btnNowYear_Adm)


btnAdmPostProgBack = KeyboardButton("Назад к выбору факультета")

AdmPostProgBack = ReplyKeyboardMarkup(resize_keyboard = True)
AdmPostProgBack.add(btnAdmPostProgBack)


btnYEAR_2022 = KeyboardButton("2022")
btnYEAR_2023 = KeyboardButton("2023")
btnYEAR_P = KeyboardButton("Позже")

YEAR_BTN = ReplyKeyboardMarkup(resize_keyboard = True)
YEAR_BTN.add(btnYEAR_2022, btnYEAR_2023, btnYEAR_P)


btnRestYe = KeyboardButton("Да")
btnResrNo = KeyboardButton("Нет")

RestYN = ReplyKeyboardMarkup(resize_keyboard = True)
RestYN.add(btnRestYe, btnResrNo)


btnStart = KeyboardButton('/start')

Start_ = ReplyKeyboardMarkup(resize_keyboard = True)
Start_.add(btnStart)