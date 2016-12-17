import sys, csv, sqlite3
import tmdbsimple as tmdb
from os import listdir
from os.path import isfile, join

from tools import *
from DB_tools import *
from insertBase import *

def update_base(DIR_path,DB_filepath,table,DB_Similar,CSV_filepath):
    if (internet_access("update the data bases")):
        mypath=DIR_path
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()

        tADD = []

        for tmp in onlyfiles:
            name = tmp.replace("_"," ").rsplit('.',1)[0]
            cur.execute('SELECT * FROM {tn} WHERE NAME="{n}"'.format(tn=table,n=name))
            data = cur.fetchone()
            if data is None:
                tADD.append(name)

        # if not in base add to csv file and db file
        l = len(tADD)
        i=0
        if (l != 0):
            print "\nUPDATE"
            with open(CSV_filepath, 'a') as update:
                    printProgress(i, l, prefix = 'Progress:', suffix = '', barLength = 50)
                    for f in tADD:
                        ## MOVIE DATA BASE
                        search = tmdb.Search()
                        genre = tmdb.Genres()
                        responseM = search.movie(query=f.replace("_"," ").rsplit('.',1)[0])
                        responseG = genre.list()
                        for s in responseM.get('results'):
                            # GET GENRE NAME
                            gName = get_genre_name(s,responseG)
                            gVideo = get_video_url(s['id'])
                            if (s['poster_path'] is None):
                                update.write("{};https://image.tmdb.org/t/p/w185/NONE;{};{};{}\n".format(s['title'], gVideo, s['release_date'].rsplit('-',2)[0], gName))
                                to_db = [s['title'],"https://image.tmdb.org/t/p/w185/NONE",gVideo,s['release_date'].rsplit('-',2)[0],gName]
                            else:
                                update.write("{};https://image.tmdb.org/t/p/w185{};{};{};{}\n".format(s['title'], s['poster_path'], gVideo, s['release_date'].rsplit('-',2)[0], gName))
                                to_db = [s['title'],"https://image.tmdb.org/t/p/w185/"+s['poster_path'],gVideo,s['release_date'].rsplit('-',2)[0],gName]
                            break
                        status = insert_base(to_db,DB_filepath,table)

                        ## SIMILAR DATA BASE
                        #print "UPDATE SIMILAR"
                        response = search.movie(query=s['title'])
                        for si in search.results:
                            id = si['id']
                            break

                        movie = tmdb.Movies(id)
                        responseM = movie.similar_movies()
                        responseG = genre.list()
                        for si in responseM.get('results'):
                            # GET GENRE NAME AND YOUTUBE URL
                            gName = get_genre_name(si,responseG)
                            gVideo = get_video_url(si['id'])

                            # INSERT IN BASE
                            if (si['poster_path'] is not None):
                                if (si['release_date'] is not None):
                                    to_db = [si['title'],"https://image.tmdb.org/t/p/w185/"+si['poster_path'],gVideo,s['release_date'].rsplit('-',2)[0].encode('utf-8'),gName]
                                    status = insert_base(to_db,DB_Similar,"similar")

                        i += 1
                        printProgress(i, l, prefix = 'Progress:', suffix = 'update', barLength = 50)

            # DEL DOUBLE IN BASE
            status = del_double(DB_Similar,"similar")

            # DEL MOVIE ALREADY EXISTS IN MOVIE BASE
            status = finalize_base(CSV_filepath,DB_Similar)

        return 0
