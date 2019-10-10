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
#from collections import deque

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
"""

def camelCase (s):
    ln = len (s)
    r = 1 if s else 0
    for i in range (len (s)):
        c = s [i]
        if c == c.upper ():
            r += 1
    return r

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = camelCase (s)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
