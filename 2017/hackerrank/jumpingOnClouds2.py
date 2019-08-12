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

def jumpingOnClouds (n, c):
    i = 0
    s = 0
    while i < n - 2:
        if c [i + 2] == 1:
            i += 1
        else: i += 2
        s += 1
    if i == n - 2: s += 1
    return s

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input())
    c = list (map (int, input ().rstrip ().split ()))
    result = jumpingOnClouds (n, c)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
