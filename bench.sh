#!/bin/bash
#bench.sh

./clean.sh
path="data/Small/"
echo "PRINT"
python main.py -d $path -n ZERO -p movie
echo ""
echo "THEATER"
python main.py -d $path -n ZERO -a nowPlaying
echo ""
echo "STAT"
python main.py -d $path -n ZERO -s terminal -t movie
echo ""
echo "WEB"
python main.py -d $path -n ZERO -w all -t movie
touch $path/The_Matrix.avi
touch $path/Lucy.avi
echo ""
echo "UPDATE"
python main.py -d $path -n ZERO -p movie
echo ""
echo "ERASE"
python main.py -d $path -e ZERO
