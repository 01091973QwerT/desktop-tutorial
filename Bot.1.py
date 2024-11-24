import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7503679104:AAHbS8DwfayIyqqp_2BWy7TRG4ddpsZWg-U")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text = ["Привет"])
async def привет_massage(massage):
    print("Привет , что бы начать нажмите /start")
    await massage.answer("Привет , что бы начать нажмите /start")



@dp.message_handler(commands=['start'])
async def start_massage(massage):
    print("start massage")
    await massage.answer("Првиет! Напиши слово Калории и начнем ")

@dp.message_handler(text='Калории', state=None)
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

    # Упрощенная формула Миффлина-Сан Жеора для женщин (пример)
    # Для мужчин формула немного другая.
    calories = 655 + (9.6 * weight) + (1.85 * growth) - (4.7 * age)


    await message.answer(f"Ваша примерная норма калорий: {calories:.0f} ккал", parse_mode=ParseMode.MARKDOWN)
    await state.finish()


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
