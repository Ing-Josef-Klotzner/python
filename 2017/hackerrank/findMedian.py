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

def findMedian (n, l):
    l.sort ()
    return l [n // 2]

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = findMedian (n, arr)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
