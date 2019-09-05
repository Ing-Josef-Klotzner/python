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
from itertools import combinations
#from collections import deque

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
"""
# returns True if char is a-z or A-Z (u = True)
def isAZ (c, u):
    oc = ord (c)
    if u:   # upper case
        if oc > 64 and oc < 91: return True
    else: 
        if oc > 96 and oc < 123: return True
    return False

def caesarCypher (s, k, n):
    res = ""
    for i in range (n):
        c = s [i]
        if isAZ (c, True):
            res += chr ((ord (c) - 65 + k) % 26 + 65)
        elif isAZ (c, False):
            res += chr ((ord (c) - 97 + k) % 26 + 97)
        else res += c
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    s = input ()
    k = int (input ())
    result = caesarCypher (s, k, n)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
