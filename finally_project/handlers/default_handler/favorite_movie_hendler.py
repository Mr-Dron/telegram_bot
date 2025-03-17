from database.models import MovieCash

def favorite_movie(message):
    movies = MovieCash.select()
    result = list()
    
    result = [movie for movie in movies if movie.movie_viewed and movie.user.user_id == message.from_user.id]            
    
    return result