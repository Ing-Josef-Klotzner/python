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
from bisect import bisect

#    position = bisect.bisect_left(l, r)
#    bisect.insort_left(l, r)

def utopianTree (n):
    res = 1
    for i in range (1, n + 1):
        if i % 2: res *= 2
        else: res += 1
    return res


def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    t = int (input())
    for t_itr in range (t):
        n = int (input ())
        result = utopianTree (n)
        print (result)
        fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
