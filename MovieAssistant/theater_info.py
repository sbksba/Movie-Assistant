import tmdbsimple as tmdb
from scraper import get_genre_name
from security import internet_access

def nowPlaying():
    if (internet_access("the movies actually on theater")):
        movie = tmdb.Movies()
        genre = tmdb.Genres()
        rG = genre.list()
        response = movie.now_playing()
        print "\nNOW PLAYING\n===========\n"
        for s in response.get('results'):
            gName = get_genre_name(s,rG)

            if (s['poster_path'] is None):
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
            else:
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)

def upcoming():
    if (internet_access("the upcoming movies")):
        movie = tmdb.Movies()
        genre = tmdb.Genres()
        rG = genre.list()
        response = movie.upcoming()
        print "\nUPCOMING\n========\n"
        for s in response.get('results'):
            gName = get_genre_name(s,rG)

            if (s['poster_path'] is None):
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
            else:
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)

def popular():
    if (internet_access("the popular movies")):
        movie = tmdb.Movies()
        genre = tmdb.Genres()
        rG = genre.list()
        response = movie.popular()
        print "\nPOPULAR\n=======\n"
        for s in response.get('results'):
            gName = get_genre_name(s,rG)

            if (s['poster_path'] is None):
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
            else:
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
