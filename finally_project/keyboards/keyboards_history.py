from telebot.types import KeyboardButton, ReplyKeyboardMarkup

def date_keyboard(date_list):
    
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for date in date_list:
        keyboard.add(KeyboardButton(date))
        
    return keyboard