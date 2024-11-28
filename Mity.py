from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ParseMode
import asyncio

from aiogram.utils import executor

bot = Bot(token='7503679104:AAHbS8DwfayIyqqp_2BWy7TRG4ddpsZWg-U')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start_menu(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Рассчитать', 'Информация')
    await message.answer('Выберите опцию:', reply_markup=keyboard)

@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(
        types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories'),
        types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
    )
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула миффлина-Сан Жеора: M = 10 * вес(кг) + 6.25 * рост(см) - 5 * возраст(г) + 5')

@dp.callback_query_handler(text='calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите ваш возраст:')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)