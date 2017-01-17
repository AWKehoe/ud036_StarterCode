import fresh_tomatoes
from media import Movie

# Create instances of Movies

toy_story_4 = Movie("Toy Story 4", 
                    "Animated movie about crazy toys", 
                    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                    "https://www.youtube.com/watch?v=QW0sjQFpXTU")

avatar = Movie("Avatar", 
               "Animated fantasy movie about some weird blue people",
               "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story_4, avatar]

fresh_tomatoes.open_movies_page(movies)

