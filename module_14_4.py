import asyncio
import logging
from itertools import product
from math import asinh

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
    CallbackQuery
from babel.plural import in_range_list
from cb import *
import texts
from admin import *
from crud_functions import get_all_products
from db import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7503679104:AAHbS8DwfayIyqqp_2BWy7TRG4ddpsZWg-U")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Рассчитать', 'Информация','Купить']
    keyboard.add(*[KeyboardButton(text) for text in buttons])
    await message.answer("Выберите действие:", reply_markup=keyboard)

@dp.callback_query_handler(text = 'product_buying')
async def send_confirm_message(callback: CallbackQuery):
    await callback.message.answer(text = "Вы успешно приобрели продукт!")
    await callback.answer()

@dp.message_handler(Text(equals='Купить'))
async def get_buying_list(message: types.Message):
    list_text = [texts.Mgame, texts.Lgame,  texts.XLgame, texts.XXLgame]
    products =  get_all_products()
    for i in range(1,5):
        with open(f"files/{i}.png.jpg", 'rb') as img:
            await message.answer_photo(img, f"Название: {products[i - 1][1]} | Описание: {products[i - 1][2]}  | Цена: {products[i - 1][3]} ")
            #"Название: <title> | Описание: <description> | Цена: <price>"
    await message.answer("Выберите продукт для покупки:", reply_markup = catalog_kb)

@dp.callback_query_handler(text='product_buying1')
async def set_age(callback: types.Message):
    with open('files/1.png.jpg', 'rb') as img:
        await callback.message.answer_photo(img, texts.Mgame, reply_markup = catalog_kb)

@dp.callback_query_handler(text='product_buying2')
async def set_age(callback: types.Message):
    with open('files/2.png.jpg', 'rb') as img:
        await callback.message.answer_photo(img, texts.Lgame, reply_markup = catalog_kb)

@dp.callback_query_handler(text='product_buying3')
async def set_age(callback: types.Message):
    with open('files/3.png.jpg', 'rb') as img:
        await callback.message.answer_photo(img, texts.XLgame, reply_markup=catalog_kb)

@dp.callback_query_handler(text='product_buying4')
async def set_age(callback: types.Message):
    with open('files/4.png.jpg', 'rb') as img:
        await callback.message.answer_photo(img, texts.XXLgame, reply_markup=catalog_kb)

#message.answer_photo
#message.answer_video
#message.answer_file

@dp.message_handler(Text(equals="Рассчитать"))
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: (10 * вес в кг) + (6.25 * рост в см) - (5 * возраст) + 5")
    await call.answer()

@dp.callback_query_handler(text='calories')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост (в см):')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес (в кг):')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = float(data['weight'])

    calories = 655 + (9.6 * weight) + (1.85 * growth) - (4.7 * age)
    await message.answer(f"Ваша примерная норма калорий: {calories:.0f} ккал", parse_mode=ParseMode.MARKDOWN)
    await state.finish()

@dp.message_handler(text='Информация', state=None)
async def info(message: types.Message):
    await message.answer("Здесь будет информация о расчете калорий.")

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())