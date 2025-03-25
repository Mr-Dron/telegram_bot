from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

def genres_kb(all_genres: list) -> ReplyKeyboardMarkup:
    """Создает reply-клавиатуру из всех жанров фильмов, которые есть на Kinopisk

    Args:
        all_genres (list): Список из всех жанров фильмов

    Returns:
        _type_: ReplyKeyboardMarkup
    """
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for genre in all_genres:
        keyboard.add(KeyboardButton(genre))
    
    return keyboard


def go_to_output_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для продолжения вывода или выхода из поиска

    Returns:
        InlineKeyboardMarkup
    """
    further_button = InlineKeyboardButton(text="Далее", callback_data="next_to_search_output")
    exit_output_button = InlineKeyboardButton(text="Выйти из поиска", callback_data="exit_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(further_button, exit_output_button)
    
    return keyboard

def add_additional_or_continue_output() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для добавления дополнительных фильтров или продолжения поиска

    Returns:
        InlineKeyboardMarkup
    """
    additional_filter_button = InlineKeyboardButton(text="Добавить дополнительные фильтры", callback_data="additional_filter")
    continue_output_button = InlineKeyboardButton(text="Продолжить поиск", callback_data="continue_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(additional_filter_button)
    keyboard.add(continue_output_button)
    
    return keyboard
    
def additional_filter_kb() -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для выбора дополнительных фильтров или продолжения поиска

    Returns:
        InlineKeyboardMarkup
    """
    filter_rating_button = InlineKeyboardButton(text="Выбрать рейтинг", callback_data="filter_rating")
    filter_budget_button = InlineKeyboardButton(text="Выбрать бюджет", callback_data="filter_budget")
    continue_without_anything_button = InlineKeyboardButton(text="Продолжить поиск", callback_data="continue_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(filter_rating_button, filter_budget_button)
    keyboard.add(continue_without_anything_button)
    
    return keyboard