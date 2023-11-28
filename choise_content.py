import random
import os
from aiogram import types
from message import get_random_reply
import logging

logger = logging.getLogger('actions_logger')

async def send_picture(message: types.Message):
    reply = await get_random_reply()
    await message.reply(reply)
    picture = random.choice(os.listdir("C:/Users/Даниил/Desktop/picture"))
    with open(f"C:/Users/Даниил/Desktop/picture/{picture}", 'rb') as photo:
        await message.reply_photo(photo)
    username = message.from_user.username
    logger.info(f"@{username} отправлена картинка: {picture}")

async def send_video(message: types.Message):
    reply = await get_random_reply()
    await message.reply(reply)
    video = random.choice(os.listdir("C:/Users/Даниил/Desktop/video"))
    with open(f"C:/Users/Даниил/Desktop/video/{video}", 'rb') as video_file:
        await message.reply_video(video_file)
    username = message.from_user.username
    logger.info(f"@{username} отправлено видео: {video}")

async def send_music(message: types.Message):
    reply = await get_random_reply()
    await message.reply(reply)
    music = random.choice(os.listdir("C:/Users/Даниил/Desktop/music"))
    with open(f"C:/Users/Даниил/Desktop/music/{music}", 'rb') as music_file:
        await message.reply_audio(music_file)
    username = message.from_user.username
    logger.info(f"@{username} отправлена музыка: {music}")