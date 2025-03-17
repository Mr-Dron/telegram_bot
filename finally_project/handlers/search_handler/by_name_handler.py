from states.bot_state import UserState
from telebot.types import Message
from api.api_kinopoisk import find_movie_name
from utils.db_utils import save_movie_cash
 
 
def start_search(bot, message: Message):
    bot.set_state(message.from_user.id, UserState.search_by_name)
    bot.send_message(message.from_user.id, "Введите название фильма")


def progress_search(bot, message: Message):
    # bot.send_message(message.from_user.id, "Произвожу поиск...") 
    result = find_movie_name(message.text)
    
    # exact_search = [movie for movie in result if movie["name"].lower() == message.text.lower()]
    # similar_movie = [movie for movie in result if movie["name"].lower() != message.text.lower()]
    
    # search_results = [exact_search, similar_movie]
    
    if result == []:
        bot.send_message(message.from_user.id, "Результатов не найдено")
        return []
    else:
        save_movie_cash(message, result)
        bot.delete_state(message.from_user.id)
        return result
        
    

    
        

