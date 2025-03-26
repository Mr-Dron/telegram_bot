from loader import bot
from states.bot_state import UserState
from telebot.types import Message, CallbackQuery
from database.models import User

from keyboards.keyboards_limit import try_set_limit
from keyboards.keyboards_menu import go_to_menu_kb


@bot.message_handler(commands=["limit"])
def limit_start(message: Message) -> None:
    """Обработчик команды limit. Для изменения лимита выводимых результатов поиска

    Args:
        message (Message): Объект сообщения телеграм, хранящий информацию пользователя 
    """
    bot.send_message(message.from_user.id, "*__Изменение лимита__*\n"
                     "Установите новое значение, сколько результатов выдавать на один поиск \\(1\\-250\\)\n"
                     "Сейчас у вас установлен лимит *__{}__*".format(User.get(User.user_id == message.from_user.id).limit),
                     parse_mode="MarkdownV2")
    
    bot.set_state(message.from_user.id, UserState.new_limit)
    
@bot.message_handler(state=UserState.new_limit)
def set_new_limit(message: Message) -> None:
    """Ловит состояние изменения лимита, обрабатывает исключения невозможного лимита или выхода за пределы.
    Сохраняет новый лимит

    Args:
        message (Message): Объект сообщения телеграм, хранящий информацию о пользователе

    Raises:
        Exception: Принудительный вызов исключения, если введенное сообщение выходит за пределы допустимых значений 
    """
    try:
        new_limit = int(message.text)
        if 250 < new_limit or new_limit < 1:
            raise Exception
    except Exception as exc:
        bot.delete_state(message.from_user.id)
        bot.send_message(message.from_user.id, "*__Ошибка ввода__*\n"
                         "Число должно быть целым и в диапазоне от 1 до 250", 
                         parse_mode="MarkdownV2", reply_markup=try_set_limit())
        return
    
    user = User.get(User.user_id == message.from_user.id)
    user.limit = message.text
    user.save()
    bot.send_message(message.from_user.id, "Лимит изменен на {}".format(user.limit), reply_markup=go_to_menu_kb())
    bot.delete_state(message.from_user.id )
    
    
    


@bot.callback_query_handler(func=lambda call:
    call.data == "try_again")
def try_set_new_limit(call: CallbackQuery) -> None:
    """Обработка случая ошибки ввода или выхода за пределы

    Args:
        call (CallbackQuery): Обьект нажатия на кнопку, хранящий информацию о пользователе
    """
    bot.send_message(call.from_user.id, "Введите новый лимит")
    bot.set_state(call.from_user.id, UserState.new_limit)