from aiogram import types

async def start(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Скинуть картинку")],
            [types.KeyboardButton(text="Скинуть видео")],
            [types.KeyboardButton(text="Скинуть музыку")],
        ],
        resize_keyboard=True,
    ))