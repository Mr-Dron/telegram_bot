from loader import bot
from telebot.types import CallbackQuery

from database.models import MovieCash
from keyboards.keyboards_output import output_history_kb, go_to_output_hisoty
from utils.search_check import history_check

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie_history",
                             "previous_movie_history",
                             "add_to_favorites_history",
                             "next_to_history_output"])
def main_output_history(call: CallbackQuery):
    """Вывод результата поиска по-одному фильму с клавиатурой

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий данные пользователя
    """

    results = SEARCH_RESULTS[call.from_user.id]
    data = call.data
    if data == "add_to_favorites_history":
        fav_movie = MovieCash.get(MovieCash.movie_id == results[CURRENT_INDEX[call.from_user.id]].movie_id)
        if fav_movie.movie_viewed:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.from_user.id, '"{}" уже добавлен в избранное'.format(results[CURRENT_INDEX[call.from_user.id]].movie_name),
                             reply_markup=go_to_output_hisoty())
            return
        else:
            fav_movie.movie_viewed = True
            fav_movie.save()
            bot.send_message(call.from_user.id, '"{}" добавлен в избранные'.format(
                results[CURRENT_INDEX[call.from_user.id]].movie_name
            ))

    CURRENT_INDEX[call.from_user.id] = correct_kb(call, results, CURRENT_INDEX[call.from_user.id])


def correct_kb(call: CallbackQuery, results: list, current_index: int) -> int:
    """Коррекция текущего символа, в зависимости от нажатия кнопки 

    Args:
        call (CallbackQuery): Обьект нажатия кнопки, хранящий данные пользователя 
        results (list): Список результатов поиска
        current_index (int): Текущий символ

    Returns:
        int: Обнавленный индекс
    """
    data = call.data    
    
    if data == "previous_movie_history":
        current_index -= 1
    elif data == "next_movie_history":
        current_index += 1
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_search(call, results[current_index], 
                  current_index, len(SEARCH_RESULTS[call.from_user.id]))
    
    return current_index

def output_search(call: CallbackQuery, result: dict, current_index: int, length_result: int) -> None:
    """Вывод фильма под текущим индексом в списке результатов поиска

    Args:
        call (CallbackQuery): Обект нажатия на кнопка, хранящий данные пользователя
        result (dict): Информация о фильме под текущим индексом
        current_index (int): Текущий индекс
        length_result (int): Длинна списка с результатом поиска
    """
        
    res = history_check(result)
    
    try:
        bot.send_photo(call.from_user.id, photo=result.movie_poster, 
                   caption=res, parse_mode="MarkdownV2", reply_markup=output_history_kb(current_index, length_result))
    except Exception as exc:
        bot.send_message(call.from_user.id, res, parse_mode="MarkdownV2", reply_markup=output_history_kb(current_index, length_result))

