import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
import random

from gtts import gTTS
import os

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == 'news')
async def news(callback: CallbackQuery):
    await callback.answer("Загрузка новостей...", show_alert=True)
    await callback.message.answer('Вот свежие новости')


@dp.message(F.text == "Тестовая кнопка 1")
async def test_button(message: Message):
    await message.answer('Обработка нажатия на reply кнопку')

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Это бот умеет выполнять команды: \n /start \n /help \n /minitranning')

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет,{message.from_user.first_name}!', reply_markup=kb.inline_keyboard_test)




#@dp.message(Command('training'))
#async def training(message: Message):
#    training_list = [
#        "Тренировка 1:\n1. Скручивания: 3 подхода по 15 повторений\n2. Велосипед: 3 подхода по 20 повторений (каждая сторона)\n3. Планка: 3 подхода по 30 секунд",
#        "Тренировка 2:\n1. Подъемы ног: 3 подхода по 15 повторений\n2. Русский твист: 3 подхода по 20 повторений (каждая сторона)\n3. Планка с поднятой ногой: 3 подхода по 20 секунд (каждая нога)",
#        "Тренировка 3:\n1. Скручивания с поднятыми ногами: 3 подхода по 15 повторений\n2. Горизонтальные ножницы: 3 подхода по 20 повторений\n3. Боковая планка: 3 подхода по 20 секунд (каждая сторона)"
#    ]
#    rand_tr = random.choice(training_list)
#    await message.answer(f"Это ваша мини-тренировка на сегодня {rand_tr}")

#    tts = gTTS(rand_tr, lang='ru')
#    tts.save('training.ogg')
#    audio = FSInputFile('training.ogg')
#    await bot.send_voice(message.chat.id, audio)
#    os.remove('training.ogg')


#@dp.message(Command('photo', prefix='&'))
#async def photo(message: Message):
#    list = ['https://ic.pics.livejournal.com/kiowa_mike/11303100/6116166/6116166_600.jpg', 'https://i.pinimg.com/736x/ac/c7/ae/acc7ae3d2f8f8e15b2e452633219cab2.jpg', 'https://cs12.pikabu.ru/post_img/big/2019/04/16/11/1555438706155677273.jpg','https://media-cdn.tripadvisor.com/media/photo-s/1b/6a/2f/e3/caption.jpg']
#    rand_photo = random.choice(list)
#    await message.answer_photo(photo=rand_photo, caption='Это фото для тебя!')

#@dp.message (F.photo)
#async def react_photo(message: Message):
#    list = ['Классное фото!', 'Супер!', 'Огонь!', 'Непонятно!']
#    rand_answ = random.choice(list)
#    await message.answer(rand_answ)
#    await bot.download(message.photo[-1], destination=f'tmp/{message.photo[-1].file_id}.jpg')

#@dp.message (F.text == 'Что такое ИИ?')
#async def aitext(message: Message):
#    await message.answer('Искусственный интеллект — компьютерные системы, имитирующие человеческое мышление.')

#@dp.message(Command('help'))
#async def help(message: Message):
#    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /video \n /audio \n /photo \n &photo \n /training \n /voice \n /doc')

#@dp.message(CommandStart())
#async def start(message: Message):
#    await message.answer(f'Привет, {message.from_user.full_name}!')

#@dp.message()
#async def start(message: Message):
#    if message.text.lower() == 'тест':
#        await message.answer('тестируем')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())





