MovieAssistant
==============

[![Build Status](https://travis-ci.org/sbksba/Movie-Assistant.svg?branch=master)](https://travis-ci.org/sbksba/Movie-Assistant)

Synopsis
--------

> It is a python module to create and manage the movies of a user (or several).
> This module creates a database of user's films as well a recommendation database, the module also allows the user to access to the information of movies played in the cinema.   

Usage
-----

> _Create a profile_  
    `python main.py -d data/Small/ -n ZERO`

> _Print the data base movie for a profile_
    `python main.py -d data/Small/ -n ZERO -p movie`

> _Print the data base movie for a profile in a web page_
    `python main.py -d data/Small/ -n ZERO -w all -t movie`

> _Print the stats for the data base movie of a profile_
    `python main.py -d data/Small/ -s terminal -t movie`

> _Delete a profile_
    `python main.py -d data/Small/ -e ZERO`

> _Print the movies currently playing at the movie theater_
    `python main.py -d data/Small/ -s terminal -t movie`

## Licence

(Licence MIT)

Copyright © 2016 sbksba

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
