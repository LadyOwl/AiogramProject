import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

import random


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('photo', prefix='&'))
async def photo(message: Message):
    list = ['https://ic.pics.livejournal.com/kiowa_mike/11303100/6116166/6116166_600.jpg', 'https://i.pinimg.com/736x/ac/c7/ae/acc7ae3d2f8f8e15b2e452633219cab2.jpg', 'https://cs12.pikabu.ru/post_img/big/2019/04/16/11/1555438706155677273.jpg','https://media-cdn.tripadvisor.com/media/photo-s/1b/6a/2f/e3/caption.jpg']
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это фото для тебя!')

@dp.message (F.photo)
async def react_photo(message: Message):
    list = ['Классное фото!', 'Супер!', 'Огонь!', 'Непонятно!']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1], destination=f'/tmp/{message.photo[-1].file_id}.jpg')


@dp.message (F.text == 'Что такое ИИ?')
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — компьютерные системы, имитирующие человеческое мышление.')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')

@dp.message()
async def start(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())





