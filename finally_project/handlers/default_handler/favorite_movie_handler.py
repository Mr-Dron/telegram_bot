from loader import bot

from states.bot_state import UserState
from database.models import MovieCash
from keyboards.keyboards_output import go_to_output_favorite, output_favorite_kb
from keyboards.keyboards_menu import go_to_menu_kb

from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call:
    call.data == "favorite")
def favorite_movie(call):
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
        
