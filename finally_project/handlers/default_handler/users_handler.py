from database.models import User
 
def all_users_handler(bot, message):
    users = User.select()
    
    for user in users:
        bot.send_message(message.from_user.id, 
                         f"ID пользователя: {user.user_id}\n"
                         f"Ссылка: @{user.username}\n"
                         f"Имя: {user.first_name}\n"
                         f"Фамилия: {user.last_name}\n"
                         f"Админ: {user.admin}")