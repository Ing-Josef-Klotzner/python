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

"""
"""

def hackerrankInString (s):
    hack = "hackerrank"
    ptr = 0
    for c in s:
        if c == hack [ptr]: ptr += 1
        if ptr == 10: return "YES"
    return "NO"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s = input ()
        result = hackerrankInString (s)
        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
