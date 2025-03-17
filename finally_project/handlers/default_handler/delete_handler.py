from database import models

def delete_start(bot, message):
    cash = models.MovieCash.select()
    
    for movie in cash:
        if str(movie.date_add) == message.text:
            movie.delete_instance()
    bot.send_message(message.from_user.id, f"История за {message.text} очищена")