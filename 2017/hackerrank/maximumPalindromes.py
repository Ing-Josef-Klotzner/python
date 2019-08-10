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
from collections import Counter
from math import factorial

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
week
2
1 4
2 3
out:
2
1
"""
#def initialize (s):
    # This function is called once before all queries.

def maximumPalindromes (s):
    cnt = Counter (s)
#    print (cnt)
    dvn = 0
    dvr = 1
    nofc = 0   # number of odd frquency characters - middle of palindrome
    for k in cnt:
        v = cnt [k]
        vh = v // 2
        dvn += vh
        if vh: dvr *= factorial (vh)
        if v % 2: nofc += 1
    nofc = max (1, nofc)
#    print (dvn, dvr, nofc)
    return (factorial (dvn) // dvr * nofc) % (10 ** 9 + 7)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = list (input ())
#    initialize (s)
    q = int (input ())
    for _ in range (q): # q
        [l, r] = list (map (int, input ().split ()))
        s1 = s [l - 1 : r]
#        print (s1)
        result = maximumPalindromes (s1)
#        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
