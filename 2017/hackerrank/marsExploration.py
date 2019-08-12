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

def marsExploration (s):
    ln = len (s)
    error = 0
    for i in range (ln):
        c = s [i]
        im = i % 3
        if ((im == 0 or im == 2) and c != 'S' or
            im == 1 and c != 'O'): error += 1
#        print (i, im, c, error)
    return error

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = marsExploration (s)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
