import asyncio
import logging
import Config
from aiogram import Bot, Dispatcher
from keyboard import start, send_memes, return_to_start
from choise_content import send_picture, send_video, send_music, send_anime_mem, send_gachi_mem

logger = logging.getLogger()
async def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(asctime)s - %(message)s')
    BOT_TOKEN = Config.BOT_TOKEN
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(send_picture, lambda message: "Скинуть картинку" in message.text)
    dp.register_message_handler(send_video, lambda message: "Скинуть видео" in message.text)
    dp.register_message_handler(send_music, lambda message: "Скинуть музыку" in message.text)
    dp.register_message_handler(send_memes, lambda message: "Мемы" in message.text)
    dp.register_message_handler(send_anime_mem, lambda message: "Аниме мемы" in message.text)
    dp.register_message_handler(send_gachi_mem, lambda message: "Гачи мемы" in message.text)
    dp.register_message_handler(return_to_start, lambda message: message.text == "Вернуться в главное меню")
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())