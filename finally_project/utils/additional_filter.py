from loader import bot
from states.bot_state import UserState

from keyboards.keyboards_additional import add_additional_or_continue_output, additional_filter_kb

from api.api_kinopoisk import GENRE, RATING, BUDGET


@bot.message_handler(state=UserState.add_additional_filters)
def add_additional_filter(message):
    GENRE[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, "Идет процесс поиска...", reply_markup=add_additional_or_continue_output())

@bot.callback_query_handler(func=lambda call:
    call.data == "additional_filter")
def add_addetional_filter(call):
    bot.delete_state(call.from_user.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.from_user.id, "*__Добавление дополнительных фильтров__*\n"
                     "Здесь вы можете добавить дополнительные фильтры для более точного поиска фильма, под ваши предпочтения", 
                     parse_mode="MarkdownV2", reply_markup=additional_filter_kb())

@bot.callback_query_handler(func=lambda call:
    call.data == "filter_rating")
def add_rating_filter(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if GENRE[call.from_user.id] == None:
        bot.send_message(call.from_user.id, "Введите рейтинг фильма (пример: 7, 10, 7.2-10).")
    else:
        bot.send_message(call.from_user.id, 'У вас уже установлен дополнительный фильтр \\"*_рейтинг_*\\"\\: {}\n'
                         'Введите рейтинг фильма \\(пример\\: 7\\, 10\\, 7\\.2\\-10\\)\\.'.format(GENRE[call.from_user.id]),
                         parse_mode="MarkdownV2")
    bot.set_state(call.from_user.id, UserState.add_additional_rating)


@bot.message_handler(state=UserState.add_additional_rating)
def data_verification(message):
    
    bot.delete_state(message.from_user.id)
    RATING[message.from_user.id] = message.text
    bot.send_message(message.from_user.id, "Добавлен фильтр по рейтингу", reply_markup=add_additional_or_continue_output())
    
    
    
@bot.callback_query_handler(func=lambda call:
    call.data == "filter_budget")
def add_rating_filter(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if GENRE[call.from_user.id] == None:
        bot.send_message(call.from_user.id, "Введите бюджет фильма (1000 - 6.000.000).")
    else:
        bot.send_message(call.from_user.id, 'У вас уже установлен дополнительный фильтр \\"*_бюджет_*\\"\\: {}\n'
                         'Введите бюджет фильма \\(1000 \\- 6\\.000\\.000\\)\\.'.format(GENRE[call.from_user.id]),
                         parse_mode="MarkdownV2")
    bot.set_state(call.from_user.id, UserState.add_additional_budget)


@bot.message_handler(state=UserState.add_additional_budget)
def data_verification(message):
    
    bot.delete_state(message.from_user.id)
    BUDGET[message.from_user.id] = message.text
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.from_user.id, "Добавлен фильтр по бюджету фильма", reply_markup=add_additional_or_continue_output())
    