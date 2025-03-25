from loader import bot

from database.models import MovieCash
from states.bot_state import UserState
from telebot.types import Message, CallbackQuery

from utils.history_date import find_date_serach
from keyboards.keyboards_menu import go_to_menu_kb
from keyboards.keyboards_history import date_keyboard
from keyboards.keyboards_output import go_to_output_hisoty

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS


@bot.callback_query_handler(func=lambda call:
    call.data == "history")
def start_history_hendler(call: CallbackQuery) -> None:
    """Обрабатывает нажитие на кнопку с callback = history.
    Запрашивает дату, за которую нужна история и переводит в состояние истории 

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий данные пользователя
    """
    history_date = find_date_serach(call)
    if history_date == []:
        bot.set_state(call.from_user.id, UserState.main)
        bot.send_message(call.from_user.id, "У вас еще нет истории поиска\nВернуься в меню?",
                         reply_markup = go_to_menu_kb())

    else:
        bot.send_message(call.from_user.id, "За какую дату смотреть историю поиска?",
                     reply_markup=date_keyboard(history_date))
    
        bot.set_state(call.from_user.id, UserState.history)
        

@bot.message_handler(state=UserState.history)
def history_progress(message: Message) -> None:
    """Ловит состояние history, начинает поиск фильмов в БД по заданной дате. 
    Собирает в один список и отправляет на вывод

    Args:
        message (Message): Обьект сообщения, хранящий данные пользователя
    """
    
    history = MovieCash.select()
    movies = [mov for mov in history if str(mov.date_add) == message.text and message.from_user.id == mov.user.user_id]
    if movies == []:
        bot.delete_state(message.from_user.id) 
        bot.send_message(message.from_user.id, "Истории за эту дату нет", reply_markup=go_to_menu_kb())
        return
    else:
        SEARCH_RESULTS[message.from_user.id] = movies
        bot.send_message(message.from_user.id, f"Найдено фильмов\\: *__{len(SEARCH_RESULTS[message.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=go_to_output_hisoty(), parse_mode="MarkdownV2")
    
        CURRENT_INDEX[message.from_user.id] = 0
        bot.delete_state(message.from_user.id) 

    
    
