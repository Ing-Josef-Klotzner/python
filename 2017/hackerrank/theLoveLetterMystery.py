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
def theLoveLetterMystery (s):
    n = len (s)
    if n < 2: return 0
    cnt = 0
    for i in range (n // 2):
        fr = s [i]
        bk = s [n - i - 1]
        if fr != bk:
            cnt += abs (ord (fr) - ord (bk))
    return cnt

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s = input ()
        result = theLoveLetterMystery (s)
        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
