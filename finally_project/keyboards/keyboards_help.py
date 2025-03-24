from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_keyboad():
    main_button = InlineKeyboardButton(text="Меню", callback_data="main")
    error_button = InlineKeyboardButton(text="Нашел(а) ошибку", callback_data="error")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(main_button)
    keyboard.add(error_button)
    
    return keyboard