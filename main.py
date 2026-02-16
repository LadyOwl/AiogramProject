import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


bot = Bot(token='8552150838:AAHoCUeZ558kWRWfhYCf96z8HClol3FrTX8')
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет, я бот!')

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())





