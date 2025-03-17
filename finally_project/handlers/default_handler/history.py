from database.models import MovieCash
from states.bot_state import UserState
from telebot.types import Message, ReplyKeyboardRemove
from utils.history_date import find_date_serach
from keyboards.keyboards import history_keyboard, go_to_main_keyboard

def start_history_hendler(bot, message: Message):
    history_date = find_date_serach(message)
    if history_date == []:
        bot.set_state(message.from_user.id, UserState.main)
        bot.send_message(message.from_user.id, "У вас еще нет истории поиска\nВернуься в меню?",
                         reply_markup = go_to_main_keyboard())

    else:
        bot.send_message(message.from_user.id, "За какую дату смотреть историю поиска?",
                     reply_markup=history_keyboard(history_date))
    
        bot.set_state(message.from_user.id, UserState.history)

def history_progress(bot, message: Message):
    
    history = MovieCash.select()
    movies = [mov for mov in history if str(mov.date_add) == message.text and message.from_user.id == mov.user.user_id]
    if movies == []:
        bot.send_message(message.from_user.id, "Истории за эту дату нет", reply_markup=ReplyKeyboardRemove())
        bot.delete_state(message.from_user.id) 
        return []
    else:
        bot.delete_state(message.from_user.id) 
        return movies
    
    
