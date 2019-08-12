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
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def equalizeArray (n, c):
    ctL = [0] * 101
    maxv = 0
    for v in c:
        ctL [v] += 1
        maxv = max (maxv, ctL [v])
    return n - maxv

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input())
    c = list (map (int, input ().rstrip ().split ()))
    result = equalizeArray (n, c)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
