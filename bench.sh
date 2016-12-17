#!/bin/bash
#bench.sh

#./clean.sh
path="data/marylou"
echo "PRINT"
python main.py -d $path -n marylou -p movie
echo ""
echo "THEATER"
python main.py -d $path -n marylou -a nowPlaying
echo ""
echo "STAT"
python main.py -d $path -n marylou -s terminal -t movie
echo ""
echo "WEB"
python main.py -d $path -n marylou -w all -t movie
#touch $path/The_Matrix.avi
touch $path/Lucy.avi
echo ""
echo "UPDATE"
python main.py -d $path -n marylou -p movie
echo ""
echo "ERASE"
#python main.py -d $path -e marylou
