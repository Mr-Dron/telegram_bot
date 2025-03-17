from states.bot_state import UserState
from telebot.types import Message
from utils.output_result import output_search
from utils.db_utils import save_movie_cash
from api.api_kinopoisk import find_movie_rating

def start_search(bot, message: Message):
    bot.send_message(message.from_user.id, "Введите минимальный рейтинг фильма")
    bot.set_state(message.from_user.id, UserState.search_by_rating)
 

def progress_search_by_rating(bot, message: Message): 
    bot.send_message(message.from_user.id, "Идет процесс поиска...")
    result = find_movie_rating(message.text) 

    
    save_movie_cash(message, result)
    bot.delete_state(message.from_user.id)

    return result
