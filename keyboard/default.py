from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    button = KeyboardButton(text="🏢 Kompaniya haqida")
    button2 = KeyboardButton(text="📍 Fililallar")
    button3 = KeyboardButton(text="💼 Bo'sh ish o'rinlari")
    button4 = KeyboardButton(text="Menyu")
    button5 = KeyboardButton(text="🗣 Yangiliklar")
    button6 = KeyboardButton(text="📞 Kontaktlar/Manzil")
    button7 = KeyboardButton(text="🇺🇿/🇷🇺 Til")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5],
            [button6, button7],
        ],
        resize_keyboard=True
    )
    return rkm


def back_menu():
    button = KeyboardButton(text="Back")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button]
        ],
        resize_keyboard=True
    )
    return rkm





#ru
def main_menu_ru():
    button = KeyboardButton(text="🏢 О компании")
    button2 = KeyboardButton(text="📍 Филиалы")
    button3 = KeyboardButton(text="💼 Вакансии")
    button4 = KeyboardButton(text="📱 Меню")
    button5 = KeyboardButton(text="🗣 Новости")
    button6 = KeyboardButton(text="📞 Контакты/Адрес")
    button7 = KeyboardButton(text="🇺🇿/🇷🇺 Язык")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3],
            [button4, button5],
            [button6, button7],
        ],
        resize_keyboard=True
    )
    return rkm


# langunage changes uz
def languange_uz():
    button = KeyboardButton(text="🇷🇺 Русский")
    button2 = KeyboardButton(text="🇺🇿 O'zbekcha")
    button3 = KeyboardButton(text="⬅️ Ortga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm


# languange changes ru
def languange_ru():
    button = KeyboardButton(text="🇷🇺 Русский")
    button2 = KeyboardButton(text="🇺🇿 O'zbekcha")
    button3 = KeyboardButton(text="🔙 Назад")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3]
        ],
        resize_keyboard=True
    )
    return rkm




#filial ru
def filial_ru():
    button = KeyboardButton(text="☕️ Показать ближайший филиал")
    button2 = KeyboardButton(text="🏢 Головной офис")
    button3 = KeyboardButton(text="г. Ташкент")
    button4 = KeyboardButton(text="🔙 Назад")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
            [button4]
        ],
        resize_keyboard=True
    )
    return rkm


# yaqin fillial ru
def yaqin_filial_ru():
    button = KeyboardButton(text="📍Отправить геолокацию", request_location=True)
    button2 = KeyboardButton(text="🔙 Назад")



    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2]
        ],
        resize_keyboard=True
    )
    return rkm



# Tashkent filal ru

def tosheknt_filial_ru():
    button_samarkand = KeyboardButton(text="📍 Самарканд Дарвоза")
    button_alay = KeyboardButton(text="📍 Алайский базар")
    button_malika = KeyboardButton(text="📍 Малика")
    button_yahyo = KeyboardButton(text="📍 Яхьё Гулямова, 94")
    button2 = KeyboardButton(text="🔙 Назад")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button_samarkand, button_alay],
            [button_malika, button_yahyo],
            [button2],
        ],
        resize_keyboard=True
    )
    return rkm


#bosh ish orinlari
def bosh_ish_orinlari_uz():
    button1= KeyboardButton(text="Toshkent")
    button2 = KeyboardButton(text="Andijon")
    button3 = KeyboardButton(text="Qarshi")
    button4 = KeyboardButton(text="Qo'qon")
    button5 = KeyboardButton(text="Namangan")
    button6 = KeyboardButton(text="Toshkent viloyati")
    button7 = KeyboardButton(text="Nukus")
    button8 = KeyboardButton(text="Samarqand")
    button9 = KeyboardButton(text="Farg'ona")
    button10 = KeyboardButton(text="Shahrisabz")
    button11 = KeyboardButton(text="Xorazm viloyati")
    button12 = KeyboardButton(text="Urgench")
    button13 = KeyboardButton(text="⬅️ Ortga")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button1, button2],
            [button3, button4],
            [button5, button6],
            [button7, button8],
            [button9, button10],
            [button11, button12],
            [button13],
        ],
        resize_keyboard=True
    )
    return rkm

def toshkent_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Call-markaz operatori")
    button3 = KeyboardButton(text="Kuryer")
    button4 = KeyboardButton(text="❌ Bekor qilish ❌")
    button5 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
            [button4, button5]
        ],
        resize_keyboard=True
    )
    return rkm

def andijon_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def qarshi_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm



def qoqon_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm


def namangan_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def toshkent_viloyati_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def nukus_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm


def samarqand_viloyati_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def fergana_viloyati_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def shahrisabz_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm



def xorazm_viloyati_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="Kuryer")
    button3 = KeyboardButton(text="❌ Bekor qilish ❌")
    button4 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm


def navoiy_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm


def urgench_menu():
    button = KeyboardButton(text="Universal xodim")
    button2 = KeyboardButton(text="❌ Bekor qilish ❌")
    button3 = KeyboardButton(text="Ortga ↩️")


    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm





# Главные вакансии
def glavnye_vakansii_ru():
    button1 = KeyboardButton(text="Ташкент")
    button2 = KeyboardButton(text="Андижан")
    button3 = KeyboardButton(text="Карши")
    button4 = KeyboardButton(text="Коканд")
    button5 = KeyboardButton(text="Наманган")
    button6 = KeyboardButton(text="Ташкентская область")
    button7 = KeyboardButton(text="Нукус")
    button8 = KeyboardButton(text="Самарканд")
    button9 = KeyboardButton(text="Фергана")
    button10 = KeyboardButton(text="Шахрисабз")
    button11 = KeyboardButton(text="Хорезмская область")
    button12 = KeyboardButton(text="Ургенч")
    button13 = KeyboardButton(text="⬅️ Назад")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button1, button2],
            [button3, button4],
            [button5, button6],
            [button7, button8],
            [button9, button10],
            [button11, button12],
            [button13],
        ],
        resize_keyboard=True
    )
    return rkm

def tashkent_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Оператор колл-центра")
    button3 = KeyboardButton(text="Курьер")
    button4 = KeyboardButton(text="❌ Отмена ❌")
    button5 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
            [button4, button5]
        ],
        resize_keyboard=True
    )
    return rkm

def andijan_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def karshi_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm

def kokand_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm

def namangan_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def tashkent_viloyat_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def nukus_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm

def samarkand_viloyat_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def fergana_viloyat_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def shahrisabz_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm

def horazm_viloyat_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="Курьер")
    button3 = KeyboardButton(text="❌ Отмена ❌")
    button4 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
            [button3, button4],
        ],
        resize_keyboard=True
    )
    return rkm

def navoiy_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm

def urgench_menu_ru():
    button = KeyboardButton(text="Универсальный сотрудник")
    button2 = KeyboardButton(text="❌ Отмена ❌")
    button3 = KeyboardButton(text="Назад ↩️")

    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
            [button2, button3],
        ],
        resize_keyboard=True
    )
    return rkm
