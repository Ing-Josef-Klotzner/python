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
from collections import defaultdict
from time import time
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

19
"""
glass = ((0, 0), (0, 1), (0, 2),
                (1, 1),
        (2, 0), (2, 1), (2, 2))

def glass_sum (a, y, x):
    sum = 0
    for r, c in glass:
        sum += a [r + y] [c + x]
    return sum

def hourglassSum (a):
    mx = -1000
    for y in range (4):
        for x in range (4):
            mx = max (mx, glass_sum (a, y, x))
    return mx    

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range (6):
        arr.append (list (map (int, input ().rstrip ().split ())))
    result = hourglassSum (arr)
#    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
