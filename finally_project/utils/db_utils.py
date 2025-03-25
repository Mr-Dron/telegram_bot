from telebot.types import Message
from database.models import MovieCash, User
from datetime import datetime
from peewee import IntegrityError

 
def save_movie_cash(message: Message, result: list) -> None:
    """Принимает список результатов поиска, прогоняет каждый фильм, выбирает нужные поля, заполняет
    новый словарь и сохраняет результат с нужными полями в БД

    Args:
        message (Message): Обьект сообщения, хранящее данные о пользователе
        result (list): Список результатов
    """
    for res in result:
        find_key = ["id", "name", "description", "rating", "year", "genres", "ageRating", "poster"]
        result_dict = {"id": None,
                       "name": None,
                       "description": None,
                       "rating": None,
                       "year": None,
                       "genres": None,
                       "ageRating": None,
                       "poster": None}
        
        for key, value in res.items():
            if key in find_key:
                if key == "poster":
                    result_dict[key] = value["previewUrl"]
                else:
                    result_dict[key] = value
                
        movie = MovieCash(user = message.from_user.id,
                          movie_id = result_dict["id"],
                          movie_name = result_dict["name"],
                          movie_description = result_dict["description"],
                          movie_rating = result_dict["rating"]["kp"],
                          movie_year = result_dict["year"],
                          movie_genre = ", ".join([genre for genre_dict in result_dict["genres"] for genre in genre_dict.values()]),
                          movie_age_rating = result_dict["ageRating"],
                          movie_poster = result_dict["poster"],    
                          date_add = datetime.today(),
                          movie_viewed = False) 
            
        movie.save()

def new_user(message: Message) -> bool:
    """Пробует создать нового пользователя, если в БД нету, то создает нового и возвращает True(пользователь был создан)

    Args:
        message (Message): Обьект сообщения, хранящий данные о пользователе

    Returns:
        bool: Статус создания нового пользователя. True пользователь создан, False пользователь уже существует
    """
    user_id = message.from_user.id 
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    
    try:
        if user_id == 567301066:
            User.create(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                admin = True,
                limit = 10,
            )
        else:
            User.create(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                admin = False,
                limit = 10,
            )
        return True
    except IntegrityError:
        return False
        