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

def closestNumbers (n, l):
    l.sort ()
    diff = 10**20
    for i in range (n - 1): 
        cur_diff = l [i + 1] - l [i]
        if cur_diff < diff: diff = cur_diff 
    res = []
    for i in range (n - 1):
        cur_diff = l [i + 1] - l [i]
        if cur_diff == diff:
            res += [l [i], l [i + 1]]
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = closestNumbers (n, arr)
    fptr.write (" ".join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
