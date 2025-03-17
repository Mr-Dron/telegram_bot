from telebot.types import Message

def start_help(bot, message: Message) -> None:
    bot.send_message(message.from_user.id, "Так я первый прототип, я еще помочь ничем не могу. Жди следующих обновлений") 