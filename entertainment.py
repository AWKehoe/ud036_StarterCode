import fresh_tomatoes
from media import Movie

# Create instances of my favourite War Movies using Movie Class

greatescape = Movie("The Great Escape", 
                    "Steve McQueen fails to escape POW camp",
                    "https://upload.wikimedia.org/wikipedia/en/c/c7/Great_escape.jpg",
                    "https://youtu.be/hBpp1OTq0rY")

bridgetofar = Movie("A Bridge To Far", 
                    "The story of Operation Market Garden",
                    "https://upload.wikimedia.org/wikipedia/en/e/e7/Bridge_too_far_movieposter.jpg",
                    "https://youtu.be/AWL184ZcSxA")

battleofbritain = Movie("The Battle Of Britain", 
                    "How the RAF defeated the might of the German Lufwaffe",
                    "https://upload.wikimedia.org/wikipedia/en/1/12/Battle_of_Britain_%28movie_poster%29.jpg",
                    "https://youtu.be/KwBcnbutpjw")

battleofthebulge = Movie("Battle Of The Bulge", 
                        "Not a story of struggles of dieting...",
                        "https://upload.wikimedia.org/wikipedia/en/5/5b/Bulge_sheet_A.jpg",
                        "https://youtu.be/mdjau_yi5AY")

platoon = Movie("Platoon", 
                         "One mans fight for the honor of war",
                        "https://upload.wikimedia.org/wikipedia/en/a/a9/Platoon_posters_86.jpg",
                        "https://youtu.be/hGsyEkfjhQk")

metaljacket = Movie("Full Metal Jacket", 
                        "Story of a soldier who wears a metal jacket",
                        "https://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
                        "https://youtu.be/x9f6JaaX7Wg")

# Create a list of movies 
movies = [greatescape, bridgetofar, battleofbritain, battleofthebulge, platoon, metaljacket]

# Module that creates a HTML file which visualizes all of your favorite movies.
fresh_tomatoes.open_movies_page(movies)

