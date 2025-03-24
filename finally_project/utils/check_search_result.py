
def check_search_result_start(results):
    processed_result = list()
    
    for movie in results:
        if check_result_name(movie):
            processed_result.append(movie)
    
    return processed_result

def check_result_name(movie):
    if "name" not in movie or movie["name"] == None:
        return False
    else:
        return check_result_poster(movie)

def check_result_description(movie):
    if "description" not in movie or movie["description"] == None:
        return False
    else:
        return check_result_poster(movie)

def check_result_poster(movie):
    if "poster" not in movie or movie["poster"] == None or "previewUrl" not in movie["poster"] or movie["poster"]["previewUrl"] == None:
        return False
    else:
        return True