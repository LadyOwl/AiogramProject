import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from datetime import datetime, timedelta
import random
import requests

from config import TOKEN, NASA_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

def get_random_apod():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + (end_date - start_date) * random.random()
    date_str = random_date.strftime("%Y-%m-%d")
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={date_str}"
    response = requests.get(url)
    return response.json()

async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())