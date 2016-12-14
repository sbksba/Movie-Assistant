import urllib
import os

def internet_access(item):
    try:
        stri = "https://www.google.com"
        data = urllib.urlopen(stri)
        return True
    except:
        print "[X] Please enable your internet connection for "+item+""
        return False

def exist_file(file_path):
    return os.path.isfile(file_path)
