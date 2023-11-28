import random

replies = [
    "Ваш контент!",
    "Это для вас!",
    "Вот что я нашла...",
    "Смотрите, что у меня есть!",
    "Вот оно!!!!"
]

async def get_random_reply():
    return random.choice(replies)