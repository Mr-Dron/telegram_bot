from loader import bot
from keyboards.keyboards_help import help_keyboad
from telebot.types import Message

@bot.message_handler(commands=["help"])
def start_help(message: Message) -> None:
    """Обработчик комманды help

    Args:
        message (Message): Объект сообщения телеграм, хранящий информацию
    """
    bot.send_message(message.from_user.id, "Я тестовый помощник в использовании этого бота\n"
                     "На данный момент бот умеет искать фильмы по названию\\, рейтингу, жанру\\.\n"
                     "Нажми на кнопку *Меню*\\, выбери подходящий фильтр и найди фильм для приятного времяпровождения\\!", 
                     parse_mode="MarkdownV2", reply_markup=help_keyboad()) 