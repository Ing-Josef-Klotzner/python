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
from collections import Counter

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
"""

def twoStrings (s1, s2):
    ms1 = Counter (s1)
    ms2 = Counter (s2)
    diff = ms1 - ms2
    print (ms1)
    print (diff)
    return "YES" if ms1 != diff else "NO"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s1 = input ()
        s2 = input ()
        result = twoStrings (s1, s2)
        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
