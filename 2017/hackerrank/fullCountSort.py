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
from sys import stdin
from functools import reduce
from operator import add
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def countSort (n, l):
    c = [[] for x in range (100)]
    il = 0
    for i, ct in l:
        if il >= n // 2:
            c [int (i)].append (ct)
        else: c [int (i)].append ('-')
        il += 1
    return reduce (add, c)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = deque ()
    for ct in stdin:
        arr.append (ct.split ())
    result = countSort (n, arr)
    fptr.write (" ".join (result))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
