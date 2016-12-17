from Profile import Profile

from Config_tools import ConfigSectionMap
from optparse import OptionParser
import sys
import os

parser = OptionParser()
parser.add_option("-d", "--dir", dest="dir", help ="The directorie of the movie files")
parser.add_option("-n", "--name", dest="name", help ="The name of the profile")
parser.add_option("-e", "--erase", dest="erase", help ="Delete the profile")
parser.add_option("-s", "--stat", dest="stat", help ="Print the stat for the profile (terminal of graphic)")
parser.add_option("-t", "--table", dest="table", help ="Name of the movie base (movie or similar)")
parser.add_option("-a", "--theater", dest="theater", help ="Print Theater Info (nowPlaying or upcoming or popular)")
parser.add_option("-w", "--web", dest="web", help ="Print base on webpage (all or genre in particular)")
parser.add_option("-p", "--printd", dest="printd", help ="Print the base")
(options, args) = parser.parse_args()
dir = options.dir
name = options.name
erase = options.erase
stat = options.stat
table = options.table
theater = options.theater
web = options.web
printd = options.printd

def window():
    try:
        if (dir and erase):
            p = Profile(erase,dir)
            p.delete()
        elif (dir and name and printd):
            p = Profile(name,dir)
            p.printBase(printd)
        elif (dir and name and theater):
            p = Profile(name,dir)
            p.theaterInfo(theater)
        elif (dir and name and stat and table):
            p = Profile(name,dir)
            if (stat == "terminal"):
                p.statBase(table)
            elif (stat == "graphic"):
                p.plotBase(table)
        elif (dir and name and table and web):
            p = Profile(name,dir)
            p.webPage(table,web)
        elif (dir and name):
            p = Profile(name,dir)
    except:
        if len(sys.argv) != 3:
            #parser.error("Error Arguments")
            print ""

def bench():
    name = ConfigSectionMap("PROFILE")['default']
    dire = ConfigSectionMap("PROFILE")['dir']
    p = Profile(name,dire)
    print p
    table="movie"
    p.printBase(table)
    p.statBase(table)
    #p.plotBase(table)
    p.webPage(table,"all")
    p.theaterInfo("nowPlaying")
    #p.delete()
