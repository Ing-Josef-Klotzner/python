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

def serviceLane (n, width, cases):
    res = []
    for cs in cases:
        res.append (min (width [cs [0] : cs [1] + 1]))
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, t] = map (int, input ().split ())
    width = list (map (int, input ().rstrip ().split ()))
    cases = []
    for _ in range (t):
        cases.append (list (map (int, input ().rstrip ().split ())))
    result = serviceLane (n, width, cases)
    fptr.write ('\n'.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
