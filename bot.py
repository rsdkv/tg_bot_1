from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import random
from config import TOKEN

import markup as nav
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# @test6767test_bot

# старт
@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.   id, 'Привет{0.first_name}'.format(message.from_user), reply_markup=nav.mainMenu)


@dp.message_handler()
async def with_puree(message: types.Message):
    if message.text == 'Учиться':
        await bot.send_message(message.from_user.id, 'Здесь вы можете найти... \n '
                                                     'весь этот текст нужно будет вынести '
                                                     'в отдельный файл и мне дать',
                               reply_markup=nav.eduMenu)

    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'возращение в главное меню', reply_markup=nav.mainMenu)
    elif message.text == 'Стать лучше':
        await bot.send_message(message.from_user.id, 'тут я не понял куда ведёт, можно ещё раз написать?', reply_markup=nav.improveMenu)
    elif message.text == 'Книги':
        await bot.send_message(message.from_user.id, 'тут будет список книг,\n  '
                                                     'это тоже нужно дать текстом мне',
                               reply_markup=nav.improveMenu)

    else:
        await message.reply('Неизветсная команда')

@dp.message_handler(lambda message: message.text == "1-->111")
async def without_puree(message: types.Message):
    await message.reply("111!")


# echo - заглушка

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("С помощью этого бота ты можешь получить много полезной информации и записаться на обучение")


if __name__ == '__main__':
    executor.start_polling(dp)
