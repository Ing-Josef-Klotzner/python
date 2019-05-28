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
#from math import ceil
from array import array
#from time import sleep

#setrecursionlimit (11000)

def cutTheSticks (arr):
    arry = array ('H', sorted (arr))
    res = []
    while len (arry):
        i = 0
        res.append (len (arry))
        print (arry, len (arry))
        # on sorted list minimum element always first
        cut_len = arry [0]
        while i < len (arry):
            v = arry [i]
            arry [i] = v - cut_len if v - cut_len >= 0 else 0
            if not arry [i]: arry.pop (i) 
            else : i += 1
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = cutTheSticks (arr)
    print ("\n", result)
    fptr.write ('\n'.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
