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
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def countingSort (l):
    n = len (l)
    c = [0] * 100
    for i in l:
        c [i] += 1
    res = []
    for i, ct in enumerate (c):
        if ct:
            res += [i] * ct
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque (map (int, input ().rstrip ().split ()))
    result = countingSort (arr)
    fptr.write (" ".join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
