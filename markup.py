from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main menu
btnRandom = KeyboardButton('rand digit')
btnOther = KeyboardButton('другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRandom, btnOther)


#other menu
btnInfo= KeyboardButton('info')
btnLink= KeyboardButton('link')