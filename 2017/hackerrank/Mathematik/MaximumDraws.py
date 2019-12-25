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
#from bisect import bisect_right
#from math import factorial as fac
#from collections import deque   #, defaultdict
#from time import time   #sleep
#from functools import reduce
#from copy import deepcopy
#from operator import mul
#from itertools import product, combinations
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

def maximumDraws (n):
    if n == 1: return 2
    breakeven = n
    return n + 1

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        n = int ( input ())
        result = maximumDraws (n)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

