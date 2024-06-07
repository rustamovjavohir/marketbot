from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from bot_data import any_data

cb = CallbackData("fabnum", "action")

# _______________________Главное Меню_______________________________
main_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
main_menu.row(KeyboardButton("🛒 Заказать"), KeyboardButton("💾 Профиль"))
main_menu.row(KeyboardButton("📃 История"), KeyboardButton("🧾 Правила"))
main_menu.row(KeyboardButton("🎛 Support"), KeyboardButton("🖥 Работа"))
main_menu.row(KeyboardButton("💰 Пополнить баланс"), KeyboardButton("✅ Отзывы"))
# _______________________Способы оплаты_____________________________
deposit_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
deposit_menu.add("Qiwi").row("Банк. Картой", "Bitcoin").add("Отменить")

check_deposit = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add("✅ Оплатил").add("Отменить")
# _______________________Города_____________________________________
city = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
city.row("Москва", "С. Петербург")
city.row("Казань", "Екатеринбург")
city.row("Сочи", "Краснодар")
city.add("Отменить")
# ___________________________________________________________________
cancle_button = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add("Отменить")


# _____________________Создаем клавиатура под районы_________________
def generate_keyboard_zone(zone_name):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in any_data["city_zone"][zone_name]:
        keyboard.add(i)
    keyboard.add("Отменить")
    return keyboard
# ___________________________________________________________________


#_____________________ХУЙ____________________________________________
work_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
work_menu.row(KeyboardButton("🛒 Заказать"), KeyboardButton("💾 Профиль"))
work_menu.row(KeyboardButton("📃 История"), KeyboardButton("🧾 Правила"))
work_menu.row(KeyboardButton("🎛 Support"), KeyboardButton("🖥 Работа"))
work_menu.row(KeyboardButton("💰 Пополнить баланс"), KeyboardButton("✅ Отзывы"))
work_menu.row(KeyboardButton("⚡️ Меню воркера ⚡️"))
#_____________________________________________________________________



# _____________________Создаем клавиатура под товары_________________
def generate_keyboard_product(zone_name):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in any_data["product"][any_data["zone"][zone_name]]:
        keyboard.add(i)
    keyboard.add("Отменить")
    return keyboard


# _____________________Создаем клавиатура под цены_________________
def generate_keyboard_price(product_name):
    keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for i in any_data["product_price"][product_name]:
        keyboard.add(i)
    keyboard.add("Отменить")
    return keyboard
# ___________________________________________________________________
# _______________________Админ клавиатуры____________________________
admin_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row("Подсчет мамонтов", "Начать рассылку").row("Забанить пользователя", "Разбанить пользователя")
confirm_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row("Подтвердить рассылку", "Да ну её нах")
photo_menu = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).row("Да", "Нет")
# ___________________________________________________________________