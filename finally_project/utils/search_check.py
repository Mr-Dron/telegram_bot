from .escape_markdown import escape_markdow

def history_check(result):
    find_key = [result.cash_id, result.movie_name, result.movie_description, result.movie_rating, 
                result.movie_year, result.movie_genre, result.movie_age_rating, result.date_add]
    
    result_key = {result.cash_id: "ID фильма", result.movie_name: "Название", 
                  result.movie_description: "Описание", result.movie_rating: "Рейтинг", 
                  result.movie_year: "Год", result.movie_genre: "Жанр", 
                  result.movie_age_rating: "Возростной рейтинг", result.date_add: "Дата добавления"}    
    
    result_dict = dict()
    
    for key in find_key:
        if key is not None and key != "":
            result_dict[result_key[key]] = escape_markdow(str(key))
    
    return prepation_for_out(result_dict)
    
    

def search_check(result):
    find_key = ["name", "description", "rating", "year", "genres", "ageRating"]
    result_key = {"name": "Название", "description": "Описание", "rating": "Рейтинг", 
                  "year": "Год", "genres": "Жанр", "ageRating": "Возростной рейтинг"}
    
    result_dict = dict()
    for key, value in result.items():
        if key in find_key and value is not None and value != "":
            if isinstance(value, dict):
                result_dict[result_key[key]] = escape_markdow(str(search_check_dict(value)))
            elif isinstance(value, list):
                result_dict[result_key[key]] = escape_markdow(str(search_check_list(value)))
            else:
                result_dict[result_key[key]] = escape_markdow(str(value))
    
    return prepation_for_out(result_dict)


def search_check_dict(data):
    find_keys = ["kp", "url"]
    for key, value in data.items():
        if key in find_keys:
            return value 

def search_check_list(data):
    return ", ".join([genre for genre_dict in data for genre in genre_dict.values()])

def prepation_for_out(result_dict):
    result_list = list()
    for key, value in result_dict.items():
        if key == "Описание":
            result_list.append(f"\n*{key}*: _{value}_\n")
        elif key == "Возростной рейтинг":
            result_list.append(f"*{key}*: *__{value}\\+__*")
        else:
            result_list.append(f"*{key}*: {value}")
    
    return "\n".join(result_list)