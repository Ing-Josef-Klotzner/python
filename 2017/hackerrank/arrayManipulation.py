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
#from collections import defaultdict
#from time import time
from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
5 3
1 2 100
2 5 100
3 4 100
Output
200

10 4
2 6 8
3 5 7
1 8 1
5 9 15
output
31

5 3
1 2 100
2 5 100
3 4 100
output
200

4 3
2 3 603
1 1 286
4 4 882
output
882
"""
# lazy add in operation array
def add (arr, N, lo, hi, val):
    arr [lo] += val
    if (hi + 1 < N):
        arr [hi + 1] -= val
  
# Utility method to get actual
# array from operation array
def updateArray (arr, N):
    # convert array from prefix sum array to final
    # and return maximum value
    mx = 0
    for i in range (1, N):
        arr [i] += arr [i - 1]
        mx = max (mx, arr [i])
#    printArr (arr)
    return mx

# method to print final updated array
def printArr (arr):
    print (" ".join (map (str, arr)))

def arrayManipulation (n, queries):
    arr = [0] * n
    # for speed and not needed for result to manipulate the whole array
    # just add value to lower edge and -value to higher edge
    # to get final array convert prefix sum array to final array
    for a, b, k in queries:
        add (arr, n, a - 1, b - 1, k)
    mx = updateArray (arr, n)
    return mx

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    try:
        n, m = map (int, input ().split ())
    except KeyboardInterrupt: exit ()
    queries = []
    for _ in range (m):
        queries.append (list (map (int, input ().rstrip ().split ())))
    result = arrayManipulation (n, queries)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
