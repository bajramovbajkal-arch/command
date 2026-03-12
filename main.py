import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_1 = KeyboardButton(text="baylanis")
button_2 = KeyboardButton(text="Xizmetler")

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [button_1, button_2],

    ],
    resize_keyboard=True,
)

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")

bot= Bot(token=TOKEN)
dp= Dispatcher()


async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
