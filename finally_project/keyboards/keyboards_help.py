from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def help_keyboad() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для возвращения в меню или сообщения об ошибке

    Returns:
        InlineKeyboardMarkup
    """
    main_button = InlineKeyboardButton(text="Меню", callback_data="menu")
    error_button = InlineKeyboardButton(text="Нашел(а) ошибку", callback_data="error")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(main_button)
    keyboard.add(error_button)
    
    return keyboard