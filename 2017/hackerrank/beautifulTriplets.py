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

def beautifulTriplets (n, d, arr):
    res = 0
    for i in range (n - 2):
        for j in range (i + 1, n - 1):
            diff1 = arr [j] - arr [i]
            if diff1 < d: continue
            elif diff1 > d: break
            for k in range (j + 1, n):
                print (i, j, k)
                diff2 = arr [k] - arr [j]
                if diff2 < d: continue
                elif diff2 > d: break
                res += 1
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, d] = map (int, input ().split ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = beautifulTriplets (n, d, arr)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
