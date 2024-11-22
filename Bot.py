from aiogram import Bot, Dispatcher, executor, types
import asyncio

api =
bot = Bot(token = api)
dp = Dispatcher(bot )


@dp.message_handler(commands=['start'])
async def start_massage(massage):
    print("Привет! Я бот помогающий твоему здоровью")



@dp.message_handler()
async def all_massage(massage):
    print("Введите команду /start, чтобы начать общение")

if __name__ == "__main__" :
    executor.start_polling(dp, skip_updates=True)

