from loader import bot

from keyboards.keyboards_menu import main_keyboard
from config_data.config import CURRENT_INDEX, SEARCH_RESULTS

@bot.callback_query_handler(func=lambda call: 
    call.data in ["exit_output",
                  "menu",
                  "exit_to_menu"])
def main_menu_handler(call):
    CURRENT_INDEX[call.from_user.id] = 0
    try:
        SEARCH_RESULTS[call.from_user.id].clear()
    except Exception as exc:
        SEARCH_RESULTS[call.from_user.id] = list()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, "Приступайте к просмотру найденных фильмов или выберите действие, чтобы найти новый.", reply_markup=main_keyboard())