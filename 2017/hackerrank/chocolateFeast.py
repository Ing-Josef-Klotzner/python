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

def chocolateFeast (n, c, m):
    res = 0
    papierln = n // c
    papierlnR = 0
    while papierln + papierlnR >= m:
        res += papierln
        pap_old = papierln + papierlnR
        papierln = (papierlnR + papierln) // m
        papierlnR = pap_old % m
    res += papierln
    return res 

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        [n, c, m] = map (int, input ().split ())
        result = chocolateFeast (n, c, m)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
