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
#from collections import deque
from sys import stdin

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
tc1 ... 268
"""

def lilysHomework (arr, n):
    pos = {}
    for i, num in enumerate (arr):
        pos [num] = i
    cnt = 0
    srtd_arr = sorted (arr)
    for i in range (n):
        if arr [i] != srtd_arr [i]:
            cnt += 1
            oth_idx = pos [srtd_arr [i]]
            pos [arr [i]] = oth_idx
            arr [i], arr [oth_idx] = arr [oth_idx], arr [i]
    return cnt

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    #arr = list (map (int, stdin.readline ().rstrip ().split ()))
    arr = [int (x) for x in stdin.readline ().rstrip ().split ()]
    asc = lilysHomework (arr [ : : ], n)
    desc = lilysHomework (arr [ : : -1], n)
    result = min (asc, desc)
    print (result, asc, desc)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
