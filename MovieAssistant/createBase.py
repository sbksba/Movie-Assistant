import sys, csv, sqlite3

from tools import exist_file
from DB_tools import del_double
from insertBase import insert_similar

def create_base_csv(CSV_filepath,DB_filepath,table):
   if (exist_file(CSV_filepath)):
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

def create_base_similar(CSV_filepath,DB_filepath,DB_Similar):
   db = sqlite3.connect(DB_Similar)
   cur = db.cursor()
   cur.executescript("""
   DROP TABLE IF EXISTS similar;
   CREATE TABLE similar (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, IMGURL TEXT, YOUTUBEURL TEXT, YEAR TEXT, GENRE TEXT);
   """)

   cur.close()
   db.close()
   insert_similar(CSV_filepath,DB_filepath,DB_Similar)

   return 0
