from telebot.handler_backends import State, StatesGroup

class UserState(StatesGroup):
    search_by_name = State()
    search_by_rating = State()
    history = State()
    delete_history = State()
    search_out = State()
    main = State()
    search_by_genre = State()
    favorite_movie = State()