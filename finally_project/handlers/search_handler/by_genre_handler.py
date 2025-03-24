from loader import bot
from states.bot_state import UserState

from api.api_kinopoisk import all_genres, find_movie_by_genre
from utils.db_utils import save_movie_cash
from utils.check_search_result import check_search_result_start

from keyboards.keyboards_genre import genres_kb, go_to_output_kb
from keyboards.keyboards_additional import additional_filter_kb, add_additional_or_continue_output
from keyboards.keyboards_menu import go_to_menu_kb

from api.api_kinopoisk import RATING, BUDGET, GENRE
from config_data.config import CURRENT_INDEX, SEARCH_RESULTS


@bot.callback_query_handler(func=lambda call:
    call.data == "search_genre")
def start_search(call):
    
    genres = all_genres()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.set_state(call.from_user.id, UserState.add_additional_filters)
    RATING[call.from_user.id] = None
    BUDGET[call.from_user.id] = None
    GENRE[call.from_user.id] = None
    
    bot.send_message(call.from_user.id, "\t__*Поиск по жанру*__\n"
                     "Выберите желаемый жанр\\.",
                     parse_mode="MarkdownV2", reply_markup=genres_kb(genres))

# @bot.message_handler(state=UserState.add_additional_filters)
# def add_additional_filter(message):
#     GENRE[message.from_user.id] = message.text
#     bot.send_message(message.from_user.id, "Идет процесс поиска...", reply_markup=add_additional_or_continue_output())


# @bot.callback_query_handler(func=lambda call:
#     call.data == "additional_filter")
# def add_addetional_filter(call):
#     bot.delete_state(call.from_user.id)
#     bot.delete_message(call.message.chat.id, call.message.message_id)
#     bot.send_message(call.from_user.id, "*__Добавление дополнительных фильтров__*\n"
#                      "Здесь вы можете добавить дополнительные фильтры для более точного поиска фильма, под ваши предпочтения", 
#                      parse_mode="MarkdownV2", reply_markup=additional_filter_kb())

# @bot.callback_query_handler(func=lambda call:
#     call.data == "filter_rating")
# def add_rating_filter(call):
#     bot.delete_message(call.message.chat.id, call.message.message_id)
#     if GENRE[call.from_user.id] == None:
#         bot.send_message(call.from_user.id, "Введите рейтинг фильма (пример: 7, 10, 7.2-10).")
#     else:
#         bot.send_message(call.from_user.id, 'У вас уже установлен дополнительный фильтр \\"*_рейтинг_*\\"\\: {}\n'
#                          'Введите рейтинг фильма \\(пример\\: 7\\, 10\\, 7\\.2\\-10\\)\\.'.format(GENRE[call.from_user.id]),
#                          parse_mode="MarkdownV2")
#     bot.set_state(call.from_user.id, UserState.add_additional_rating)


# @bot.message_handler(state=UserState.add_additional_rating)
# def data_verification(message):
    
#     bot.delete_state(message.from_user.id)
#     RATING[message.from_user.id] = message.text
#     bot.send_message(message.from_user.id, "Добавлен фильтр по рейтингу", reply_markup=add_additional_or_continue_output())
    
    
    
# @bot.callback_query_handler(func=lambda call:
#     call.data == "filter_budget")
# def add_rating_filter(call):
#     bot.delete_message(call.message.chat.id, call.message.message_id)
#     if GENRE[call.from_user.id] == None:
#         bot.send_message(call.from_user.id, "Введите бюджет фильма (1000 - 6.000.000).")
#     else:
#         bot.send_message(call.from_user.id, 'У вас уже установлен дополнительный фильтр \\"*_бюджет_*\\"\\: {}\n'
#                          'Введите бюджет фильма \\(1000 \\- 6\\.000\\.000\\)\\.'.format(GENRE[call.from_user.id]),
#                          parse_mode="MarkdownV2")
#     bot.set_state(call.from_user.id, UserState.add_additional_budget)


# @bot.message_handler(state=UserState.add_additional_budget)
# def data_verification(message):
    
#     bot.delete_state(message.from_user.id)
#     BUDGET[message.from_user.id] = message.text
#     bot.delete_message(message.chat.id, message.message_id)
#     bot.send_message(message.from_user.id, "Добавлен фильтр по бюджету фильма", reply_markup=add_additional_or_continue_output())
    
    
@bot.callback_query_handler(func=lambda call:
    call.data == "continue_output")
def search_by_genre(call):
    
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