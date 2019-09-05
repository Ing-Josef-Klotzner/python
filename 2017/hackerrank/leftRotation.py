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
5 4
1 2 3 4 5

Output
5 1 2 3 4
"""
def leftRotation (a, d):
    return a [d : ] + a [ : d]

def main ():
#    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n, d = map (int, input ().rstrip ().split ())
    # reduce rotation to less than one
    d = d % n
    a = list (map (int, input ().rstrip ().split ()))
    result = leftRotation (a, d)
    print (" ".join (map (str, result)))
#    fptr.write ('\n'.join (map (str, result)))
#    fptr.write ('\n')
#    fptr.close ()

if __name__ == '__main__':
    main ()
