import requests
import os

from database.models import User
from telebot.types import Message

RATING = dict()
BUDGET = dict()
GENRE = dict()

def find_movie_name(keyword: str, message: Message) -> list:
    """Поиск фильмов по ключевому слову в названии через API Kinopoisk

    Args:
        keyword (str): Ключевое слово или название
        message (Message): Обьект сообщения телеграм, содержащий информацию о пользователе

    Returns:
        list: Список с результатом поиска
    """
    url = "https://api.kinopoisk.dev/v1.4/movie/search"
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.environ.get("KINOPOISK_API_KEY")  
    }
    params = {
        "query": keyword,
        "limit": User.get(User.user_id == message.from_user.id).limit,
        "page": 1,
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None

def find_movie_rating(keyword: str, message: Message) -> list:
    """Поиск фильма по рейтингу через API Kinopoiska

    Args:
        keyword (str): рейтинг или диапозон рейтинга
        message (Message): Объект сообщения телеграм, содержащий информацию о пользователе

    Returns:
        list: результат поиска
    """
    url = "https://api.kinopoisk.dev/v1.4/movie"
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.environ.get("KINOPOISK_API_KEY")  
    }
    params = {
        "rating.kp": f"{keyword}",
        "limit": User.get(User.user_id == message.from_user.id).limit
    }
    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None


def all_genres() -> list:
    """Поиск всех доступных жанров фильма через API Kinopoisk

    Returns:
        list: Список всех жанров 
    """
    url = "https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name"

    headers = {
        "accept": "application/json",
        "X-API-KEY": "C2930HW-5JXMS89-HW29QP4-0C6TRAS"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        genres = [genre["name"] for genre in data]
        return genres
    else:
        print(f"Ошибка {response.status_code}")
        return None

def find_movie_by_genre(message: Message) -> list:
    """Поиск фильмов по жанру как основной параметр, рейтинг и бюджет 
    необязательные параметры и могут принимать значение None 

    Args:
        message (Message): Объект сообщения телеграм, содержащий информацию о пользователе

    Returns:
        list: Список результатов поиска
    """

    url = "https://api.kinopoisk.dev/v1.4/movie"

    headers = {
        "accept": "application/json",
        "X-API-KEY": "C2930HW-5JXMS89-HW29QP4-0C6TRAS"
    }
    params = {
        "genres.name": GENRE[message.from_user.id],
        "rating.kp": RATING[message.from_user.id],
        "budget.value": BUDGET[message.from_user.id],
        "limit": User.get(User.user_id == message.from_user.id).limit,
        "page": 4,
    }

    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None

    