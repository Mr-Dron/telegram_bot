from telebot.types import Message
from database.models import MovieCash

def find_date_serach(message: Message) -> list:
    """Находит все различные даты истории поиска

    Args:
        message (Message): Обьект сообщения, хранящий данные пользователя

    Returns:
        list: Список всех различных дат
    """
    movie_cash = MovieCash.select()
    date_cash = list()
    
    for movie in movie_cash:
        if (message.from_user.id == movie.user.user_id) and str(movie.date_add) not in date_cash:
            date_cash.append(str(movie.date_add))
    
    date_cash.reverse()
    return date_cash