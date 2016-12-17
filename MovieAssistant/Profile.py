import os.path as op

from tools import *
from DB_tools import print_base
from Config_tools import ConfigSectionMap

# CREATION OF THE DATA BASES
from scraper import scraper_directorie
from createBase import create_base_csv, create_base_similar
from update import update_base

####
from UiX_firefox import get_movies_db, open_movies_page
from statBase import stat_base, plot_base
from theater_info import theater

# API KEY TMDB
tmdb.API_KEY = ConfigSectionMap("API")['key']

# GLOBALS VARIABLES
csvFile = ConfigSectionMap("FILE")['csv']
dbFile = ConfigSectionMap("FILE")['movie']
dbSimi = ConfigSectionMap("FILE")['similar']
status = 1

class Profile(object):

    def __init__(self, name, moviePath):
        path = "profile/"+name+"/"
        self.moviePath = moviePath
        self.name = name

        if (op.exists(path)):
            status=update_base(self.moviePath,
                               self.getProfilePath()+dbFile,
                               "movie",
                               self.getProfilePath()+dbSimi,
                               self.getProfilePath()+csvFile)
        else:
            os.makedirs(path)
            status=scraper_directorie(path+csvFile, self.moviePath)
            status=create_base_csv(path+csvFile,path+dbFile,"movie")
            status=create_base_similar(path+csvFile,path+dbFile,path+dbSimi)

    def __str__(self):
        return "NAME : "+self.name+"\nMOVIE PATH : "+self.moviePath+"\nPROFILE PATH : "+self.getProfilePath()

    def getProfilePath(self):
        return "profile/"+self.name+"/"

    def delete(self):
        if (op.exists(self.getProfilePath())):
            shutil.rmtree(self.getProfilePath())

    def printBase(self,table):
        if (table == "movie"):
            print_base(self.getProfilePath()+dbFile,table)
        elif (table == "similar"):
            print_base(self.getProfilePath()+dbSimi,table)

    def statBase(self,table):
        if (table == "movie"):
            stat_base(self.getProfilePath()+dbFile,table)
        elif (table == "similar"):
            stat_base(self.getProfilePath()+dbSimi,table)

    def plotBase(self,table):
        if (table == "movie"):
            plot_base(self.getProfilePath()+dbFile,table)
        elif (table == "similar"):
            plot_base(self.getProfilePath()+dbSimi,table)

    def webPage(self,table,genre):
        if (table == "movie"):
            movies = get_movies_db(self.getProfilePath()+dbFile,genre,table)
        elif (table == "similar"):
            movies = get_movies_db(self.getProfilePath()+dbSimi,genre,table)
        if (movies != False):
            open_movies_page(movies, self.getProfilePath()+'myMovies.html')

    def theaterInfo(self,choice):
        theater(choice)
