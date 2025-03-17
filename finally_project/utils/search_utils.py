# from states.bot_state import UserState
# from telebot.types import Message
# from . import output_result
# from utils.db_utils import save_movie_cash
# from api.api_kinopoisk import find_movie_name

# def search_by_name(user_id) -> None: 
#     bot.send_message(user_id, "Введите название фильма")
    
    
# @bot.message_handler(state=UserState.search_by_name)
# def search_movie(message: Message):
#     bot.send_message(message.from_user.id, "Состояние изменено. Произвожу поиск")
#     result = find_movie_name(message.text)
    
#     finally_result = [movie for movie in result if movie["name"].lower() == message.text.lower()]
    
#     if finally_result == []:
#         bot.send_message(message.from_user.id, "Результатов не найдено")
    
#     output_result(message.from_user.id, finally_result)    
#     save_movie_cash(finally_result)
 

# def search_by_rating(user_id) -> None:
#     bot.send_message(user_id, "Введите минимальный рейтинг фильма")
#     bot.set_state(user_id, UserState.search_by_rating)

# @bot.message_handler(state=UserState.search_by_rating)
# def search_movie(message: Message):
#     from api.api_kinopoisk import find_movie_rating
#     result = find_movie_rating(message.text)

#     output_result(message.from_user.id, result)

#     from utils.db_utils import save_movie_cash
#     save_movie_cash(result)


# def history_search(user_id) -> None:
#     bot.send_message(user_id, "За какую дату смотреть историю поиска?")
#     bot.set_state(user_id, UserState.history)
    

