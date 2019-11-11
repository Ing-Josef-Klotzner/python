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
#from itertools import permutations, combinations, product
#from bisect import bisect_right, bisect_left
#from math import factorial as fac
#from collections import deque   #, defaultdict
#from time import time   #sleep
from functools import reduce
from operator import add    #mul
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

def get_z_arr (s, n):
    n = len (s)
    z = [0] * n
    return get_zarr (s, z)

def get_zarr (string, z):
    n = len (string)
    z [0] = n
    l, r, k = 0, 0, 0
    for i in range (1, n):
        if i > r:
            l, r = i, i
            while r < n and string [r - l] == string [r]: r += 1
            z [i] = r - l
            r -= 1
        else:
            k = i - l
            if z [k] < r - i + 1: z [i] = z [k]
            else:
                l = i
                while r < n and string [r - l] == string [r]:
                    r += 1
                z [i] = r - l
                r -= 1
    return z

def stringSimilarity (s):
    n = len (s)
    z = get_z_arr (s, n)

    # debug part
#    print (z)

    return reduce (add, z)
        

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        s = input ().rstrip ()
        result = stringSimilarity (s)
#        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
Create Z Array

The idea is to maintain an interval [L, R] which is the interval with max R
such that [L,R] is prefix substring (substring which is also prefix).

Steps for maintaining this interval are as follows –

1) If i > R then there is no prefix substring that starts before i and ends
   after i, so we reset L and R (to i) and compute new [L,R] by comparing
   str[0..] to str[i..] and get Z[i].

2) If i <= R then let K = i-L,  now Z[i] >= min(Z[K], R-i+1)  because
   str[i..] matches with str[K..] for atleast R-i+1 characters (they are in
   [L,R] interval which we know is a prefix substring).
   Now two sub cases arise –
      a) If Z[K] < R-i+1  then there is no prefix substring starting at
         str[i] (otherwise Z[K] would be larger)  so  Z[i] = Z[K]  and
         interval [L,R] remains same.
      b) If Z[K] >= R-i+1 then it is possible to extend the [L,R] interval
         thus we will set L as i and start matching from str[R]  onwards  and
         get new R then we will update interval [L,R] and calculate Z[i].
"""
