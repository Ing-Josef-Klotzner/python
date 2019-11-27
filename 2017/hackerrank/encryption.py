#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

from os import environ
from math import ceil, floor
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def encryption (s):
    # remove blanks from string
    s = s.replace (" ", "")
    l = len (s)
    # find grid
    lw = l ** .5
    rows = floor (lw); cols = rows
    if rows * cols < l:
        cols = ceil (lw)
    if rows * cols < l:
        rows = cols
    print (rows, cols, l)
    encT = ""
    for c in range (cols):
        for r in range (rows):
            p = c + cols * r
            if p < l:
                encT += s [p]
        if c != cols - 1:
            encT += ' '
    return encT

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = encryption (s)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
