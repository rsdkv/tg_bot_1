from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import random
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @test6767test_bot

# старт
@dp.message_handler(commands="start")
async def process_start_command(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Книги")],
        [types.KeyboardButton(text="Кино")],
        [types.KeyboardButton(text="Трейдинг")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Выберите интересующий вариант из меню"
                                         )
    await message.answer("Что вам интересно?", reply_markup=keyboard)


@dp.message_handler(text="Книги")
async def with_puree(message: types.Message):
    with open("books.txt") as books:
        lines = random.sample(list(books), 10)
        await message.reply(*map(str.strip, lines))


@dp.message_handler(lambda message: message.text == "Без пюрешки")
async def without_puree(message: types.Message):
    await message.reply("Так невкусно!")


# echo - заглушка

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("С помощью этого бота ты можешь получить много полезной информации и записаться на обучение")


if __name__ == '__main__':
    executor.start_polling(dp)
