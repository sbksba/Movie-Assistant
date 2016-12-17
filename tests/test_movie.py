from MovieAssistant import scraper
from MovieAssistant import createBase
from MovieAssistant import update

import tmdbsimple as tmdb

tmdb.API_KEY = '7196d4486bd0fda2b04e9dac5db9e3df'

# GLOBALS VARIABLES
csvFile='tests/tmp/movie.csv'
dbFile='tests/tmp/MovieBase.sqlite'
dbSimi='tests/tmp/SimilarBase.sqlite'
testPath='data/zero'

def test_scrape():
    # TEST SCRAPE INFORMATION AND CREATE CSV FILE
    status=1
    status=scraper.scraper_directorie(csvFile,testPath)
    assert status == 0

def test_movie():
    # TEST CREATE MOVIE BASE
    status=1
    status=createBase.create_base_csv(csvFile,dbFile,"movie")
    assert status == 0

def test_similar():
    # TEST CREATE SIMILAR BASE
    status=1
    status=createBase.create_base_similar(csvFile,dbFile,dbSimi)
    assert status == 0

'''
def test_insert_similar():
    # TEST INSERT DATA IN SIMILAR BASE AND CLEAN IT
    status=1
    status=insertBase.insert_similar(csvFile,dbFile,dbSimi)
    assert status == 0
'''

def test_update_base():
    status=1
    status=update.update_base(testPath, dbFile, "movie", dbSimi, csvFile)
    assert status == 0

if __name__ == '__main__':
    test_scrape()
    test_movie()
    test_similar()
    #test_insert_similar()
    test_update_base()
