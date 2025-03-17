from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data import config
from telebot.types import Message
from handlers.search_handler import by_name_handler, by_rating_handler, by_genre_handler
from states.bot_state import UserState
from database.models import User, MovieCash
from keyboards.keyboards import default_keyboard_search, default_keyboard_history, default_keyboard_favorite
from utils.output_result import out_search_with_kb, out_cash_with_kb, out_favorite_with_kb
from handlers.default_handler import (start_handler, help_handler, history, delete_handler,
                                      users_handler, admin_panel_hendler, main_hander, 
                                      favorite_movie_hendler)


storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=storage)
search_results = dict()
current_index = dict()

@bot.message_handler(commands=["start"])    # кнопка меню старт
def start(message: Message):
    """Обработка запуска бота и комманды старт

    Args:
        message (Message): команда /start
    """
    start_handler.bot_start(bot, message)


@bot.message_handler(commands=["help"])     # кнопка меню помощь
def help(message: Message):
    """Обработка комманды /help

    Args:
        message (Message): комманда /help
    """
    help_handler.start_help(bot, message)


@bot.callback_query_handler(                # нажатие на кнопку поиска по названию  
    func=lambda callback_query: (
        callback_query.data == "search_name"
    )
)
def search_by_name(callback_query):
    """Обработка нажатия на кнопку 'поиск по названию'. Ловит нажатие кнопки и запускает линейку
    функций поиска фильма по названию и вывод(3 функции)

    Args:
        callback_query: callback кнопки 'поиск по названию'
    """
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    by_name_handler.start_search(bot, callback_query)


@bot.message_handler(state=UserState.search_by_name)    # API запрос на поиск по названию и обработка результата
def search_by_name_progress(message: Message):
    """Функция ловит состояние 'search_by_name'. Отправляет api запрос, получает ответ, 
    конвертирует в json формат, отбирает необходимые ключи и подготавливает список словарей с результатом поиска 

    Args:
        message (Message): название фильма
    """
    search_results[message.from_user.id] = by_name_handler.progress_search(bot, message)
    
    bot.send_message(message.from_user.id, 
                     f"По вашему запросу найдено фильмов\\: *__{len(search_results[message.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=default_keyboard_search(len(search_results[message.from_user.id])), parse_mode="MarkdownV2")
    
    current_index[message.from_user.id] = 0


@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie",
                             "previous_movie",
                             "add_to_favorites_movie",
                             "exit_search",
                             "further_to_the_out_serch"])
def output_search(call):
    """Вывод результата поиска по-одному фильму с клавиатурой

    Args:
        call: Нажатие на кнопки клавиатуры с определенным callback
    """
    global search_results, current_index
    results = search_results[call.from_user.id]
    data = call.data
    if data == "add_to_favorites_movie":
        fav_movie = MovieCash.get(MovieCash.movie_id == results[current_index[call.from_user.id]]["id"])
        fav_movie.movie_viewed = True
        fav_movie.save()
        bot.send_message(call.from_user.id, "{} добавлен в избранные".format(
            results[current_index[call.from_user.id]]["name"]
        ))
    
    current_index[call.from_user.id] = out_search_with_kb(bot, call, results, current_index[call.from_user.id])
    
    if data == "exit_search":
        search_results[call.from_user.id].clear()
        current_index[call.from_user.id] = 0
        main_hander.main_menu_handler(call, bot)
        return
           

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "search_rating"
    )
)
def search_by_rating(callback_query):
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    by_rating_handler.start_search(bot, callback_query)


@bot.message_handler(state=UserState.search_by_rating)
def search_by_rating_progress(message: Message):
    search_results[message.from_user.id] = by_rating_handler.progress_search_by_rating(bot, message)
    
    bot.send_message(message.from_user.id, 
                     f"По вашему запросу найдено\\: *__{len(search_results[message.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=default_keyboard_search(len(search_results[message.from_user.id])), parse_mode="MarkdownV2")
    
    current_index[message.from_user.id] = 0


@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "history"
    )
)
def start_history(callback_query):
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    history.start_history_hendler(bot, callback_query)



@bot.message_handler(state=UserState.history)
def history_progress(message: Message):
    search_results[message.from_user.id] = history.history_progress(bot, message)
    
    bot.send_message(message.from_user.id, f"Найдено фильмов\\: *__{len(search_results[message.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=default_keyboard_history(len(search_results[message.from_user.id])), parse_mode="MarkdownV2")
    
    current_index[message.from_user.id] = 0



@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie_hist",
                             "previous_movie_hist",
                             "add_to_favorites_movie_hist",
                             "exit_history",
                             "further_to_the_out_history"])
def output_cash(call):
    global search_results, current_index
    results = search_results[call.from_user.id]
    
    current_index[call.from_user.id] = out_cash_with_kb(bot, call, results, current_index[call.from_user.id])
    
    data = call.data 
    if data == "exit_history":
        search_results[call.from_user.id].clear()
        current_index[call.from_user.id] = 0
        main_hander.main_menu_handler(call, bot)
        return

@bot.message_handler(state=UserState.main)
def main_menu(message: Message):
    main_hander.main_menu_handler(message, bot)
    

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "genre")
def genre_search_start(callback):
    by_genre_handler.start_search(callback, bot)
    bot.set_state(callback.from_user.id, UserState.search_by_genre)


@bot.message_handler(state=UserState.search_by_genre)
def genre_search(message: Message):
    search_results[message.from_user.id] = by_genre_handler.search_by_genre(message, bot)

    bot.send_message(message.from_user.id, 
                 f"По вашему запросу найдено фильмов\\: *__{len(search_results[message.from_user.id])}__*\n"
                 "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                 reply_markup=default_keyboard_search(len(search_results[message.from_user.id])), parse_mode="MarkdownV2")
    
    current_index[message.from_user.id] = 0

@bot.callback_query_handler(func=lambda callback_query: callback_query.data == "favorite")
def search_favorite_movie(callback):
    search_results[callback.from_user.id] = favorite_movie_hendler.favorite_movie(callback)
    bot.set_state(callback.from_user.id, UserState.favorite_movie)
    current_index[callback.from_user.id] = 0
    
    if search_results[callback.from_user.id]:
        bot.send_message(callback.from_user.id, 
                 f"В вашем списке желаемого фильмов\\: *__{len(search_results[callback.from_user.id])}__*\n"
                 "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                 reply_markup=default_keyboard_favorite(len(search_results[callback.from_user.id])), parse_mode="MarkdownV2")
    
        
    else:
        bot.send_message(callback.from_user.id, "В вашем списке желаемого нет фильмов")
        main_hander.main_menu_handler(callback, bot)
        return

@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie_fav",
                             "previous_movie_fav",
                             "exit_favorite",
                             "further_to_the_out_favorite"])
def output_favotite(call):
    global search_results, current_index
    results = search_results[call.from_user.id]
    
    current_index[call.from_user.id] = out_favorite_with_kb(bot, call, results, current_index[call.from_user.id])
    
    data = call.data 
    if data == "exit_favorite":
        search_results[call.from_user.id].clear()
        current_index[call.from_user.id] = 0
        main_hander.main_menu_handler(call, bot)
        return



# панель администратора

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "delete_db"
    )
)
def delete_handlers(callback_query):
    bot.send_message(callback_query.from_user.id, "За какую дату удалить историю?")
    bot.set_state(callback_query.from_user.id, UserState.delete_history)

@bot.message_handler(state=UserState.delete_history)
def delete_progress(message: Message):
    delete_handler.delete_start(bot, message)

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "my_data"
    )
)
def my_data(callback_query):
    bot.send_message(callback_query.from_user.id, 
                     f"Ник: {callback_query.from_user.username}"
                     f"\nИмя: {callback_query.from_user.first_name}"
                     f"\nФамилия: {callback_query.from_user.last_name}"
                     f"\nID: {callback_query.from_user.id}\n")

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "all_users"
    ) 
)
def all_users(callback_query):
    users_handler.all_users_handler(bot, callback_query)

@bot.callback_query_handler(
    func=lambda callback_query: (
        callback_query.data == "admin_panel"
    )
)
def admin_panel(callback_query):
    bot.edit_message_reply_markup(callback_query.from_user.id, callback_query.message.message_id)
    admin_panel_hendler.out_admin_panel_hendler(bot, callback_query)

# @bot.message_handler(commands=["test"])
# def test(message: Message):
#     movie = MovieCash.get_or_none(MovieCash.movie_id == 1)
#     bot.send_photo(message.from_user.id, photo=movie.movie_poster)

    