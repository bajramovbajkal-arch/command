import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message,InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery
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

#adilbek
@dp.message(Command('alo'))
async def g(a:Message):
    await a.answer('dnx')

@dp.message(Command('jardem'))
async def g(a:Message):
    await a.answer('ne jardem kerek')


inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📞 Command 1", callback_data="com_1"),
        InlineKeyboardButton(text="📢 Command 2", callback_data="com_2")],

        [InlineKeyboardButton(text="📞 Command 3", callback_data="com_3"),
        InlineKeyboardButton(text="📢 Command 4", callback_data="com_4")],

        [InlineKeyboardButton(text="📞 Command 5", callback_data="com_5")]
    ]
)

@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "📋 Kerakli bo‘limni tanlang:",
        reply_markup=inline_kb
    )


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    data = callback.data

    if data == "com_1":
        await callback.message.answer("Salom")

    elif data == "com_2":
        await callback.message.answer("help")

    elif data == "com_3":
        await callback.message.answer("About")

    elif data == "com_4":
        await callback.message.answer(
            "Reset"
        )

    elif data == "com_5":
        await callback.message.answer(
            "Future"
        )

    await callback.answer()

async def main():
    print('bot ishladi')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
