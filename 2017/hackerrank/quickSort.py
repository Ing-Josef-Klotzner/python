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

def quickSort (l):
    n = len (l)
    if n < 2:
        return l
    pivot = l [0]
    left = []; equal = [pivot]; right = []
    for i in range (1, n):
        curr = l [i]
        if curr < pivot: left.append (curr)
        elif curr > pivot: right.append (curr)
        else: equal.append (curr)
    return quickSort (left) + quickSort (equal) + quickSort (right)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque (map (int, input ().rstrip ().split ()))
    result = quickSort (arr)
    fptr.write (" ".join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
