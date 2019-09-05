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
from functools import reduce

def reverse (x):
    res = 0
    while (x > 0):
        res = res * 10 + x % 10
        x //= 10
    return res
 
def beautifulDays (i, j, k):
    def func (y, x):
        rx = reverse (x)
        return y if (x - rx) % k else y + 1
    res = reduce (func, range (i, j + 1), 0)
    print (res)
    return res    

def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    ijk = input ().split ()
    i = int (ijk [0])
    j = int (ijk [1])
    k = int (ijk [2])
    result = beautifulDays (i, j, k)
    print ("\n" + str (result))
    fptr.write(str(result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
