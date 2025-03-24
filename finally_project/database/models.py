from config_data.config import DB_PATH
from peewee import (SqliteDatabase, Model, CharField, IntegerField, 
AutoField, DateField, BooleanField, FloatField, ForeignKeyField)

db = SqliteDatabase(DB_PATH)

class BaseModel(Model): 
    class Meta:
        database = db

class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    admin = BooleanField(default=False)
    limit = IntegerField(default=10)

class MovieCash(BaseModel):
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
    try:
        db.create_tables(BaseModel.__subclasses__())
    except Exception as exc:
        print(f"Ошибка создания таблицы. {exc}")
