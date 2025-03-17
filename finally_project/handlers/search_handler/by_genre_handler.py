from api.api_kinopoisk import all_genres, find_movie_by_genre
from utils.db_utils import save_movie_cash
from keyboards.keyboards import genres_kb
import json

def start_search(message, bot):
    genres = all_genres()
    bot.send_message(message.from_user.id, "Выберите желаемый жанр", reply_markup=genres_kb(genres))
    


def search_by_genre(message, bot):
    result = []
    result = find_movie_by_genre(message.text)
    
    if result == []:
        bot.send_message(message.from_user.id, "Результатов не найдено")
        return []
    else:
        save_movie_cash(message, result)
        bot.delete_state(message.from_user.id)
        return result 