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

"""
"""
def beautifulBinaryString (s, n):
    if n < 2: return 0
    cnt = 0
    for i in range (2, n):
        if s [i - 2] == '0' and s [i - 1] == '1' and s [i] == '0':
            s [i] = '1'
            cnt += 1
    return cnt

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    s = list (input ())
    result = beautifulBinaryString (s, n)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
