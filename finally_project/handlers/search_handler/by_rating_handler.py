from loader import bot

from states.bot_state import UserState
from telebot.types import Message, CallbackQuery

from utils.db_utils import save_movie_cash
from api.api_kinopoisk import find_movie_rating
from keyboards.keyboards_output import go_to_output_search
from keyboards.keyboards_menu import go_to_menu_kb
from utils.check_search_result import check_search_result_start

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS


@bot.callback_query_handler(func=lambda call:
    call.data == "search_rating")
def start_search(call: CallbackQuery) -> None:
    """Ловит нажатие на кнопку с callback = search_rating. Устанавливает состояние на поиск по рейтингу.
    Запрашивает у пользователя рейтинг или диапозон рейтинга фильма

    Args:
        call (CallbackQuery): Обьект нажатия, хранящий данные пользователя 
    """
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.set_state(call.from_user.id, UserState.search_by_rating)
    bot.send_message(call.from_user.id, "\t__*Поиск по рейтингу*__\n"
                     "Введите рейтинг фильма \\(пример\\: 7\\, 10\\, 7\\.2\\-10\\)\\.",
                     parse_mode="MarkdownV2")
 

@bot.message_handler(state=UserState.search_by_rating)
def progress_search_by_rating(message: Message) -> None: 
    """Ловит стояние поиска по рейтингу. Получает ответ от пользователя, отправляет запрос API Kinopoisk
    Получает ответ, отпраляет его на проверку наличия необходимых полей и полученный результат отправляет на вывод

    Args:
        message (Message): _description_
    """
    preliminary_result = find_movie_rating(message.text, message) 
    
    result = check_search_result_start(preliminary_result)
    
    if result == []:
        bot.send_message(message.from_user.id, "Результатов не найдено", reply_markup=go_to_menu_kb())
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
