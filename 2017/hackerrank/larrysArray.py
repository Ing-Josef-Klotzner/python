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
from functools import reduce
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def larrysArray (n, A):
    return "NO" if sum ([1 for i in range (n) 
        for j in range (i + 1, n) if A [i] > A [j]]) % 2 else "YES"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        n = int (input ())
        A = list (map (int, input ().rstrip ().split ()))
        result = larrysArray (n, A)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
5
12
9 6 8 12 3 7 1 11 10 2 5 4
21
17 21 2 1 16 9 12 11 6 18 20 7 14 8 19 10 3 4 13 5 15
15
5 8 13 3 10 4 12 1 2 7 14 6 15 11 9
13
8 10 6 11 7 1 9 12 3 5 13 4 2
18
7 9 15 8 10 16 6 14 5 13 17 12 3 11 4 1 18 2

NO
YES
NO
YES
NO
"""
