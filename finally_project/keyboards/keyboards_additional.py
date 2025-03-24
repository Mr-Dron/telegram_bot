from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def add_additional_or_continue_output():
    additional_filter_button = InlineKeyboardButton(text="Добавить дополнительные фильтры", callback_data="additional_filter")
    continue_output_button = InlineKeyboardButton(text="Продолжить поиск", callback_data="continue_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(additional_filter_button)
    keyboard.add(continue_output_button)
    
    return keyboard
    
def additional_filter_kb():
    filter_rating_button = InlineKeyboardButton(text="Выбрать рейтинг", callback_data="filter_rating")
    filter_budget_button = InlineKeyboardButton(text="Выбрать бюджет", callback_data="filter_budget")
    continue_without_anything_button = InlineKeyboardButton(text="Продолжить поиск", callback_data="continue_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(filter_rating_button, filter_budget_button)
    keyboard.add(continue_without_anything_button)
    
    return keyboard