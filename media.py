class Movie(object):
    """ A Movie class that describes information related to title, links to poster image and link to trailer
    
    Attributes:
        title: A string that contains the movie title
        storyline: A string to hold a brief storyline
        poster_image_url: A string describing the url to a poster image for the movie
        trailer_youtube_url: A string describing the url for the movie trailer
    """
    
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_url):
        """Initiate Movie instance with title, storyline, poster image and movie trailer"""
        
        self.title = movie_title  # Text to hold film title
        self.storyline = movie_storyline  # Strapline of the film story
        self.poster_image_url = movie_poster_image  # A url to a poster image
        self.trailer_youtube_url = movie_trailer_url  # A url to the film trailer
    
        

        
        
        
