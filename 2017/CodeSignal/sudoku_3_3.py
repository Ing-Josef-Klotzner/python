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

from itertools import product
from copy import copy

def is_distinct (list):
    '''Auxiliary function to is_solved
    checks if all elements in a list are distinct
    (ignores 0s though)
    '''
    used = []
    for i in list:
        if i == 0:
            continue
        if i in used:
            return False
        used.append (i)
    return True


def is_valid (brd):
    '''Checks if a 3x3 mini-Sudoku is valid.'''
    for i in range (3):
        row = [brd [i] [0], brd [i] [1], brd [i] [2]]
        if not is_distinct (row):
            return False
        col = [brd [0] [i], brd [1] [i], brd [2] [i]]
        if not is_distinct (col):
            return False
    return True

''' Solves a mini-Sudoku   brd is the board
  empties is the number of empty cells '''
def solve (brd, empties = 9):
    if empties == 0:   #Base case
        return is_valid (brd)
    for row, col in product (range (3), repeat = 2):
        cell = brd [row] [col]   #Run through every cell
        if cell != 0: continue  #If its not empty: ignore
        brd2 = copy (brd)
        for test in [1, 2, 3]:
            brd2 [row] [col] = test
            if is_valid (brd2) and solve (brd2, empties - 1):
                return True
            brd2 [row] [col] = 0   #BackTrack
    return False

def main ():
    Board = [ [ 0 , 0 , 0 ],
              [ 1 , 0 , 0 ],
              [ 0 , 3 , 1 ] ]
    solve( Board , 9 - 3 )

    for row in Board:
        print (row)

if __name__ == '__main__':
    main ()
