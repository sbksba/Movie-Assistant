import tmdbsimple as tmdb
from tools import internet_access, get_genre_name

def theater(item):
    if (internet_access("theater information")):
        movie = tmdb.Movies()
        genre = tmdb.Genres()
        rG = genre.list()
        if (item == "nowPlaying"):
            response = movie.now_playing()
            name = "NOW PLAYING"
        elif (item == "upcoming"):
            response = movie.upcoming()
            name = "UPCOMING"
        elif (item == "popular"):
            response = movie.popular()
            name = "POPULAR"
        else:
            print "\n[X] Theater command unknown"
            exit(0)
        print "\n"+name+"\n=======\n"
        for s in response.get('results'):
            gName = get_genre_name(s,rG)

            if (s['poster_path'] is None):
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
            else:
                print "{:50} | {} | {}".format(s['title'], s['release_date'], gName)
