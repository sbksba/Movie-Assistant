import tmdbsimple as tmdb
import csv, sys, shutil
from os import listdir
from os.path import isfile, join

from tools import *

def scraper_directorie(CSV_filepath,DIR_path):
    if (internet_access("create a profile")):
        mypath=DIR_path
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        l = len(onlyfiles)
        i=0
        with open(CSV_filepath,'w') as fcsv:
            fcsv.write("name;img_url;youtube_url;year;genre\n")
            printProgress(i, l, prefix = 'Progress:', suffix = '', barLength = 50)
            for f in onlyfiles:
                search = tmdb.Search()
                genre = tmdb.Genres()
                responseM = search.movie(query=f.replace("_"," ").rsplit('.',1)[0])
                responseG = genre.list()
                for s in responseM.get('results'):
                    # GET GENRE NAME
                    gName = get_genre_name(s,responseG)
                    gVideo = get_video_url(s['id'])

                    if (s['poster_path'] is None):
                        fcsv.write("{};https://image.tmdb.org/t/p/w185/NONE;{};{};{}\n".format(s['title'], gVideo, s['release_date'].rsplit('-',2)[0], gName))
                    else:
                        fcsv.write("{};https://image.tmdb.org/t/p/w185{};{};{};{}\n".format(s['title'], s['poster_path'], gVideo, s['release_date'].rsplit('-',2)[0], gName))
                    break
                i += 1
                printProgress(i, l, prefix = 'Progress:', suffix = 'movie', barLength = 50)

        return 0
    else:
        name = DIR_path.split('/',1)[1]
        shutil.rmtree("profile/"+name)
