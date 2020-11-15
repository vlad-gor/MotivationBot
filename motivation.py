import asyncio
import csv
import random
import os

from aiogram import Bot, Dispatcher, executor, types
from models import Aphorism
from db_manager import DB_manager
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('TOKEN')
user_id = os.getenv('USER_ID')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

loop = asyncio.get_event_loop()

dbM = DB_manager()
dbM.create_table(Aphorism)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm MotivationBot!\nPowered by aiogram.")

@dp.message_handler(commands=['add'])
async def add_aphorism(message: types.Message):
    '''
    Добавление афоризма в базу
    '''
    pass

# Periodic tasks
async def send_aphorism():
    mes = str(random.choice(dbM.get_records(Aphorism)))
    await bot.send_message(user_id, mes)

def repeat(coro, loop):
    asyncio.ensure_future(coro(), loop=loop)
    loop.call_later(3600, repeat, coro, loop)

if __name__ == '__main__':
    loop.call_later(3600, repeat, send_aphorism, loop)
    executor.start_polling(dp, skip_updates=True)