from aiogram import executor
from handlers import client, all_users
from bot_data import dp


async def on_startup(_):
    print("Bot Started")


all_users.register_handlers_verification(dp)
client.register_handlers_client(dp)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)