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
from math import log
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def minimumDistances (n, a):
    min_ = 1000
    if n < 100:
        d = dict ()
        for i, x in enumerate (a):
            if x in d: min_ = min (i - d [x], min_)
            else: d [x] = i
    else:
        d = [1000] * 100001
        for i, x in enumerate (a):
            if d [x] != 1000: min_ = min (i - d [x], min_)
            else: d [x] = i
    return -1 if min_ == 1000 else min_

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    a = list (map (int, input ().rstrip ().split ()))
    result = minimumDistances (n, a)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
