from aiogram import types, Dispatcher
from bot_data import bot, db, shop_name, any_data, admin_chat, feedback_link, qiwi, card, bitcoin, admin_id, vxod_worker
import markups as nav
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
import bot_data

class get_people_id(StatesGroup):
    ban_id = State()
    unban_id = State()


class send_text(StatesGroup):
    text = State()
    photo = State()
    confirm = State()


async def main_command(message: types.Message):
    if db.get_client_data(message.from_user.id)[2] != "ban":
        if message.text == "💰 Пополнить баланс":
            await bot.send_message(message.from_user.id, "Для пополнения счета вам необходимо выбрать платежную систему:", reply_markup=nav.deposit_menu)

        if message.text == "Qiwi":
            await bot.send_message(message.from_user.id, f"Для пополнения баланса с помощью <b>QIWI</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>QIWI кошелек:</b> {qiwi}\n<b>Комментарий:</b> {message.from_user.id}\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>ВНИМАНИЕ: Деньги отправленные без комментария к платежу не зачисляются. Вернуть данные средства будет невозможно!</b>\n\nСразу после оплаты деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе 'Профиль'\n Спасибо что вы с нами!", parse_mode=types.ParseMode.HTML, reply_markup=nav.check_deposit)
        if message.text == "Банк. Картой":
            await bot.send_message(message.from_user.id, f"Для пополнения баланса с помощью <b>Банковской карты</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Номер счета:</b> {card}\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nСразу после оплаты деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе 'Профиль'\nСпасибо что вы с нами!", parse_mode=types.ParseMode.HTML, reply_markup=nav.check_deposit)
        if message.text == "Bitcoin":
            await bot.send_message(message.from_user.id, f"Для пополнения баланса с помощью <b>Bitcoin</b> вам необходимо перевести необходимую сумму по указанным ниже реквизитам:\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n<b>Bitcoin кошелек:</b> {bitcoin}\n<b>Сумма:</b> Любая необходимая\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>ВНИМАНИЕ: Баланс будет пополнен после получения 2 подтверждений от сети blockchain.</b>\n\nСразу после получения подтверждений деньги будут зачислены на ваш личный счет в магазине. Проверить баланс вы можете в разделе 'Профиль'\n Спасибо что вы с нами!", parse_mode=types.ParseMode.HTML, reply_markup=nav.check_deposit)

        if message.text == "✅ Оплатил":
            await bot.send_message(message.from_user.id, "Платеж не найден, попробуйте через 5 минут", reply_markup=nav.check_deposit)

        if message.text == "Отменить":
            await bot.send_message(message.from_user.id, text=f"✌️ Добро пожаловать в автоматический магазин <b> {shop_name} </b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВ нашем шопе ты можешь преобрести лучший товар по самым сладким ценам.\n\nОт успешного соврешения заказа тебя отделяет лишь несколько шагов.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n<b>Для начала выбери интересующий тебя пункт меню:</b>", parse_mode=types.ParseMode.HTML, reply_markup=nav.main_menu)
        if message.text == "🛒 Заказать":
            await bot.send_message(message.from_user.id, text="Выберите ваш город 👇", reply_markup=nav.city)
        if message.text == "✅ Отзывы":
            await bot.send_message(message.from_user.id, f"<b>Отзывы {shop_name}</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nВсе отзывы публикуются выборочно на нашем официальном канале. Хочешь попасть в их число? Соверши покупку в нашем магазине, попробуй товар и напиши самый ахуенный отзыв, на какой ты только способен!\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nНаш канал с отзывами: <a href='{feedback_link}'>Тебе сюда</a>", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button, disable_web_page_preview=True)
        if message.text == "🎛 Support":
            await bot.send_message(message.from_user.id, f"<b>Служба Поддержки {shop_name}</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nПример обращения в службу поддержки:\n\n1. Номер заказа\n\n2. Время приезда на местность\n\n3. Описание проблемы\n\n4. Фотографии места (2-4шт)\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nКонтакт службы поддержки: <a href='https://t.me/{admin_chat}'>@{admin_chat}</a>", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button, disable_web_page_preview=True)
        if message.text == "🖥 Работа":
            await bot.send_message(message.from_user.id, f"<b>Работа в {shop_name}</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\nНаш магазин ведет постоянный набор по всей РФ.\n\nОткрыты вакансии на следующие должности:\n\n    1. Кладмен (от 400 руб/клад)\n    2. Трафаретчик (от 80 руб/рисунок)\n    3. Перевозчик (только с залогом)\n    4. Склад (только с залогом)\n\nТак же приглашаем к сотрудничеству химиков и гроверов с качественным товаром. Достойную оплату гарантируем. Найдете магазин в который продадите дороже - мы перебьем цену. \n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nДля связи писать: <a href='https://t.me/{admin_chat}'>@{admin_chat}</a> с пометкой 'Работа'", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button, disable_web_page_preview=True)
        if message.text == "📃 История":
            await bot.send_message(message.from_user.id, "Ваша история покупок пуста. Самое время совершить первую.", reply_markup=nav.cancle_button)
        if message.text == "🧾 Правила":
            await bot.send_message(message.from_user.id, f"<b>Правила магазина {shop_name}</b>\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n1.Магазин несет ответственность за качество продаваемого товара. Если качество вас не устроило - ждем вашего сообщения в службу поддержки (Support), решим эту проблему в самые кратчайшие сроки.\n\n2.Магазин оставляет за собой право на отказ в обслуживании любого пользователя без объяснения причин. Деньги, в данном случае, возвращаются через службу поддержки на тот кошелек, с которого производилась оплата.\n\n3.Гарантия на товар 6 часов с момента покупки. Обращения, отправленные позже установленного правилами срока - не рассматриваются.\n\n4.Пополнение баланса с помощью платежной системы QIWI с неправильным комментарием или отсутствием его - бонус магазина, но если ваш рейтинг выше 70% всегда можно договориться.\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nСовершая покупки в нашем магазине вы автоматически соглашаетесь с данными правилами.", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button)
        if message.text == "💾 Профиль":
            await bot.send_message(message.from_user.id, f"<b>Ваш профиль</b>\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n👤Ваш Юзер: @{message.from_user.username}\n🆔Ваш ID: {message.from_user.id}\n🛍Количество покупок: 0\n💰Ваш баланс: {db.get_client_data(message.from_user.id)[1]} RUB\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💸Персональная скидка: 0%\n🏇До сл.скидки осталось: 3 покупки\n📊Рейтинг: 0% (Новичёк)", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button)
        if message.text in any_data["city"]:
            await bot.send_message(message.from_user.id, "Выберите желаемый район 👇", reply_markup=nav.generate_keyboard_zone(message.text))
        if message.text in any_data["zone"]:
            await bot.send_message(message.from_user.id, "Выберите желаемый товар 👇", reply_markup=nav.generate_keyboard_product(message.text))
        if message.text in any_data["product_price"]:
            await bot.send_message(message.from_user.id, "Выберите желаемый фасовку 👇", reply_markup=nav.generate_keyboard_price(message.text))
        if message.text in any_data["price"]:
            if int(message.text[message.text.find("(") + 1:][:-5]) <= db.get_client_data(message.from_user.id)[1]:
                pass  # Если у вас реально будет пополнение, то сюда вставите остаток кода
            else:
                await bot.send_message(message.from_user.id, f"Для покупки данной позиции вам необходимо пополнить счет на <b>{message.text[message.text.find('(') + 1:][:-5]}</b> рублей.\n\nДля пополнения нажмите кнопку <b>'Пополнить счет'</b> в главном меню", parse_mode=types.ParseMode.HTML, reply_markup=nav.cancle_button)

        if message.text == "Начать рассылку" and message.from_user.id in admin_id:
            await bot.send_message(message.from_user.id, "Введите текст для рассылки\n<b>Если потребуется выйти введите 'n'</b>", parse_mode=types.ParseMode.HTML)
            await send_text.text.set()

        if message.text == "Да" and message.from_user.id in admin_id:
            await bot.send_message(message.from_user.id, "Окей, отправь мне фото")
            await send_text.photo.set()
        if message.text == "Нет" and message.from_user.id in admin_id:
            await bot.send_message(message.from_user.id, f"Ладно, как хочешь\nПравильно ли ты ввел текст\n\n<b>{db.get_data_of_send_message()[0]}</b>\n\nЕсли все правильно, подтвердите рассылку!", reply_markup=nav.confirm_menu, parse_mode=types.ParseMode.HTML)
        if message.text == "Подтвердить рассылку" and message.from_user.id in admin_id:
            await get_confirm(message)
        if message.text == "Да ну её нах" and message.from_user.id in admin_id:
            db.delete_data_of_send_message()
            await bot.send_message(message.from_user.id, "Понял, завершаю работу", reply_markup=nav.admin_menu)

        if message.text == "Подсчет мамонтов" and message.from_user.id in admin_id:
            await bot.send_message(message.from_user.id, f"В системе {len(db.get_all_client())} мамонтов", reply_markup=nav.admin_menu)
        if message.text == "Забанить пользователя" and message.from_user.id in admin_id:
            await bot.send_message(message.from_user.id, "Введите id пользователя\n<b>Если потребуется выйти введите 'n'</b>", parse_mode=types.ParseMode.HTML)
            await get_people_id.ban_id.set()
        if message.text == "Разбанить пользователя":
            await bot.send_message(message.from_user.id, "Введите id пользователя\n<b>Если потребуется выйти введите 'n'</b>", parse_mode=types.ParseMode.HTML)
            await get_people_id.unban_id.set()

    else:
        await bot.send_message(message.from_user.id, f"Ваша учетная запись была заблокирована. Все денежные средства на вашем счете были заморожены.\n\n"
                                                     f"Если вы считаете, что это ошибка и вы не нарушали ни одного правила.\n\nСвяжитесь с админом @<a href='https://t.me/{admin_chat}'>@{admin_chat}</a>", parse_mode=types.ParseMode.HTML)


async def get_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["text"] = message.text
    if message.text != "n":
        db.add_data_of_send_message(text=data["text"])
        await bot.send_message(message.from_user.id, "Хотите ли добавить к рассылке фото", reply_markup=nav.photo_menu)
        await state.finish()
    else:
        await bot.send_message(message.from_user.id, "Понял, выхожу", reply_markup=nav.admin_menu)
        await state.finish()

async def invitevorker(message: types.Message, state: FSMContext):
    if message.text == '/воркер':
        await message.answer(
            f'Привет воркер!\n\nЕсли пропишешь /start то меню пропадет, нужно будет прописать еще раз /воркер', reply_markup=nav.work_menu
        )

async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id
    db.update_data_of_send_message(text=db.get_data_of_send_message()[0], photo_id=data["photo"])
    await bot.send_photo(message.from_user.id, photo=db.get_data_of_send_message()[1], caption=db.get_data_of_send_message()[0])
    await bot.send_message(message.from_user.id, "Если все правильно подтвердите рассылку!", reply_markup=nav.confirm_menu)
    await state.finish()


async def get_confirm(message: types.Message):
    await bot.send_message(message.from_user.id, "Рассылка началась")
    if db.get_data_of_send_message()[1] is not None:
        for i in db.get_all_client_without_ban():
            try:
                await bot.send_photo(i[0], photo=db.get_data_of_send_message()[1], caption=db.get_data_of_send_message()[0])
            except: pass
    else:
        for i in db.get_all_client_without_ban():
            try:
                await bot.send_message(i[0], db.get_data_of_send_message()[0])
            except: pass
    await bot.send_message(message.from_user.id, "Рассылка закончилась", reply_markup=nav.admin_menu)
    db.delete_data_of_send_message()


async def ban_client_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["ban_id"] = message.text
    if data["ban_id"] != "n":
        if data["ban_id"].isdigit():
            if db.client_exist(data["ban_id"]):
                try:
                    db.ban_client(data["ban_id"])
                    await bot.send_message(message.from_user.id, f"Пользователь {data['ban_id']} был успешно забанин", reply_markup=nav.admin_menu)
                    await state.finish()
                except: await bot.send_message(message.from_user.id, "Что-то пошло не так")
            else: await bot.send_message(message.from_user.id, "Такого пользователя нету\n Попробуйте ввести другого")
        else: await bot.send_message(message.from_user.id, "Id должен состоять из цифр\nПопробуй ввести другой id")
    else:
        await bot.send_message(message.from_user.id, "Понял, выхожу", reply_markup=nav.admin_menu)
        await state.finish()


async def unban_client_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["unban_id"] = message.text
    if data["unban_id"] != "n":
        if data["unban_id"].isdigit():
            if db.client_exist(data["unban_id"]):
                try:
                    db.unban_client(data["unban_id"])
                    await bot.send_message(message.from_user.id, f"Пользователь {data['unban_id']} был успешно разбанин",
                                           reply_markup=nav.admin_menu)
                    await state.finish()
                except: await bot.send_message(message.from_user.id, "Что-то пошло не так")
            else:
                await bot.send_message(message.from_user.id, "Такого пользователя нету\n Попробуйте ввести другого")
        else: await bot.send_message(message.from_user.id, "Id должен состоять из цифр\nПопробуй ввести другой id")
    else:
        await bot.send_message(message.from_user.id, "Понял, выхожу", reply_markup=nav.admin_menu)
        await state.finish()


async def admin_start(message: types.Message):
    await bot.send_message(message.from_user.id, "Добро пожаловать в admin панель. Что вы хотите сделать?", reply_markup=nav.admin_menu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(admin_start, user_id=admin_id, commands=["admin"])
    dp.register_message_handler(main_command, content_types=["text"])
    dp.register_message_handler(ban_client_id, user_id=admin_id, state=get_people_id.ban_id)
    dp.register_message_handler(unban_client_id, user_id=admin_id, state=get_people_id.unban_id)
    dp.register_message_handler(get_message, user_id=admin_id, state=send_text.text)
    dp.register_message_handler(get_photo, user_id=admin_id, state=send_text.photo, content_types=types.ContentTypes.PHOTO)
    dp.register_message_handler(get_confirm, user_id=admin_id, state=send_text.confirm)