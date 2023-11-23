import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
privetstviye = "Привет! Это бот для заказа хлебобулочных изделий! Скорее выбирай в меню то, что ты конкретно хочешь."
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6754050049:AAHFbhmkp-ub3xKgYiY6xSq2TT58vQ3XyIs")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(privetstviye)
    kb = [
        [types.KeyboardButton(text="Из столовой")],
        [types.KeyboardButton(text="Из пекарни")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer("Выберите откуда вы хотите заказать еду.", reply_markup=keyboard)

@dp.message(F.text.lower() =="из столовой" or F.text.lower() == "из пекарни")
async def stolovaya(message: types.Message):
    builder = ReplyKeyboardBuilder()
    reply_markup = builder.as_markup(resize_keyboard=True)
    kb = [
        [types.KeyboardButton(text="Сосиска в тесте")],
        [types.KeyboardButton(text="Пирожок с капустой")],
        [types.KeyboardButton(text="Пирожок с вишней")],
        [types.KeyboardButton(text="Пирожок с яблоком")],
        [types.KeyboardButton(text="Choco pie")],
        [types.KeyboardButton(text="Юбилейное с шоколадом")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(text="Выберите позицию из списка.",reply_markup=keyboard)
@dp.message(F.text.lower() =="сосиска в тесте" or F.text.lower() == "пирожок с капустой" or F.text.lower() == "пирожок с вишней" or F.text.lower() == "пирожок с яблоком" or F.text.lower() == "choco pie"or F.text.lower() == "юбилейное с шоколадом")
async def zakaz(message: types.Message):
    await message.answer(text="Введите здание, в котором вы находитесь, кабинет, ник в тг.")
    @dp.message(F.text)
    async def zakaz1(message: types.Message):
        place = message
        await message.answer(text=place)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())