import tmdbsimple as tmdb
import urllib, os, sys, shutil
from os.path import isfile
from time import sleep

# Test if internet is accessible
def internet_access(item):
    try:
        stri = "https://www.google.com"
        data = urllib.urlopen(stri)
        return True
    except:
        print "[X] Please enable your internet connection for "+item+""
        return False

# Test if a file exist
def exist_file(file_path):
    return os.path.isfile(file_path)

# Return the genre name of a movie
def get_genre_name(s,list_genre):
    gId=gName=""
    for tmp in s['genre_ids']:
        gId = tmp
        break
    for g in list_genre.get('genres'):
        if (g['id'] == gId):
            gName = g['name']

    return gName

# Return the youtube url for a movie
def get_video_url(id_movie):
    movies = tmdb.Movies(id_movie)
    r = movies.videos()
    gVideo="https://www.youtube.com/watch?v="
    for v in r.get('results'):
        gVideo += v['key']
        break

    return gVideo

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
