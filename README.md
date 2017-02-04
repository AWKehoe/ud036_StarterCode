# ud036_StarterCode
The repository contains the Source code for a Movie Trailer website. The website displays a users favourite movies using a poster image, a storyline snapline and a link to the movie trailer when the poster image is clicked.

## What's Included

To generate a movie trailer website three python modules are used:

1. media.py
2. entertainment.py
3. fresh_tomatoes.py

### media.py
This contains a Movie class that can be used to generate an instance object of a movie. The Movie class has 4 instance variables:

| Instance Variable | Description |
| ----------------- | ----------- |
| **title**| *A string that contains the movie title*|
|**storyline**| *A string to hold a brief storyline*|
|**poster_image_url**| *A string containing the url to a poster image for the movie*|
|**trailer_youtube_url**| *A string containing the url for the movie trailer*|
    
**Note** all instance variable must be supplied in single class constructor. 

An example of instantiating a Movie instance of the war film The Great Escape is shown below:
```
greatescape = Movie("The Great Escape", 
                    "Steve McQueen fails to escape POW camp",
                    "https://upload.wikimedia.org/wikipedia/en/c/c7/Great_escape.jpg",
                    "https://youtu.be/hBpp1OTq0rY")
 ```

### entertainment.py

This module is a factory for creating instances of the Movie Class and then passing the list of movie instances into the fresh_tomatoes.py module that renders the website.

The user can create as many class instances as required. However the user must create a python list variable to store the list of movie class instances. The list variable is then passed into a function called **_open_movies_page(\<list\>)_**. See the code example below:

declare a list of movies
```
movies = [greatescape, bridgetofar, battleofbritain, battleofthebulge, platoon, metaljacket]

```

call function **_open_movies_page()_** from fresh_tomatoes.py and pass the movies list variable.
```
fresh_tomatoes.open_movies_page(movies)

```

The method call will now display a web page containing all your favourite movies.

### fresh_tomatoes.py
This module was created by Adarsh Nair from Udacity ( see Contributors section below for contact details) . The module contains python code that will render a web page and display a list of movies. The movies are passed within a python list variable when the open_movies_page() method is called.



## Getting Started

## Contributors

## Copywrite and Licenses
