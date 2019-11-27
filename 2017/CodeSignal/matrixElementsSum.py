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
"""
"""
def matrixElementsSum (mx):  # matrix
    ln = len (mx [0])
    upL = [1] * ln
    res = 0
    for fNr, floor in enumerate (mx):
        for room in range (ln):
            if upL [room] != 0:
                res += floor [room]
#        print (upL)
        for room in range (ln):
            upL [room] *= floor [room]
    return res
    
def main ():
#    sequence = list (map (int, input ().split ()))
    matrix = [[1,1,1,0], 
              [0,5,0,1],
              [2,1,3,10]]
    print (matrixElementsSum (matrix))

if __name__ == '__main__':
    main ()
