import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types


wikipedia.set_lang('ru')

def search_page(name):
    tru_obj = wikipedia.page(name)
    return tru_obj.url

logging.basicConfig(level=logging.INFO)
bot = Bot(token='5060205687:AAFOfR5D-2SPCqOLQtifweD2KxeqcN7Fxkg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer('Привет! Что ты хочешь найти в википедии?')


@dp.message_handler()
async def get_page_wiki(message: types.Message):
    find_page = search_page(message.text)
    await message.answer(find_page)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)