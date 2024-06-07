from aiogram import types, Dispatcher
from bot_data import bot, db, verification, shop_name, admin_chat
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from PIL import Image, ImageDraw, ImageFont
import markups as nav
import random
import string

W, H = (1920, 1080)


class get_word(StatesGroup):
    word = State()


def generate_word():
    place = Image.new("RGB", (1920, 1080), "white")
    font = ImageFont.truetype("font.ttf", size=300)
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(8))
    imgdraw = ImageDraw.Draw(place)
    w, h = font.getsize(rand_string)
    imgdraw.text(((W-w)/2, (H-h)/2), rand_string, font=font, fill="black")
    place.save("verification_img.jpg")
    return rand_string


async def command_start(message: types.Message):
    if message.from_user.username is not None:
        if not db.client_exist(message.from_user.id):
            if verification:
                text = generate_word()
                db.add_verification_user(message.from_user.id, text)
                photo = open("verification_img.jpg", "rb")
                await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption="🇷🇺 RUS:\n\nВведите капчу:\n\n<i>Если вы введете 3 раза неправильно капчу, то будете заблокированы на 1 час!</i>\n\n🇺🇸 ENG:\n\nEnter a captcha:\n\nIf you enter the wrong captcha 3 times, you will be blocked for 1 hour!", parse_mode='HTML')
                photo.close()
                await get_word.word.set()
            else:
                db.add_client(message.from_user.id)
                await bot.send_message(message.from_user.id,
                                       f"✌️ Добро пожаловать в автоматический магазин <b> {shop_name} </b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВ нашем шопе ты можешь преобрести лучший товар по самым сладким ценам.\n\nОт успешного соврешения заказа тебя отделяет лишь несколько шагов.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>Для начала выбери интересующий тебя пункт меню:</b>",
                                       parse_mode=types.ParseMode.HTML, reply_markup=nav.main_menu)
        elif db.get_client_data(message.from_user.id)[2] != "ban" and db.client_exist(message.from_user.id):
            await bot.send_message(message.from_user.id, f"✌️ Добро пожаловать в автоматический магазин <b> {shop_name} </b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВ нашем шопе ты можешь преобрести лучший товар по самым сладким ценам.\n\nОт успешного соврешения заказа тебя отделяет лишь несколько шагов.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>Для начала выбери интересующий тебя пункт меню:</b>", parse_mode=types.ParseMode.HTML, reply_markup=nav.main_menu)
        elif db.get_client_data(message.from_user.id)[2] == "ban" and db.client_exist(message.from_user.id):
            await bot.send_message(message.from_user.id,
                                   f"Ваша учетная запись была заблокирована. Все денежные средства на вашем счете были заморожены.\n\n"
                                   f"Если вы считаете, что это ошибка и вы не нарушали ни одного правила.\n\nСвяжитесь с админом <a href='https://t.me/{admin_chat}'>@{admin_chat}</a>",
                                   parse_mode=types.ParseMode.HTML)

    else:
        await bot.send_message(message.from_user.id, "У вас не установлен <b>username</b>\n\nУстановите его, потом введите /start", parse_mode=types.ParseMode.HTML)


async def get_answer(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["word"] = message.text
    if data["word"] == db.get_verification_data(message.from_user.id)[1]:
        await bot.send_message(message.from_user.id, f"✌️ Добро пожаловать в автоматический магазин <b> {shop_name} </b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВ нашем шопе ты можешь преобрести лучший товар по самым сладким ценам.\n\nОт успешного соврешения заказа тебя отделяет лишь несколько шагов.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>Для начала выбери интересующий тебя пункт меню:</b>", parse_mode=types.ParseMode.HTML, reply_markup=nav.main_menu)
        db.delete_verification_data(message.from_user.id)
        db.add_client(message.from_user.id)
        await state.finish()
    else: await bot.send_message(message.from_user.id, "Неправильно")


def register_handlers_verification(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"])
    dp.register_message_handler(get_answer, state=get_word.word)