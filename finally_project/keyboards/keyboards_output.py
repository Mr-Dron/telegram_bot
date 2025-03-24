from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove

# Вывод результата поиска
def go_to_output_search():
    further_button = InlineKeyboardButton(text="Далее", callback_data="next_to_search_output")
    exit_output_button = InlineKeyboardButton(text="Выйти из поиска", callback_data="exit_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(further_button, exit_output_button)
    
    return keyboard

def output_search_kb(current_index, length):
    exit_output_button = InlineKeyboardButton(text="Выйти из поиска", callback_data="exit_to_menu")
    next_movie_button = InlineKeyboardButton(text="Вперёд --->", callback_data="next_movie_search")
    previous_movie_button = InlineKeyboardButton(text="<--- Назад", callback_data="previous_movie_search")
    page_button = InlineKeyboardButton(text=f"{current_index + 1} из {length}", callback_data=" ")
    add_to_favorites_button = InlineKeyboardButton(text="Добавить в избранное", callback_data="add_to_favorites")
    
    keyboard = InlineKeyboardMarkup()
    if length == 1:
        keyboard.add(add_to_favorites_button)
        keyboard.add(page_button)
        keyboard.add(exit_output_button)
    elif current_index == 0:
        keyboard.add(add_to_favorites_button)
        keyboard.add(page_button, next_movie_button)
        keyboard.add(exit_output_button)
    elif current_index == length - 1:
        keyboard.add(add_to_favorites_button)
        keyboard.add(previous_movie_button, page_button)
        keyboard.add(exit_output_button)
    else: 
        keyboard.add(add_to_favorites_button)
        keyboard.add(previous_movie_button, page_button, next_movie_button)
        keyboard.add(exit_output_button)
    
    return keyboard

# Вывод истории поиска
def go_to_output_hisoty():
    further_button = InlineKeyboardButton(text="Далее", callback_data="next_to_history_output")
    exit_output_button = InlineKeyboardButton(text="Выйти из истории", callback_data="exit_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(further_button, exit_output_button)
    
    return keyboard

def output_history_kb(current_index, length):
    exit_output_button = InlineKeyboardButton(text="Выйти из истории", callback_data="exit_to_menu")
    next_movie_button = InlineKeyboardButton(text="Вперёд --->", callback_data="next_movie_history")
    previous_movie_button = InlineKeyboardButton(text="<--- Назад", callback_data="previous_movie_history")
    page_button = InlineKeyboardButton(text=f"{current_index + 1} из {length}", callback_data=" ")
    add_to_favorites_button = InlineKeyboardButton(text="Добавить в избранное", callback_data="add_to_favorites_history")
    
    keyboard = InlineKeyboardMarkup()
    if length == 1:
        keyboard.add(add_to_favorites_button)
        keyboard.add(page_button)
        keyboard.add(exit_output_button)
    elif current_index == 0:
        keyboard.add(add_to_favorites_button)
        keyboard.add(page_button, next_movie_button)
        keyboard.add(exit_output_button)
    elif current_index == length - 1:
        keyboard.add(add_to_favorites_button)
        keyboard.add(previous_movie_button, page_button)
        keyboard.add(exit_output_button)
    else: 
        keyboard.add(add_to_favorites_button)
        keyboard.add(previous_movie_button, page_button, next_movie_button)
        keyboard.add(exit_output_button)
    
    return keyboard

# вывод списка избранного
def go_to_output_favorite():
    further_button = InlineKeyboardButton(text="Далее", callback_data="next_to_favorite_output")
    exit_output_button = InlineKeyboardButton(text="Выйти из списка желаемого", callback_data="exit_output")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(further_button, exit_output_button)
    
    return keyboard

def output_favorite_kb(current_index, length):
    exit_output_button = InlineKeyboardButton(text="Выйти из списка желаемого", callback_data="exit_to_menu")
    next_movie_button = InlineKeyboardButton(text="Вперёд --->", callback_data="next_movie_favorite")
    previous_movie_button = InlineKeyboardButton(text="<--- Назад", callback_data="previous_movie_favorite")
    page_button = InlineKeyboardButton(text=f"{current_index + 1} из {length}", callback_data=" ")
    remove_from_favorites_button = InlineKeyboardButton(text="Удалить из избранного", callback_data="remove_from_favorites")
    
    keyboard = InlineKeyboardMarkup()
    if length == 1:
        keyboard.add(remove_from_favorites_button)
        keyboard.add(page_button)
        keyboard.add(exit_output_button)
    elif current_index == 0:
        keyboard.add(remove_from_favorites_button)
        keyboard.add(page_button, next_movie_button)
        keyboard.add(exit_output_button)
    elif current_index == length - 1:
        keyboard.add(remove_from_favorites_button)
        keyboard.add(previous_movie_button, page_button)
        keyboard.add(exit_output_button)
    else: 
        keyboard.add(remove_from_favorites_button)
        keyboard.add(previous_movie_button, page_button, next_movie_button)
        keyboard.add(exit_output_button)
    
    return keyboard