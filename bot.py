from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from config import TOKEN

import markup as nav

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# @test6767test_bot

# обработчик списка фильмов
with open('text_films.txt', encoding='utf8') as f:
    lines = f.readlines()
films_text = ''
for item in lines:
    films_text += item

# обработчик списка книг
with open('text_books.txt', encoding='utf8') as f:
    lines = f.readlines()
books_text = ''
for item in lines:
    books_text += item

# обработчик текста обучения
with open('text_edu.txt', encoding='utf8') as f:
    lines = f.readlines()
edu_text = ''
for item in lines:
    edu_text += item

# обработчик текста музыки
with open('text_musics.txt', encoding='utf8') as f:
    lines = f.readlines()
music_text = ''
for item in lines:
    music_text += item

# обработчик текста ссылок
with open('text_links.txt', encoding='utf8') as f:
    lines = f.readlines()
links_text = ''
for item in lines:
    links_text += item

# обработчик текста арбитража
with open('text_arbitrage.txt', encoding='utf8') as f:
    text_arbitrage = f.read()


# старт
@dp.message_handler(commands=['start', 'начать', 'старт'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name} '
                                                 'Я Гендиректор Виктори, бот, созданный '
                                                 'для помощи вам. Что вы хотели бы?'.format(message.from_user),
                           reply_markup=nav.mainMenu)


# меню
@dp.message_handler()
async def with_puree(message: types.Message):
    # главное меню
    if message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Главное меню', reply_markup=nav.mainMenu)
    elif message.text == 'Учиться':
        await bot.send_message(message.from_user.id,
                               'Здесь вы можете найти всё, что вам может понадобиться для обучения: \n' + edu_text,
                               reply_markup=nav.eduMenu)
    elif message.text == 'Стать лучше':
        await bot.send_message(message.from_user.id,
                               'Здесь вы можете найти все, что вам может понадобиться. Выберите интересующую вас тему',
                               reply_markup=nav.traderMenu)
    elif message.text == 'Развлечься':
        await bot.send_message(message.from_user.id, 'Вы можете не только развлечься, но и прокачать свой мозг',
                               reply_markup=nav.libraryMenu)
        # библиотека подменю
    elif message.text == 'Фильмы':
        await bot.send_message(message.from_user.id, 'Список для просмотра:\n' + films_text,
                               reply_markup=nav.filmsMenu)
    elif message.text == 'Книги':
        await bot.send_message(message.from_user.id, 'Список книг, которые могут изменить вышу жизнь:\n' + books_text,
                               reply_markup=nav.booksMenu)
    elif message.text == 'Музыка':
        await bot.send_message(message.from_user.id, 'Ссылки на ресурсы для прослушивания:\n ' + music_text,
                               reply_markup=nav.musicsMenu)
    elif message.text == 'Другие материалы':
        await bot.send_message(message.from_user.id, 'Ссылки на ресурсы: \n' + links_text,
                               reply_markup=nav.mainMenu)
    elif message.text == 'Трейдеру':
        await bot.send_message(message.from_user.id, 'Здесь есть всё, что вам может понадобиться',
                               reply_markup=nav.traderMenu)
    elif message.text == 'Арбитражи':
        await bot.send_message(message.from_user.id, text_arbitrage,
                               reply_markup=nav.arbitrageMenu)
    else:
        await message.reply('Неизветсная команда')


# echo - заглушка

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("С помощью этого бота ты можешь получить много полезной информации и записаться на обучение")


if __name__ == '__main__':
    executor.start_polling(dp)
