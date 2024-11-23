from aiogram import Bot, Dispatcher, executor, types
import asyncio

api =
bot = Bot(token = api)
dp = Dispatcher(bot )


@dp.message_handler(text = ["Привет"])
async def привет_massage(massage):
    print("Привет , что бы начать нажмите /start")
    await massage.answer("Привет , что бы начать нажмите /start")



@dp.message_handler(commands=['start'])
async def start_massage(massage):
    print("start massage")
    await massage.answer("Првиет!Рады вас у нас видеть ")

@dp.message_handler()
async def all_massage(massage):
    print("Мы получили сообщение ")
    await massage.answer(massage.types.upper())

if __name__ == "__main__" :
    executor.start_polling(dp, skip_updates=True)

