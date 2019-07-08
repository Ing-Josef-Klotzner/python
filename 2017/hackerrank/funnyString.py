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

def funnyString (s):
    ln = len (s)
    for i in range (1, ln // 2 + 1):
        diff = abs (ord (s [i]) - ord (s [i - 1]))
#        print (ln - i, ln - i - 1, " : ",i ,i - 1)
        diffR = abs (ord (s [ln - i - 1]) - ord (s [ln - i]))
#        print (diffR, diff)
        if diff != diffR:
            return "Not Funny"
    return "Funny"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s = input ()
        result = funnyString (s)
        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
