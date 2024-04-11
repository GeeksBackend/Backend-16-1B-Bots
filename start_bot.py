from aiogram import Bot, Dispatcher, types, executor
from config import token 

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет")

@dp.message_handler(commands='help')
async def help(message:types.Message):
    await message.answer("Чем могу вам помочь?")

@dp.message_handler(text="Привет")
async def hello(message:types.Message):
    await message.reply("Привет, как дела?")

@dp.message_handler(commands='test')
async def test(message:types.Message):
    await message.answer_location(0, 0)
    await message.answer_photo("https://lh3.googleusercontent.com/Ek63xemXlxAwPTFjoSWw3Y8iTgiI48AD_w5Z2NKEDEGF0MJPV72cpOeSOi6-LFUVA5DKl6UYjTPBc07b2MLxwfQkS-dAVjNOxBXj2BALne3b2X8XbcjLO0TXMNX0Mq0ovUdWLIVzmGrmD4hHAnERg34")
    await message.answer_dice()

executor.start_polling(dp)