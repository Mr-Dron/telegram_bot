from config_data.config import DB_PATH
from peewee import (SqliteDatabase, Model, CharField, IntegerField, 
AutoField, DateField, BooleanField, FloatField, ForeignKeyField)

db = SqliteDatabase(DB_PATH)

class BaseModel(Model): 
    """Базовый класс для всех моделей БД"""
    class Meta:
        database = db

class User(BaseModel):
    """Модель пользователя телеграм

    Поля:
        user_id (int): Уникальный id пользователя телеграм
        username (str): Логин пользователя телеграм
        first_name (str): Имя пользователя
        last_name (str): Фамилия пользователя
        admin (bool): Статус, является ли пользователь администратором(по умолчанию False)
        limit (int): Лимит выводимых результатов поиска(по умолчанию 10)

    """
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    admin = BooleanField(default=False)
    limit = IntegerField(default=10)

class MovieCash(BaseModel):
    """Модель для хранения информации о фильмах пользователя

    Поля: 
        user (User): Ссылка на поьзователя(внешний ключ)
        movie_id (int): Уникальный id фильма из внешнего источника
        cash_id (int): Уникальный id фильма записи в БД()
        movie_name (str): Название фильма
        movie_description (str): Описание фильма
        movie_rating (str): Рейтинг фильма
        movie_year (int): Год выпуска фильма
        movie_genre (str): Жанрый фильма
        movie_age_rating (int): Возрастной рейтинг 
        movie_poster (str): Ссылка на постер фильма
        date_add (date): Дата добавления фильма в БД
        movie_viewed (bool): Находится ли фильм в списке желаемого(по умолчанию False)
    """
    user = ForeignKeyField(User, backref="movies")
    movie_id = IntegerField()
    cash_id = AutoField()
    movie_name = CharField(null=True)
    movie_description = CharField(null=True)
    movie_rating = FloatField(null=True)
    movie_year = IntegerField(null=True)
    movie_genre = CharField(null=True)
    movie_age_rating = IntegerField(null=True)
    movie_poster = CharField(null=True)
    date_add = DateField()
    movie_viewed = BooleanField(default=False)


def create_models():
    """Создает все таблицы в базе данных для моделей, наследующих BaseModel.
    
    Обрабатывает исключение при возникновение создания таблиц
    """
    try:
        db.create_tables(BaseModel.__subclasses__())
    except Exception as exc:
        print(f"Ошибка создания таблицы. {exc}")
