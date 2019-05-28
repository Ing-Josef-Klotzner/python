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

def hurdleRace (k, height):
    res = max (height) - k
    return res if res >= 0 else 0
    
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    nk = input().split ()
    n = int (nk [0])
    k = int (nk [1])
    height = list (map (int, input ().rstrip ().split ()))
    result = hurdleRace (k, height)
    print (result)
    fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
