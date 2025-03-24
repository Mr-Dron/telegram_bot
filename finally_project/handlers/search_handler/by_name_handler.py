from loader import bot
from states.bot_state import UserState
from telebot.types import Message

from api.api_kinopoisk import find_movie_name
from utils.db_utils import save_movie_cash
from keyboards.keyboards_output import go_to_output_search
from utils.check_search_result import check_search_result_start
from keyboards.keyboards_menu import go_to_menu_kb

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS
 
@bot.callback_query_handler(func=lambda call: 
    call.data == "search_name") 
def start_search(call: Message):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.set_state(call.from_user.id, UserState.search_by_name)
    bot.send_message(call.from_user.id, "\t__*Поиск по названию*__\n"
                     "Введите название фильма или часть названия фильма\\.",
                     parse_mode="MarkdownV2")


@bot.message_handler(state=UserState.search_by_name)
def progress_search(message: Message):
    preliminary_result = find_movie_name(message.text, message)
    
    result = check_search_result_start(preliminary_result)
    
    if result == []:
        bot.send_message(message.from_user.id, "Результатов не найдено", reply_markup=go_to_menu_kb())
        SEARCH_RESULTS[message.from_user.id] = []
        bot.delete_state(message.from_user.id)
    else:
        save_movie_cash(message, result)
        bot.delete_state(message.from_user.id)
        SEARCH_RESULTS[message.from_user.id] = result
        
        bot.send_message(message.from_user.id, 
                     f"По вашему запросу найдено фильмов\\: *__{len(SEARCH_RESULTS[message.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=go_to_output_search(), parse_mode="MarkdownV2")
    
        CURRENT_INDEX[message.from_user.id] = 0
        
    

    
        

