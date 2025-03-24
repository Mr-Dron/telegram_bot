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
    new_limit = State()
    add_additional_filters = State()
    add_additional_rating = State()
    add_additional_budget = State()