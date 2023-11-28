import os
import random
import asyncio
import logging
import Config
from aiogram import Bot, Dispatcher, types

async def start(message: types.Message):
    await message.reply("Выберите опцию:", reply_markup=types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Скинуть картинку")],
            [types.KeyboardButton(text="Скинуть видео")],
            [types.KeyboardButton(text="Скинуть музыку")],
        ],
        resize_keyboard=True,
    ))

async def send_picture(message: types.Message):
    picture = random.choice(os.listdir("C:/Users/Даниил/Desktop/picture"))
    with open(f"C:/Users/Даниил/Desktop/picture/{picture}", 'rb') as photo:
        await message.reply_photo(photo)

async def send_video(message: types.Message):
    video = random.choice(os.listdir("C:/Users/Даниил/Desktop/video"))
    with open(f"C:/Users/Даниил/Desktop/video/{video}", 'rb') as video_file:
        await message.reply_video(video_file)

async def send_music(message: types.Message):
    music = random.choice(os.listdir("C:/Users/Даниил/Desktop/music"))
    with open(f"C:/Users/Даниил/Desktop/music/{music}", 'rb') as music_file:
        await message.reply_audio(music_file)

async def main():
    logging.basicConfig(level=logging.DEBUG)
    BOT_TOKEN = Config.BOT_TOKEN
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(send_picture, lambda message: "Скинуть картинку" in message.text)
    dp.register_message_handler(send_video, lambda message: "Скинуть видео" in message.text)
    dp.register_message_handler(send_music, lambda message: "Скинуть музыку" in message.text)
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())