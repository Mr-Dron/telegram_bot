from loader import bot
from telebot.types import CallbackQuery

from database.models import MovieCash
from keyboards.keyboards_output import output_favorite_kb
from keyboards.keyboards_menu import go_to_menu_kb
from utils.search_check import history_check

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie_favorite",
                             "previous_movie_favorite",
                             "remove_from_favorites",
                             "next_to_favorite_output"])
def main_output_favorite(call: CallbackQuery):
    """Вывод результата поиска через реализацию пагинации

    Args:
        call(CallbackQuery): Нажатие на кнопки клавиатуры с определенным callback
    """

    results = SEARCH_RESULTS[call.from_user.id]
    data = call.data
    if data == "remove_from_favorites":
        fav_movie = MovieCash.get(MovieCash.movie_id == results[CURRENT_INDEX[call.from_user.id]].movie_id)
        fav_movie.movie_viewed = False
        fav_movie.save()
        bot.send_message(call.from_user.id, '"{}" Удален из избранного'.format(
            results[CURRENT_INDEX[call.from_user.id]].movie_name
        ))
        if len(results) == 1:
            bot.send_message(call.from_user.id, "Ваш список желаемых фильмов пуст", reply_markup=go_to_menu_kb)
        elif CURRENT_INDEX[call.from_user.id] == len(results) - 1:
            CURRENT_INDEX[call.from_user.id] -= 1
        results.remove(fav_movie)

    CURRENT_INDEX[call.from_user.id] = correct_kb(call, results, CURRENT_INDEX[call.from_user.id])


def correct_kb(call: CallbackQuery, results: list, current_index: int) -> int:
    """Коррекция индекса текущего фильма при навигации по списку

    Args:
        call (CallbackQuery): Обьект, содержащий информаци о нажатии на кнопку
        results (list): Список результатов поиска
        current_index (int): Текущий индекс фильма

    Returns:
        int: Обнавленный индекс
    """
    data = call.data    
    
    if data == "previous_movie_favorite":
        current_index -= 1
    elif data == "next_movie_favorite":
        current_index += 1
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_search(call, results[current_index], 
                  current_index, len(SEARCH_RESULTS[call.from_user.id]))
    
    return current_index

def output_search(call: CallbackQuery, result: MovieCash, current_index: int, length_result: int):
    """Вывод фильма с текущим индексом

    Args:
        call (CallbackQuery): Объект, хранящий информацию о нажатии на кнопку
        result (MovieCash): Обьект базы данных, фильм для вывода
        current_index (int): Текущий индекс
        length_result (int): Длинна списка результатов
    """
    res = history_check(result)
    
    try:
        bot.send_photo(call.from_user.id, photo=result.movie_poster, 
                   caption=res, parse_mode="MarkdownV2", reply_markup=output_favorite_kb(current_index, length_result))
    except Exception as exc:
        bot.send_message(call.from_user.id, res, parse_mode="MarkdownV2", reply_markup=output_favorite_kb(current_index, length_result))

