from telebot.types import BotCommand
from config_data.config import ADMIN_COMMANDS, USER_COMMANDS, DEFAULT_COMMANDS

def set_default_commands(bot):
    bot.set_my_commands( 
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )

def set_admin_commands(bot):
    bot.set_my_commands( 
        [BotCommand(*i) for i in ADMIN_COMMANDS]
    )

def set_user_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in USER_COMMANDS]
    )