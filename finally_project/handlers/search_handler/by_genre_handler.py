from loader import bot
from states.bot_state import UserState
from telebot.types import CallbackQuery

from api.api_kinopoisk import all_genres, find_movie_by_genre
from utils.db_utils import save_movie_cash
from utils.check_search_result import check_search_result_start

from keyboards.keyboards_genre import genres_kb, go_to_output_kb
from keyboards.keyboards_menu import go_to_menu_kb

from api.api_kinopoisk import RATING, BUDGET, GENRE
from config_data.config import CURRENT_INDEX, SEARCH_RESULTS


@bot.callback_query_handler(func=lambda call:
    call.data == "search_genre")
def start_search(call: CallbackQuery) -> None:
    """Обрабатывает нажатие на кнопку с callback = search_genre.
    Осуществляет поиск по жанру. Делает запрос и получает все жанры. Запрашивает у пользовалетя 1 жанр
    И обьявляет новое состояние на добавление дополнительных параметров

    Args:
        call (CallbackQuery): Обьект нажатия, хранящий данные пользователя 
    """
    
    genres = all_genres()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.set_state(call.from_user.id, UserState.add_additional_filters)
    RATING[call.from_user.id] = None
    BUDGET[call.from_user.id] = None
    GENRE[call.from_user.id] = None
    
    bot.send_message(call.from_user.id, "\t__*Поиск по жанру*__\n"
                     "Выберите желаемый жанр\\.",
                     parse_mode="MarkdownV2", reply_markup=genres_kb(genres))
    
@bot.callback_query_handler(func=lambda call:
    call.data == "continue_output")
def search_by_genre(call: CallbackQuery) -> None:
    """Ловит нажатие на кнопку с callback = continue_output. Получает результат запроса API Kinopisk
    Проводит проверку на наличие необходимых полей и финальный список отправляет на вывод

    Args:
        call (CallbackQuery): Обьект нажатия, хранящий данные пользователя 
    """
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    preliminary_result = []
    preliminary_result = find_movie_by_genre(call)
    
    result = check_search_result_start(preliminary_result)
    
    if result == []:
        bot.send_message(call.from_user.id, "Результатов не найдено", reply_markup=go_to_menu_kb())
        bot.delete_state(call.from_user.id)
    else:
        save_movie_cash(call, result)
        bot.delete_state(call.from_user.id)
        SEARCH_RESULTS[call.from_user.id] = result
        
        bot.send_message(call.from_user.id, 
                     f"По вашему запросу найдено фильмов\\: *__{len(SEARCH_RESULTS[call.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=go_to_output_kb(), parse_mode="MarkdownV2")
    
        CURRENT_INDEX[call.from_user.id] = 0