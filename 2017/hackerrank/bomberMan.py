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
def findOccurrences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]
def bombS(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

"""
0: B
.......
...O.O.
....O..
..O....
OO...OO
OO.O...
1:
.......
...O.O.
....O..
..O....
OO...OO
OO.O...
2: (Full)
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
3: Boom B
OOO.O.O
OO.....
OO....O
.......
.......
.......
4: D (Full)
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
OOOOOOO
5: 
.......
...O.O.
...OO..
..OOOO.
OOOOOOO
OOOOOOO
"""
def bomberMan (r, c, n, grid):
    if n == 1: return grid
    afgrid = []
    for i in range (r):
        afgrid.append ('O' * c)
    if n % 2 == 0: return afgrid
    fgrid = []
    for i in range (r):
        fgrid.append ('O' * c)
    # let bombs of grd blow
    def bombGrd (grd):
        grd_ = [""] * (r) 
        for y in range (r):
            for x in range (c):
                if (y < (r - 1) and grd [y + 1] [x] == 'O'
                    or x > 0 and grd [y] [x - 1] == 'O'
                    or grd [y] [x] == 'O' 
                    or x < (c - 1) and grd [y] [x + 1] == 'O'
                    or y > 0 and grd [y - 1] [x] == 'O'):
                    grd_ [y] += '.'
                else:
                    grd_ [y] += fgrid [y] [x]
        return grd_
    grid2 = bombGrd (grid)
    if n % 4 == 3: return grid2
    grid3 = bombGrd (grid2)
    if n % 4 == 1: return grid3

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [r, c, n] = map (int, input ().split ())
    grid = []
    for _ in range (r):
        im = input ()
        grid.append (im)
    result = bomberMan (r, c, n, grid)
    fptr.write ('\n'.join (result))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
