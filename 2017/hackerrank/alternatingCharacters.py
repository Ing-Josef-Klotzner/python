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
def alternatingCharacters (s):
    ln = len (s)
    dels = 0
    if ln == 0: return 0
    for i in range (1, ln):
        if s [i] == s [i - 1]:
            dels += 1
    return dels 
        

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    for i in range (n):
        s = input ()
        result = alternatingCharacters (s)
        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
