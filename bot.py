from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from dotenv import load_dotenv
from api.model import square
import logging
import os
from api.utils.static_text import  START, INFO, SORRY
#from config import TOKEN

logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    level=logging.INFO)

load_dotenv()
TOKEN=os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_name=message.from_user.full_name
    user_id=message.from_user.id
    await message.reply(START %user_name, parse_mode='MarkdownV2')


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)


# @dp.message_handler()
# async def echo_message(message: types.Message):
#     if message.content_type not in 'text':
#         await message.reply(SORRY)
#     else:
#         await bot.send_message(message.from_user.id, square(int(message.text)))

@dp.message_handler()
async def square_message(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'Нам написал {user_name}, его id = {user_id}')
    if message.text.isdigit() and  len(message.text)<= 10:
            await bot.send_message(message.from_user.id, square(int(message.text)))
    else:
        await message.reply(SORRY)

if __name__ == '__main__':
    executor.start_polling(dp)