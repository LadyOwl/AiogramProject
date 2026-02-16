import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message (F.photo)
async def aitext(message: Message):
    list = ['Классное фото!', 'Огонь!', 'Непонятно!']
    rand_ans = random.choice(list)
    await message.answer(rand_ans)


@dp.message (F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — компьютерные системы, имитирующие человеческое мышление.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять комманды: \n /start \n /help')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет, я бот!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())





