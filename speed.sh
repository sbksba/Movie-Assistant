#!/bin/bash
#speed.sh

path="data/zero"
time python main.py -d $path -n zero
touch data/zero/The_Matrix.avi
time python main.py -d $path -n zero
rm -f data/zero/The_Matrix.avi
