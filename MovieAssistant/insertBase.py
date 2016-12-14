import sys, csv, sqlite3
import tmdbsimple as tmdb
from os import listdir
from os.path import isfile, join
from scraper import *

from security import internet_access

def insert_base(insert,DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute("INSERT INTO {tn} (NAME, IMGURL, YOUTUBEURL, YEAR, GENRE) VALUES(?, ?, ?, ?, ?);".format(tn=table), insert)
    db.commit()

    cur.close()
    db.close()

    return 0

def check_double(DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute("SELECT COUNT(*) AS nbrdouble, NAME, IMGURL, YOUTUBEURL ,YEAR, GENRE FROM {tn} GROUP BY NAME, IMGURL, YOUTUBEURL, YEAR, GENRE HAVING COUNT(*) > 1".format(tn=table))
    for row in cur:
        print('{:3}|{:50}|{:65}|{:65}|{}|{}'.format(*row))
    cur.close()
    db.close()

def del_double(DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute('DELETE FROM {tn} WHERE ID NOT IN (SELECT MIN(ID) FROM {tn} GROUP BY NAME, IMGURL, YOUTUBEURL, YEAR, GENRE)'.format(tn=table))
    db.commit()

    cur.close()
    db.close()

    return 0

def finalize_base(CSV_filepath,DB_Similar):
    db = sqlite3.connect(DB_Similar)
    cur = db.cursor()

    with open(CSV_filepath, 'rb') as finalize:
        reader = csv.reader(finalize, delimiter=";")
        header = reader.next()
        for row in reader:
            cur.execute('DELETE FROM similar WHERE NAME=? AND YEAR=? AND GENRE=?',(row[0],row[3],row[4]))
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
        #check_double(DB_Similar,"similar")
        status = del_double(DB_Similar,"similar")

        # DEL MOVIE ALREADY EXISTS IN MOVIE BASE
        status = finalize_base(CSV_filepath,DB_Similar)

        return status

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
                        i += 1
                        printProgress(i, l, prefix = 'Progress:', suffix = 'movie', barLength = 50)

            status=insert_similar(CSV_filepath,DB_filepath,DB_Similar)
        return 0
