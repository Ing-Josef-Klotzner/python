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

def happyLadybugs (n, b):
# NO:
# There are at least one empty cell and there is no Letter with count 1
# OR
# There is no empty cell but the given string is happy
    # fast count list (fcL) for characters
    fcL = [0] * 27 
    for i in range (n):
        a = b [i]
        if a != "_":   # ascii "A" = 65
            fcL [ord (a) - 65] += 1
        else: fcL [26] = 1
#    print (fcL)
    for a in set (b):
        print (a)
        if a != "_" and fcL [ord (a) - 65] == 1:
            return "NO"
    if fcL [26] == 0:
        for i in range (1, n - 1):
            if b [i] != b [i + 1] and b [i] != b [i - 1]:
                return "NO"
        if n > 1:    # BAAAB  is unhappy
            fptr = ord (b [0]) - 65
            if fcL [fptr] > 1 and b [0] != b [1] and b [0] == b [-1]:
                return "NO"
    return "YES"
                
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    g = int (input ())
    for _ in range (g):
        n = int (input ())
        b = input ().strip ()
        result = happyLadybugs (n, b)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
