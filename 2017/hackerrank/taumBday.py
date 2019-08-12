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

def taumBday (b, w, bc, wc, z):
    # ensure black cost lower or equal white cost
    if bc > wc:
        bc, wc = wc, bc
        b, w = w, b
    if bc + z < wc:
        return bc * b + (bc + z) * w
    else:
        return bc * b + wc * w

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        [b, w] = list (map (int, input ().split ()))
        [bc, wc, z] = list (map (int, input ().split ()))
        result = taumBday (b, w, bc, wc, z)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
