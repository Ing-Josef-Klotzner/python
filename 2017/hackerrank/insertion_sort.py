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

def insertion_sort (l):
    for i in range (1, len (l)):
        j = i - 1
        key = l [i]
        while (j >= 0) and (l [j] > key):
           l [j + 1] = l [j]
           j -= 1
        l [j + 1] = key
    return l

def main ():
#    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque (map (int, input ().rstrip ().split ()))
    insertion_sort (arr)
    print (" ".join (map (str, arr)))
#    fptr.write (str (result) + '\n')
#    fptr.close ()

if __name__ == '__main__':
    main ()
