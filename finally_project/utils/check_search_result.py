
def check_search_result_start(results: list) -> list:
    """Принимает список всех результатов поиска, пропускает через цикл, для проверки наличия необходимых полей

    Args:
        results (list): Список результатов поиска

    Returns:
        list: Проверенный список
    """
    processed_result = list()
    
    for movie in results:
        if check_result_name(movie):
            processed_result.append(movie)
    
    return processed_result

def check_result_name(movie: dict) -> bool:
    """Проверяет, есть ли в фильме название

    Args:
        movie (dict): Информация о фильме

    Returns:
        bool: Если названия в результате нет False, иначе переход к проверке следующего поля
    """
    if "name" not in movie or movie["name"] == None:
        return False
    else:
        return check_result_poster(movie)

# def check_result_description(movie):
#     if "description" not in movie or movie["description"] == None:
#         return False
#     else:
#         return check_result_poster(movie)

def check_result_poster(movie: dict) -> bool:
    """Проверяет, есть ли в фильме постер

    Args:
        movie (dict): Информация о фильме

    Returns:
        bool: Если ссылки на постер в результате нет False, иначе True
    """
    if "poster" not in movie or movie["poster"] == None or "previewUrl" not in movie["poster"] or movie["poster"]["previewUrl"] == None:
        return False
    else:
        return True