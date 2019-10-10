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
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def cavityMap (n, grid):
    result = grid [ : ]  # copy grid to result
    for y in range (1, n - 1):
        for x in range (1, n - 1):
            cav = grid [y] [x]
            if (cav > grid [y - 1] [x] and
                cav > grid [y + 1] [x] and
                cav > grid [y] [x - 1] and
                cav > grid [y] [x + 1]):
                result [y] = result [y] [ : x] + 'X' + result [y] [x + 1 : ]
    return result

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    grid = []
    for _ in range (n):
        m = input ()
        grid.append (m)
    result = cavityMap (n, grid)
    fptr.write ('\n'.join (result))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
