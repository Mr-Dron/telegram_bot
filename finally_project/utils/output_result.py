from keyboards.keyboards import search_movie_kb, cash_movie_kb, favorite_movie_kb
from .search_check import search_check, history_check

def output_history(bot, message, result, current_index, length_result):
    res = history_check(result)
    
    try:
        bot.send_photo(message.from_user.id, photo=result.movie_poster, 
                   caption=res, parse_mode="MarkdownV2", reply_markup=cash_movie_kb(current_index, length_result))
    except Exception as exc:
        bot.send_message(message.from_user.id, res, parse_mode="MarkdownV2", reply_markup=cash_movie_kb(current_index, length_result))


def output_favorite(bot, message, result, current_index, length_result):
    res = history_check(result)
    
    try:
        bot.send_photo(message.from_user.id, photo=result.movie_poster, 
                   caption=res, parse_mode="MarkdownV2", reply_markup=favorite_movie_kb(current_index, length_result))
    except Exception as exc:
        bot.send_message(message.from_user.id, res, parse_mode="MarkdownV2", reply_markup=favorite_movie_kb(current_index, length_result))


def output_search(bot, message, result, current_index, length_result):
        
    res = search_check(result) 
        
    if ("poster" in result) and (result["poster"]["previewUrl"] != ""):
        try:
            bot.send_photo(message.from_user.id, photo=result["poster"]["previewUrl"], caption=res, 
                           parse_mode="MarkdownV2", reply_markup=search_movie_kb(current_index, length_result))
        except Exception as exc:
            bot.send_message(message.from_user.id, res, parse_mode="MarkdownV2",
                         reply_markup=search_movie_kb(current_index, length_result))
            # bot.send_photo(message.from_user.id, photo=result["poster"]["url"], caption=res, 
            #                parse_mode="MarkdownV2", reply_markup=search_movie_kb(current_index, length_result))
    else:       
        bot.send_message(message.from_user.id, res, parse_mode="MarkdownV2",
                         reply_markup=search_movie_kb(current_index, length_result))


def out_search_with_kb(bot, call, results, current_index):
    data = call.data 
    
    if data.startswith("prev"):
        current_index -= 1
    elif data.startswith("next"):
        current_index += 1
    elif data == "exit_search":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, "Вы вышли из поиска")
        return
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_search(bot, call, results[current_index], 
                  current_index ,len(results))
    
    return current_index

def out_cash_with_kb(bot, call, results, current_index):
    data = call.data 
    
    if data.startswith("prev"):
        current_index -= 1
    elif data.startswith("next"):
        current_index += 1
    elif data == "exit_history":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, "Вы вышли из истории")
        return
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_history(bot, call, results[current_index], 
                  current_index ,len(results))
    
    return current_index

def out_favorite_with_kb(bot, call, results, current_index):
    data = call.data
    
    if data.startswith("prev"):
        current_index -= 1
    elif data.startswith("next"):
        current_index += 1
    elif data == "exit_favorite":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.from_user.id, "Вы вышли из истории")
        return
    
    bot.delete_message(call.message.chat.id, call.message.message_id)
    output_favorite(bot, call, results[current_index], 
                  current_index ,len(results))
    
    return current_index