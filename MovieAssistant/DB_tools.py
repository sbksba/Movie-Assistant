import sys, csv, sqlite3

from tools import exist_file

def print_base(DB_filepath,table):
   if (exist_file(DB_filepath)):
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()

        cur.execute("SELECT * FROM {tn}".format(tn=table))
        print ""
        for row in cur:
                print "{:4}|{:50}|{:65}|{:45}|{}|{}".format(row[0], row[1].encode('utf-8'), row[2].encode('utf-8'), row[3].encode('utf-8'), row[4], row[5].encode('utf-8'))

        cur.close()
        db.close()

def del_double(DB_filepath,table):
    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute('DELETE FROM {tn} WHERE ID NOT IN (SELECT MIN(ID) FROM {tn} GROUP BY NAME, IMGURL, YOUTUBEURL, YEAR, GENRE)'.format(tn=table))
    db.commit()

    cur.close()
    db.close()

    return 0

def finalize_base(CSV_filepath,DB_Similar):
    db = sqlite3.connect(DB_Similar)
    cur = db.cursor()

    with open(CSV_filepath, 'rb') as finalize:
        reader = csv.reader(finalize, delimiter=";")
        header = reader.next()
        for row in reader:
            cur.execute('DELETE FROM similar WHERE NAME=? AND YEAR=? AND GENRE=?',(row[0],row[3],row[4]))
            db.commit()

    cur.close()
    db.close()

    return 0
