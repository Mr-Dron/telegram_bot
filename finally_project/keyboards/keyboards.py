# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
# from states.bot_state import UserState


# def main_keyboard():
#     name_button = InlineKeyboardButton(text="Поиск по названию", callback_data="search_name")
#     rating_button = InlineKeyboardButton(text="Поиск по рейтингу", callback_data="search_rating")
#     history_button = InlineKeyboardButton(text="История поиска", callback_data="history")
#     genre_button = InlineKeyboardButton(text="Поиск по жанру", callback_data="genre")
#     favorite_button = InlineKeyboardButton(text="Список желаемого", callback_data="favorite")
    
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(name_button)
#     keyboard.add(rating_button)
#     keyboard.add(history_button)
#     keyboard.add(genre_button)
#     keyboard.add(favorite_button)
    
#     return keyboard  

# def go_to_main_keyboard():
#     go_to_menu = KeyboardButton(text="Вернуться в меню")
    
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     keyboard.add(go_to_menu)
    
#     return keyboard

# def history_keyboard(date_list):
    
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     for date in date_list: 
#         keyboard.add(KeyboardButton(date))
    
#     return keyboard

# def admin_keyboard_us():
#     name_button = InlineKeyboardButton(text="Поиск по названию", callback_data="search_name")
#     rating_button = InlineKeyboardButton(text="Поиск по рейтингу", callback_data="search_rating")
#     history_button = InlineKeyboardButton(text="История поиска", callback_data="history")
#     genre_button = InlineKeyboardButton(text="Поиск по жанру", callback_data="genre")
#     admin_panel_button = InlineKeyboardButton(text="Админ панель", callback_data="admin_panel")
#     favorite_button = InlineKeyboardButton(text="Список желаемого", callback_data="favorite")
    
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(name_button)
#     keyboard.add(rating_button)
#     keyboard.add(history_button)
#     keyboard.add(genre_button)
#     keyboard.add(favorite_button)
#     keyboard.add(admin_panel_button)
    
#     return keyboard  

# def admin_keyboard_ad():
#     delete_db_button = InlineKeyboardButton(text="Очистить историю за дату", callback_data="delete_db")
#     my_data_button = InlineKeyboardButton(text="Мои данные", callback_data="my_data")
#     all_users_button = InlineKeyboardButton(text="Все пользователи", callback_data="all_users")
#     all_history_button = InlineKeyboardButton(text="Вся история поиска", callback_data="all_history")
#     any_user_history_button = InlineKeyboardButton(text="История поиска пользователя", callback_data="any_user_history")
#     user_buttons_button = InlineKeyboardButton(text="кнопки пользователя", callback_data="user_buttons")
    
#     keyboard = InlineKeyboardMarkup()
#     keyboard.add(delete_db_button, my_data_button, all_users_button, 
#                  all_history_button, any_user_history_button, user_buttons_button)
    
#     return keyboard  

# def search_movie_kb(current_index, length):
#     next_movie_button = InlineKeyboardButton(text="Следующий", callback_data=f"next_movie")
#     previous_movie_button = InlineKeyboardButton(text="Предыдущий", callback_data=f"previous_movie")
#     add_to_favorites_button = InlineKeyboardButton(text="Добавить в избранное", callback_data=f"add_to_favorites_movie")
#     exit_search_button = InlineKeyboardButton(text="Выйти из поиска", callback_data="exit_search")
    
#     keyboard = InlineKeyboardMarkup()
#     if current_index == 0: 
#         keyboard.add(next_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
#     elif current_index == length - 1:
#         keyboard.add(previous_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
#     elif length == 1:
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
#     else:
#         keyboard.add(next_movie_button, previous_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
    
#     return keyboard

# def default_keyboard_search(count):
#     further_button = InlineKeyboardButton(text="Далее", callback_data="further_to_the_out_serch")
#     exit_serach_button = InlineKeyboardButton(text="Выйти из поиска", callback_data="exit_search")
    
#     keyboard = InlineKeyboardMarkup()
#     if count == 0:
#         keyboard.add(exit_serach_button)
#     else:
#         keyboard.add(further_button, exit_serach_button)
    
#     return keyboard

# def default_keyboard_history(count):
#     further_button = InlineKeyboardButton(text="Далее", callback_data="further_to_the_out_history")
#     exit_serach_button = InlineKeyboardButton(text="Выйти из истории", callback_data="exit_history")
    
#     keyboard = InlineKeyboardMarkup()
#     if count == 0:
#         keyboard.add(exit_serach_button)
#     else:
#         keyboard.add(further_button, exit_serach_button)
    
#     return keyboard

# def default_keyboard_favorite(count):
#     further_button = InlineKeyboardButton(text="Далее", callback_data="further_to_the_out_favorite")
#     exit_serach_button = InlineKeyboardButton(text="Выйти из списка желаемого", callback_data="exit_favorite")
    
#     keyboard = InlineKeyboardMarkup()
#     if count == 0:
#         keyboard.add(exit_serach_button)
#     else:
#         keyboard.add(further_button)
#         keyboard.add(exit_serach_button)
    
#     return keyboard

# def favorite_movie_kb(current_index, length):
#     next_movie_button = InlineKeyboardButton(text="Следующий", callback_data=f"next_movie_fav")
#     previous_movie_button = InlineKeyboardButton(text="Предыдущий", callback_data=f"previous_movie_fav")
#     exit_search_button = InlineKeyboardButton(text="Выйти из списка желаемого", callback_data="exit_favorite")
    
#     keyboard = InlineKeyboardMarkup()
#     if current_index == 0: 
#         keyboard.add(next_movie_button)
#         keyboard.add(exit_search_button)
#     elif current_index == length - 1:
#         keyboard.add(previous_movie_button)
#         keyboard.add(exit_search_button)
#     elif length == 1:
#         keyboard.add(exit_search_button)
#     else:
#         keyboard.add(next_movie_button, previous_movie_button)
#         keyboard.add(exit_search_button)
    
#     return keyboard

# def cash_movie_kb(current_index, length):
#     next_movie_button = InlineKeyboardButton(text="Следующий", callback_data=f"next_movie_hist")
#     previous_movie_button = InlineKeyboardButton(text="Предыдущий", callback_data=f"previous_movie_hist")
#     add_to_favorites_button = InlineKeyboardButton(text="Добавить в избранное", callback_data=f"add_to_favorites_movie_hist")
#     exit_search_button = InlineKeyboardButton(text="Выйти из истории", callback_data="exit_history")
    
#     keyboard = InlineKeyboardMarkup()
#     if current_index == 0: 
#         keyboard.add(next_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
#     elif current_index == length - 1:
#         keyboard.add(previous_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
#     elif length == 1:
#         keyboard.add(add_to_favorites_button, exit_search_button)
#     else:
#         keyboard.add(next_movie_button, previous_movie_button)
#         keyboard.add(add_to_favorites_button)
#         keyboard.add(exit_search_button)
    
#     return keyboard

# def genres_kb(all_genres):
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     for genre in all_genres:
#         keyboard.add(KeyboardButton(genre))
    
#     return keyboard