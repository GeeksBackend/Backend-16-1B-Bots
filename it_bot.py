from aiogram import Bot, Dispatcher, types, executor
from config import token 
import logging

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Курсы'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Записаться'),
]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Привет {message.from_user.first_name}!", reply_markup=start_keyboard)
    # await message.answer(f"{message}")

@dp.message_handler(text="О нас")
async def about(message:types.Message):
    await message.reply("Geeks - это айти курсы в Бишкеке, Ташкенте и Оше! Основана в 2019")

@dp.message_handler(text="Контакты")
async def contacts(message:types.Message):
    await message.answer_contact("0777121212", "Nurbolot", "Erkinbaev")
    await message.answer_contact("0555141516", "Ulan", "Ashirov")
    await message.answer_contact("+996 225 082021", "Geeks", "Admin")

@dp.message_handler(text="Адрес")
async def send_address(message:types.Message):
    await message.answer("Отправляю местоположение...")
    await message.answer_location(40.52, 72.8030)

courses_buttons = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("iOS"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("Назад")
]
courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text="Курсы")
async def all_couses(message:types.Message):
    await message.answer("Вот все наши курсы:", reply_markup=courses_keyboard)

@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /start")

executor.start_polling(dp)