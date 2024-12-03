import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7503679104:AAHbS8DwfayIyqqp_2BWy7TRG4ddpsZWg-U")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Создание inline-клавиатуры
inline_kb = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton(text='Рассчитать норму калорий', callback_data = 'calories'),
    InlineKeyboardButton(text='Формулы расчёта', callback_data = 'formulas')
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Рассчитать', 'Информация']
    keyboard.add(*[KeyboardButton(text) for text in buttons])
    await message.answer("Выберите действие:", reply_markup=keyboard)

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
