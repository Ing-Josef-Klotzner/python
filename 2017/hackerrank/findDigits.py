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

def findDigits (n):
    n_ = n
    c = 0
    while n_ != 0:
        d = n_ % 10
        if d != 0 and n % d == 0: c += 1
#        print ("d", d)
        n_ //= 10
    return c

def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for t_itr in range (t):
        n = int (input ())
        result = findDigits (n)
        print (result)
        fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
