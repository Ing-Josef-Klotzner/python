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

def gameOfThrones (s):
    ln = len (s)
    odd = ln % 2
    ms = Counter (s)
    onceOdd = False
    for v in ms.values ():
        if not onceOdd and v % 2:
            onceOdd = True
            continue
        if v % 2: return "NO"
    return "YES"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = gameOfThrones (s)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
