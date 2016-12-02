import sqlite3
import matplotlib.pyplot as plt

def stat_base(DB_filepath,table):
    try:
        db = sqlite3.connect(DB_filepath)
        cur = db.cursor()
        '''
        cur.execute('select * from movie')
        for row in cur:
        print('{:3}|{:50}|{:65}|{}|{}'.format(*row))
        '''
        print('\nSTATISTICS : {tn}\n=========='.format(tn=table))
        print('\nGLOBALS')
        cur.execute('select count(*) from {tn}'.format(tn=table))
        for row in cur:
            total = row[0]

        cur.execute('select count(distinct m.genre) from {tn} m'.format(tn=table))
        for row in cur:
            nb_genre = row[0]

        print('number of genre  : {}\nnumber of movies : {}'.format(nb_genre,total))

        print('\nNUMBER of MOVIE BY GENRE')
        cur.execute('select count(m.name), m.genre from {tn} m group by genre order by count(m.name) DESC'.format(tn=table))
        for row in cur:
            perc = (100*row[0])/total
            print('{:3} | {:15} | {:f} %'.format(row[0],row[1],perc))

        print('\nNUMBER of MOVIE BY YEAR')
        cur.execute('select count(m.name), m.year from {tn} m group by year order by count(m.name) DESC'.format(tn=table))
        for row in cur:
            perc = (100*row[0])/total
            print('{:3} | {} | {:f} %'.format(row[0],row[1],perc))

        cur.close()
        db.close()
    except:
        print('Une erreur est survenue lors de la lecture de la base')
        exit(1)

def plot_base(DB_filepath, table):
    genre = []
    dat   = []
    tmp   = []
    explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    db = sqlite3.connect(DB_filepath)
    cur = db.cursor()

    cur.execute('select count(m.name), m.genre from {tn} m group by genre order by count(m.name) DESC'.format(tn=table))
    for row in cur:
        genre.append(row[1])
        dat.append(row[0])

    cur.execute('select count(distinct m.genre) from {tn} m'.format(tn=table))
    for row in cur:
        nb_genre = row[0]

    for i in range(nb_genre):
        tmp.append(i+1)

    plt.bar(tmp, dat, align='center')
    plt.xticks(tmp, genre)
    plt.show()

    cur.close()
    db.close()
