from loader import bot
from states.bot_state import UserState
from telebot.types import Message
from database.models import User

from keyboards.keyboards_limit import try_set_limit
from keyboards.keyboards_menu import go_to_menu_kb


@bot.message_handler(commands=["limit"])
def limit_start(message: Message):
    bot.send_message(message.from_user.id, "*__Изменение лимита__*\n"
                     "Установите новое значение, сколько результатов выдавать на один поиск \\(1\\-250\\)\n"
                     "Сейчас у вас установлен лимит *__{}__*".format(User.get(User.user_id == message.from_user.id).limit),
                     parse_mode="MarkdownV2")
    
    bot.set_state(message.from_user.id, UserState.new_limit)
    
@bot.message_handler(state=UserState.new_limit)
def set_new_limit(message: Message):
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
    
    
    


@bot.callback_query_handler(func=lambda call:
    call.data == "try_again")
def try_set_new_limit(call):
    bot.send_message(call.from_user.id, "Введите новый лимит")
    bot.set_state(call.from_user.id, UserState.new_limit)