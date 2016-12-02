import os.path as op
import os, shutil

from scraper import scraper_directorie
from createBase import *
from insertBase import update_base
from UiX_firefox import get_movies_db, open_movies_page
from statBase import *
from theater_info import *

tmdb.API_KEY = '7196d4486bd0fda2b04e9dac5db9e3df'

# GLOBALS VARIABLES
csvFile='movie.csv'
dbFile='MovieBase.sqlite'
dbSimi='SimilarBase.sqlite'
status = 1

class Profile(object):

    def __init__(self, name, moviePath):
        path = "profile/"+name+"/"
        self.moviePath = moviePath

        if (op.exists(path)):
            #print "\nProfile Already Exists"
            self.name = name
            self.moviePath = moviePath
            self.new_profile = False
            status=update_base(self.moviePath, self.getProfilePath()+dbFile, "movie", self.getProfilePath()+dbSimi, self.getProfilePath()+csvFile)
        else:
            #print "\nCreate Profile"
            os.makedirs(path)
            self.name = name
            self.new_profile = True
            # CREATE THE MOVIE BASE, SIMILAR BASE AND THE CSV FILE
            status=scraper_directorie(path+csvFile, self.moviePath)
            status=create_base_csv(path+csvFile,path+dbFile,"movie")
            status=create_base_similar(path+dbSimi)
            status=insert_similar(path+csvFile,path+dbFile,path+dbSimi)

    def __str__(self):
        return "NAME : "+self.getName()+"\nMOVIE PATH : "+self.getMoviePath()+"\nPROFILE PATH : "+self.getProfilePath()

    def getName(self):
        return self.name

    def getProfilePath(self):
        return "profile/"+self.name+"/"

    def getMoviePath(self):
        return self.moviePath

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
            open_movies_page(movies, self.getProfilePath()+'myMovies.html')
        elif (table == "similar"):
            movies = get_movies_db(self.getProfilePath()+dbSimi,genre,table)
            open_movies_page(movies, self.getProfilePath()+'myMovies.html')

    def theaterInfo(self,choice):
        if (choice == "nowPlaying"):
            nowPlaying()
        elif (choice == "upcoming"):
            upcoming()
        elif (choice == "popular"):
            popular()
        else:
            print "\nError : choice unknow"

    def update(self):
        print "\nNOT WORK VERY WELL"
        status=update_base(self.moviePath, self.getProfilePath()+dbFile, "movie", self.getProfilePath()+dbSimi, self.getProfilePath()+csvFile)
