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
from collections import defaultdict
from time import time
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
4
1 4 3 2
"""

def reverseArray (a):
    return a [ : : -1]

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = reverseArray (arr)
#    print (result)
    fptr.write (' '.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
