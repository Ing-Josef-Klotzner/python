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
from sys import setrecursionlimit
from math import factorial

setrecursionlimit (11000)

def extraLongFactorials (n, res = 1):
#    # recursion with accumulator
#    if n == 1: return res
#    return extraLongFactorials (n - 1, res * n)

#    # recursion without accumulator
#    if n == 1: return 1
#    return n * extraLongFactorials (n - 1)

#    res = n
#    while n > 1:
#        n -= 1
#        res *= n
#    return res

    return factorial (n)

def main ():
    n = int (input ())
    print (repr (extraLongFactorials (n)))

if __name__ == '__main__':
    main ()
