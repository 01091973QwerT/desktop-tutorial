import asyncio
import logging
from itertools import product
from math import asinh

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery
from babel.plural import in_range_list

from cb import *
import texts
from admin import *
from crud_functions import get_all_products, is_included, add_user




logging.basicConfig(level=logging.INFO)
bot = Bot(token="7503679104:AAHbS8DwfayIyqqp_2BWy7TRG4ddpsZWg-U")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000 # По умолчанию 1000

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Введите 'Регистрация' для начала.")

@dp.message_handler(text = 'Регистрация')
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    if not is_included(username):
        await state.update_data(username =  message.text)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя.")

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email = message.text)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age = message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer(f"Регистрация завершена {data['username'], data['email'],}")
    await state.finish()




async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())