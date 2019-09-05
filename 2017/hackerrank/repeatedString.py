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

def countA (s):
    ct = 0
    for i in s:
        if i == 'a': ct += 1
    return ct

def repeatedString (s, n):
    ln = len (s)
    lastAs = countA (s [ : n % ln])
    return countA (s) * (n // ln) + lastAs

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    n = int (input())
    result = repeatedString (s, n)
    print ("\n", result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
