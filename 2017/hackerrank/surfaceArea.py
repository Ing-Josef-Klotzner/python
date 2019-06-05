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
from math import log
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def surfaceArea (H, W, A):
    # Pad the grid width a layer of 0 for easier calculation
    a = [[0] * (W + 2)]
    for row in A:
        a.append ([0] + row + [0])
    a.append ([0] * (W + 2))
    # bottom and top are fix
    res = H * W * 2
    # Side area is just the sum of differences between adjacent cells
    for y in range (1, H + 2):
        for x in range (1, W + 2):
            res += abs (a [y] [x] - a [y - 1] [x])
            res += abs (a [y] [x] - a [y] [x - 1])
    return res
    
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [H, W] = map (int, input ().split ())
    A = []
    for _ in range (H):
        A.append (list (map (int, input ().rstrip ().split ())))
    result = surfaceArea (H, W, A)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
