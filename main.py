import asyncio
import logging
import Config

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types

dp = Dispatcher()

@dp.message()
async def message(message: types.Message):
    await message.answer(text=message.text)
async def main():
    logging.basicConfig(level=logging.DEBUG)
    anime_bot = Bot(token=Config.BOT_TOKEN)
    await dp.start_polling(anime_bot)

if __name__ == "__main__":
    asyncio.run(main())