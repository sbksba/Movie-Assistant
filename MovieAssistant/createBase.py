import sys, csv, sqlite3
from insertBase import *


def create_base_csv(CSV_filepath,DB_filepath,table):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()
        cur.executescript("""
            DROP TABLE IF EXISTS movie;
            CREATE TABLE movie (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, IMGURL TEXT, YOUTUBEURL TEXT, YEAR TEXT, GENRE TEXT);
            """)

        with open(CSV_filepath, "rb") as f: # CSV file input
            reader = csv.reader(f, delimiter=';') # no header information with delimiter
            header = reader.next()
            for row in reader:
                to_db = [unicode(row[0], "utf8"), unicode(row[1], "utf8"), unicode(row[2], "utf8"), unicode(row[3], "utf8"), unicode(row[4], "utf8")]
                cur.execute("INSERT INTO movie (NAME, IMGURL, YOUTUBEURL, YEAR, GENRE) VALUES(?, ?, ?, ?, ?);", to_db)
                db.commit()

        cur.close()
        db.close()
        del_double(DB_filepath,table)

        return 0

def create_base_similar(DB_filepath):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()
        cur.executescript("""
            DROP TABLE IF EXISTS similar;
            CREATE TABLE similar (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, IMGURL TEXT, YOUTUBEURL TEXT, YEAR TEXT, GENRE TEXT);
            """)

        cur.close()
        db.close()

        return 0

def print_base(DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute("SELECT * FROM {tn}".format(tn=table))
    print ""
    for row in cur:
        print "{:4}|{:50}|{:65}|{:45}|{}|{}".format(row[0], row[1].encode('utf-8'), row[2].encode('utf-8'), row[3].encode('utf-8'), row[4], row[5].encode('utf-8'))

    cur.close()
    db.close()
