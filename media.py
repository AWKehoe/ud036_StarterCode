class Movie():
    """ A class that defines movies """
    movie_ratings = ['U', 'PG', '13', 'R']
    
    def __init__(self, movie_title, movie_storyline, movie_trailer_url, movie_poster_image, movie_genre, movie_duration):
        self.title = movie_title
        self.storyline = movie_storyline
        self.trailerurl = movie_trailer_url
        self.posterimage = movie_poster_image        
        self.genre = movie_genre
        self.duration = movie_duration
        

        
        
        
