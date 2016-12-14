#!/bin/bash
#bench.sh

./clean.sh
path="data/Small/"
echo "PRINT"
python main.py -d $path -n zero -p movie
echo ""
echo "THEATER"
python main.py -d $path -n zero -a nowPlaying
echo ""
echo "STAT"
python main.py -d $path -n zero -s terminal -t movie
echo ""
echo "WEB"
python main.py -d $path -n zero -w all -t movie
touch $path/The_Matrix.avi
touch $path/Lucy.avi
echo ""
echo "UPDATE"
python main.py -d $path -n zero -p movie
echo ""
echo "ERASE"
python main.py -d $path -e zero
