import sys, csv, sqlite3
import tmdbsimple as tmdb
from os import listdir
from os.path import isfile, join

from tools import *
from DB_tools import *

def insert_base(insert,DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute("INSERT INTO {tn} (NAME, IMGURL, YOUTUBEURL, YEAR, GENRE) VALUES(?, ?, ?, ?, ?);".format(tn=table), insert)
    db.commit()

    cur.close()
    db.close()

    return 0

def insert_similar(CSV_filepath, DB_filepath, DB_Similar):
    if (internet_access("create the similar data base")):
        status=0
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()

        search = tmdb.Search()
        genre = tmdb.Genres()
        # PROGRESS BAR
        cur.execute('select count(*) from movie')
        for row in cur:
            l = row[0]
        i=0
        cur.execute("SELECT * FROM movie")
        printProgress(i, l, prefix = 'Progress:', suffix = '', barLength = 50)
        for row in cur:
            response = search.movie(query=row[1])
            for s in search.results:
                id = s['id']
                break

            movie = tmdb.Movies(id)
            responseM = movie.similar_movies()
            responseG = genre.list()
            for s in responseM.get('results'):
                # GET GENRE NAME AND YOUTUBE URL
                gName = get_genre_name(s,responseG)
                gVideo = get_video_url(s['id'])

                # INSERT IN BASE
                if (s['poster_path'] is not None):
                    if (s['release_date'] is not None):
                        to_db = [s['title'],"https://image.tmdb.org/t/p/w185/"+s['poster_path'],gVideo,s['release_date'].rsplit('-',2)[0].encode('utf-8'),gName]
                        status = insert_base(to_db,DB_Similar,"similar")
            i += 1
            printProgress(i, l, prefix = 'Progress:', suffix = 'similar', barLength = 50)

        cur.close()
        db.close()

        # DEL DOUBLE IN BASE
        status = del_double(DB_Similar,"similar")

        # DEL MOVIE ALREADY EXISTS IN MOVIE BASE
        status = finalize_base(CSV_filepath,DB_Similar)

        return status
