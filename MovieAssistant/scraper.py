import tmdbsimple as tmdb
import csv, sys, shutil
import os.path as op
from os import listdir
from os.path import isfile, join
from time import sleep

from security import internet_access

# Print iterations progress
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = ' ' * filledLength + '-' * (barLength - filledLength)
    sys.stdout.write('\r%s |%s| %s%s' % (prefix, bar, percent, '%')),
    if iteration == total:
        sys.stdout.write(' Complete [%s]\n' % (suffix))
    sys.stdout.flush()

def get_genre_name(s,responseG):
    gId=gName=""
    for tmp in s['genre_ids']:
        gId = tmp
        break
    for g in responseG.get('genres'):
        if (g['id'] == gId):
            gName = g['name']

    return gName

def get_video_url(id):
    movies = tmdb.Movies(id)
    r = movies.videos()
    gVideo="https://www.youtube.com/watch?v="
    for v in r.get('results'):
        gVideo += v['key']
        break

    return gVideo

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

def scraper_verif(CSV_filepath):
    print "\nVERIF CSV\n"
    with open(CSV_filepath, 'rb') as verif:
        reader = csv.reader(verif, delimiter=';')
        for row in reader:
            print "{:50} | {:65} | {:40} | {} | {}".format(row[0], row[1], row[2], row[3], row[4])
    print "\n"
