from loader import bot
from telebot.types import CallbackQuery

from database.models import MovieCash
from utils.search_check import search_check
from keyboards.keyboards_output import output_search_kb, go_to_output_search

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call: call.data in 
                            ["next_movie_search",
                             "previous_movie_search",
                             "add_to_favorites",
                             "next_to_search_output"])
def main_output_search(call: CallbackQuery):
    """Вывод результата поиска по-одному фильму с клавиатурой

    Args:
        call (CallbackQuery): Обьект нажатия на клавиатуру, хранящий данные пользователя
    """

    results = SEARCH_RESULTS[call.from_user.id]
    data = call.data
    if data == "add_to_favorites":
        fav_movie = MovieCash.get(MovieCash.movie_id == results[CURRENT_INDEX[call.from_user.id]]["id"])
        if fav_movie.movie_viewed:
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.from_user.id, '"{}" уже добавлен в избранное'.format(results[CURRENT_INDEX[call.from_user.id]]["name"]),
                             reply_markup=go_to_output_search())
            return
        else:
            fav_movie.movie_viewed = True
            fav_movie.save()
            bot.send_message(call.from_user.id, '"{}" добавлен в избранные'.format(
                results[CURRENT_INDEX[call.from_user.id]]["name"]
            ))

    CURRENT_INDEX[call.from_user.id] = correct_kb(call, results, CURRENT_INDEX[call.from_user.id])


def correct_kb(call: CallbackQuery, results: list, current_index: int) -> int:
    """Обновление текущего индекса, в зависимости от нажатия кнопки

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий данные пользователя
        results (list): Список результатов поиска
        current_index (int): Текущий индекс

    Returns:
        int: обнавленный индекс
    """
    data = call.data    
    
    if data == "previous_movie_search":
        current_index -= 1
    elif data == "next_movie_search":
        current_index += 1
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_search(call, results[current_index], 
                  current_index, len(SEARCH_RESULTS[call.from_user.id]))
    
    return current_index

def output_search(call: CallbackQuery, result: dict, current_index: int, length_result: int) -> None:
    """Вывод фильм под текущим индексом в списке результатов поиска, реализованный через Пагинацию

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий данные пользователя
        result (dict): Информаци о фильме под текущим индексом
        current_index (int): Текущий индекс
        length_result (int): Длинна списка результатов поиска
    """
        
    res = search_check(result) 
    if ("poster" in result) and (result["poster"]["previewUrl"] != ""):
        try:
            bot.send_photo(call.from_user.id, photo=result["poster"]["previewUrl"], caption=res, 
                           parse_mode="MarkdownV2", reply_markup=output_search_kb(current_index, length_result))
        except Exception as exc:
            bot.send_message(call.from_user.id, res, parse_mode="MarkdownV2",
                         reply_markup=output_search_kb(current_index, length_result))
    else:       
        bot.send_message(call.from_user.id, res, parse_mode="MarkdownV2",
                         reply_markup=output_search_kb(current_index, length_result))
