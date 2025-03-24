from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def try_set_limit():
    try_again_button = InlineKeyboardButton(text="Попробовать еще раз", callback_data="try_again")
    exit_menu = InlineKeyboardButton(text="Вернуться в меню", callback_data="exit_menu")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(try_again_button)
    keyboard.add(exit_menu)
    
    return keyboard