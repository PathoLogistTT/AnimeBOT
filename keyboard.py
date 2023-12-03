from aiogram import types

async def start(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Скинуть картинку"),
                types.KeyboardButton(text="Скинуть видео")
            ],
            [
                types.KeyboardButton(text="Скинуть музыку"),
                types.KeyboardButton(text="Мемы")
            ],
        ],
        resize_keyboard=True,
    ))

async def send_memes(message: types.Message):
    await message.reply("Выберите категорию мемов:",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Аниме мемы")],
                [types.KeyboardButton(text="Гачи мемы")],
                [types.KeyboardButton(text="Вернуться в главное меню")],
            ],
            resize_keyboard=True,
        )
    )

async def return_to_start(message: types.Message):
    await start(message)