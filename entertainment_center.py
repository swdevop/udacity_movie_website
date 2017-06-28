# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
# imports media.py which includes the Movie class needed below
import fresh_tomatoes
# imports fresh_tomatoes.py which allows us to open our fresh_tomatoes.html page


# creates necessary data for each movie in our list including title, imdb link, movie poster, and movie trailer link
tombstone = media.Movie("Tombstone",
                        "http://www.imdb.com/title/tt0108358/?ref_=nv_sr_1",
                        "https://upload.wikimedia.org/wikipedia/en/7/71/Tombstoneposter.jpeg",
                        "https://www.youtube.com/watch?v=IPS7xnVh4qk")

legends_of_the_fall = media.Movie("Legends of the Fall",
                                  "http://www.imdb.com/title/tt0110322/",
                                  "https://upload.wikimedia.org/wikipedia/en/1/1d/Legendsoffallposter.jpg",
                                  "https://www.youtube.com/watch?v=FyVmV7zSY7I")

blade_runner = media.Movie("Blade Runner",
                           "http://www.imdb.com/title/tt0083658/?ref_=nv_sr_2",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

star_trek = media.Movie("Star Trek",
                        "http://www.imdb.com/title/tt0796366/?ref_=nv_sr_7",
                        "https://upload.wikimedia.org/wikipedia/en/2/29/Startrekposter.jpg",
                        "https://www.youtube.com/watch?v=pKFUZ10Wmbw")

serenity = media.Movie("Serenity",
                       "http://www.imdb.com/title/tt0379786/?ref_=nv_sr_1",
                       "https://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
                       "https://www.youtube.com/watch?v=JY3u7bB7dZk")

nine = media.Movie("9",
                   "9 is a 2009 American computer-animated post-apocalyptic"
                   "http://www.imdb.com/title/tt0472033/?ref_=fn_al_tt_1",
                   "https://upload.wikimedia.org/wikipedia/en/c/c9/9posterfinal.jpg",
                   "https://www.youtube.com/watch?v=_qApXdc1WPY")

# creates our list of movies to include on page
movies = [tombstone, legends_of_the_fall, blade_runner, star_trek, serenity, nine]
# calls open_movies_page which will open up our web page
fresh_tomatoes.open_movies_page(movies)
