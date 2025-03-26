from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружени или файл .env не был найден")
else:
    load_dotenv()
    
    
API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_PATH = os.path.join(os.getcwd(), "finally_project", "database", os.getenv("DB_PATH"))
SEARCH_RESULTS = dict()
CURRENT_INDEX = dict()

DEFAULT_COMMANDS = (
    ("start", "запустить бота"),
    ("help", "вывести справку"),
    ("limit", "изменить лимит на поиск")
)

ADMIN_COMMANDS = (
    ("start", "запустить бота"),
    ("help", "вывести справку"),
    ("search_by_name", "поиск фильма по имени"),
    ("search_by_rating", "поиск фильма по рейтингу"),
    ("history", "история поиска"),
    ("delete_db", "Удаление базы данных"),
    ("my_data", "Мои данные"),
    ("all_users", "Все пользователи"),
)

USER_COMMANDS = (
    ("start", "запустить бота"),
    ("help", "вывести справку"),
    ("search_by_name", "поиск фильма по имени"),
    ("search_by_rating", "поиск фильма по рейтингу"),
    ("history", "история поиска"),
)