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

def gridSearch (G, R, C, P, r, c):
    for y in range (R - r + 1):
        for x in range (C - c + 1):
            if P [0] != G [y] [x : x + c]:
                continue
            elif r > 1:
                Yes = True
                for y_ in range (1, r):
                    Yes = Yes and P [y_] == G [y + y_] [x : x + c]
                if Yes: return "YES"
    return "NO"
                
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        [R, C] = map (int, input ().split ())
        G = []
        for _ in range (R):
            m = input ()
            G.append (m)
        [r, c] = map (int, input ().split ())
        P = []
        for _ in range (r):
            m = input ()
            P.append (m)
        result = gridSearch (G, R, C, P, r, c)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
