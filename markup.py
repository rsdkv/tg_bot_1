from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')
# main menu
btnEdu = KeyboardButton('Учиться')
btnImprove = KeyboardButton('Стать лучше')
btnFun = KeyboardButton('Развлечься')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnEdu, btnImprove, btnFun)


#edu menu - из кнопок: вызов главного меню  --   Обучение
eduMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnMain)

# меню для   --  Стать лучше
btnLibrary = KeyboardButton('Книги')
btnForTrader = KeyboardButton('Трейдеру')
improveMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnLibrary, btnForTrader, btnMain)