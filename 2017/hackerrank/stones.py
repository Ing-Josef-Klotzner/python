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

def stones (n, a, b):
    if a > b:
        a, b = b, a
    res = ""
    rset = set ()
    m = n - 1
    c = m * a
    res += str (c)
    rset.add (c)
    for i in range (1, n):
        c = (m - i) * a + i * b
        if c not in rset:
            res += " "
            res += str (c)
            rset.add (c)
#    print (res, rset)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    for _ in range (n):
        n = int (input ())
        a = int (input ())
        b = int (input ())
        result = stones (n, a, b)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
