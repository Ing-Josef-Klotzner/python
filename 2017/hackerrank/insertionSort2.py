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
from collections import deque
from itertools import islice
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def out_arr (ar):
    for i in ar:
        print (i, end = " ")
    print ()

def insertionSort1 (ar):
    n = len (ar)
    if len (ar) == 1: return ar
    for i in range (n - 2, - 1, -1):
        if ar [-1] >= ar [i]:
            ar.insert (i + 1, ar.pop ())
            return ar
    ar.insert (i, ar.pop ())
    return ar

def insertionSort2 (n, arr):
    for i in range (2, n + 1):
        a = deque (islice (arr, 0, i))
        b = deque (islice (arr, i, n))
        arr = insertionSort1 (a) + b
        out_arr (arr)
                
def main ():
#    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque (map (int, input ().rstrip ().split ()))
    insertionSort2 (n, arr)
#    fptr.write (str (result) + '\n')
#    fptr.close ()

if __name__ == '__main__':
    main ()
