import os
from aiogram import Bot, Dispatcher, types
import logging
from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)
API_TOKEN = os.getenv('TOKEN')
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    data = message.text
    keys = 'aeiou'
    count = 0
    for i in keys:
        count += data.count(i)
    if count > 5:
        await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
