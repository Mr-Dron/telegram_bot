from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_keyboard():
    name_button = InlineKeyboardButton(text="Поиск по названию", callback_data="search_name")
    rating_button = InlineKeyboardButton(text="Поиск по рейтингу", callback_data="search_rating")
    history_button = InlineKeyboardButton(text="История поиска", callback_data="history")
    genre_button = InlineKeyboardButton(text="Поиск по жанру", callback_data="search_genre")
    favorite_button = InlineKeyboardButton(text="Список желаемого", callback_data="favorite")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(name_button)
    keyboard.add(rating_button)
    keyboard.add(history_button)
    keyboard.add(genre_button)
    keyboard.add(favorite_button)
    
    return keyboard  

def main_keyboard_admin():
    name_button = InlineKeyboardButton(text="Поиск по названию", callback_data="search_name")
    rating_button = InlineKeyboardButton(text="Поиск по рейтингу", callback_data="search_rating")
    history_button = InlineKeyboardButton(text="История поиска", callback_data="history")
    genre_button = InlineKeyboardButton(text="Поиск по жанру", callback_data="search_genre")
    admin_panel_button = InlineKeyboardButton(text="Админ панель", callback_data="admin_panel")
    favorite_button = InlineKeyboardButton(text="Список желаемого", callback_data="favorite")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(name_button)
    keyboard.add(rating_button)
    keyboard.add(history_button)
    keyboard.add(genre_button)
    keyboard.add(favorite_button)
    keyboard.add(admin_panel_button)
    
    return keyboard  

def admin_keyboard():
    delete_db_button = InlineKeyboardButton(text="Очистить историю за дату", callback_data="delete_db")
    my_data_button = InlineKeyboardButton(text="Мои данные", callback_data="my_data")
    all_users_button = InlineKeyboardButton(text="Все пользователи", callback_data="all_users")
    all_history_button = InlineKeyboardButton(text="Вся история поиска", callback_data="all_history")
    any_user_history_button = InlineKeyboardButton(text="История поиска пользователя", callback_data="any_user_history")
    user_buttons_button = InlineKeyboardButton(text="кнопки пользователя", callback_data="user_buttons")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(delete_db_button, my_data_button, all_users_button, 
                 all_history_button, any_user_history_button, user_buttons_button)
    
    return keyboard  

def go_to_menu_kb():
    go_to_menu_button = InlineKeyboardButton(text="Вернуться в меню", callback_data="menu")
    
    keyboard = InlineKeyboardMarkup()
    keyboard.add(go_to_menu_button)
    
    return keyboard