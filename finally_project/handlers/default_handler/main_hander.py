from keyboards.keyboards import main_keyboard

def main_menu_handler(message, bot):
    bot.send_message(message.from_user.id, "Приступайте к просмотру найденных фильмов или выберите действие, чтобы найти новый.", reply_markup=main_keyboard())