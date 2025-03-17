import requests
import os

def find_movie_name(keyword: str):
    url = "https://api.kinopoisk.dev/v1.4/movie/search"
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.environ.get("KINOPOISK_API_KEY")  
    }
    params = {
        "query": keyword,
        "limit": 10
    }
    
    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None

def find_movie_rating(keyword: str):
    url = "https://api.kinopoisk.dev/v1.4/movie"
    headers = {
        "accept": "application/json",
        "X-API-KEY": os.environ.get("KINOPOISK_API_KEY")  
    }
    params = {
        "rating.kp": f"{keyword}-10",
        "limit": 10,
    }
    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None


def all_genres():
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

def find_movie_by_genre(genre):
    import requests

    url = "https://api.kinopoisk.dev/v1.4/movie"

    headers = {
        "accept": "application/json",
        "X-API-KEY": "C2930HW-5JXMS89-HW29QP4-0C6TRAS"
    }
    params = {
        "genres.name": genre,
        "limit": 10
    }

    response = requests.get(url, headers=headers, params=params)
    response.encoding = "utf-8"
    
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])
    else:
        print(f"Ошибка {response.status_code}")
        return None

    