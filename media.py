# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser
# imported so we have a way to open the movie trailer when clicked

class Movie():
    """This class provides a way to store movie related information
        self.title is for the movie title.
        self.link is for the imdb page link
        self.poster_image_url is for the movie poster image link
        self.trailer_youtube_url is for the movie trailer from youtube
    """


    def __init__(self, movie_title, movie_link, poster_image, trailer_youtube):
        # initialize instance of class Movie
        """
        :param movie_title: this will be a string containing the title of the movie
        :param movie_link: this will be a url of the movie's imdb link
        :param poster_image: this will be a url of the movie's movie poster link
        :param trailer_youtube: this will be a rul of the movie's youtube trailer
        """
        self.title = movie_title
        self.link = movie_link
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # opens up the movie trailer when the user clicks the tile
        webbrowser.open(self.trailer_youtube_url)
