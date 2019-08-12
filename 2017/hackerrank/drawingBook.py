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

def pageCount (n, p):
    def fromFront ():
        return p // 2
    def fromBack ():
        if n % 2: return (n - p) // 2
        else: return (n - p + 1) // 2
    return min (fromFront (), fromBack ())

if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    p = int (input ())
    result = pageCount (n, p)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()
