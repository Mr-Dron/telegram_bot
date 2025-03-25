from loader import bot

from telebot.types import CallbackQuery
from database.models import MovieCash

from keyboards.keyboards_output import go_to_output_favorite
from keyboards.keyboards_menu import go_to_menu_kb

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call:
    call.data == "favorite")
def favorite_movie(call: CallbackQuery) -> None:
    """Обрабатывает нажитие на кнопку с callback = favorite.
    Находит все фильмы с статусом "в списке желаемого" и отправляет на вывод

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий информацию пользователя
    """
    movies = MovieCash.select()
    
    result = [movie for movie in movies if movie.movie_viewed and movie.user.user_id == call.from_user.id]         
    
    if result == []:
        bot.send_message(call.from_user.id, "У вас нет избранных фильмов", reply_markup=go_to_menu_kb())
        return
    else:
        SEARCH_RESULTS[call.from_user.id] = result
        bot.send_message(call.from_user.id, 
                     f"В вашем списке желаемых фильмов\\: *__{len(SEARCH_RESULTS[call.from_user.id])}__*\n"
                     "Нажмите *далее* или *выйти*, чтобы продолжить\\.", 
                     reply_markup=go_to_output_favorite(), parse_mode="MarkdownV2")
    
        CURRENT_INDEX[call.from_user.id] = 0    
        
