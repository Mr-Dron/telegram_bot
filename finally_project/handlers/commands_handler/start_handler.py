from loader import bot
from telebot.types import Message
from database.models import User
from utils.db_utils import new_user
from keyboards.keyboards_menu import main_keyboard, main_keyboard_admin

@bot.message_handler(commands=["start"])
def bot_start(message: Message) -> None:
    
    user = User.get_or_none(User.user_id == message.from_user.id)
    
    if user == None:
        new_user(message)
        user = User.get_or_none(User.user_id == message.from_user.id)
        if user.admin:
            bot.send_message(message.from_user.id, "Добро пожаловать администратор!",
                             reply_markup=main_keyboard_admin())
        else:
            bot.send_message(message.from_user.id, f"{message.from_user.first_name}! Добро пожаловать.\nЯ первый полноценный бот."
                         " Меня создали для поиска фильмов по различным фильтрам.\nТак как я еще сырой, все предложения "
                         "и идеи по улучшению функционала можете отправлять моему создателю @Rusya352",
                         reply_markup=main_keyboard())
    else:
        if user.admin:
            bot.send_message(message.from_user.id, "Рад снова вас видеть, администратор",
                             reply_markup=main_keyboard_admin(), parse_mode="MarkdownV2")
        else:
            bot.send_message(message.from_user.id, f"Рад снова тебя видеть {message.from_user.first_name}!",
                         reply_markup=main_keyboard())