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

def fairRations (n, B):
    brd = 0; gvn = False
    for i in range (n - 1):
        if B [i] % 2:
#            print ("ungerade", B [i])
            if not gvn:
                brd += 2
                gvn = True
            else: gvn = False
        else:
#            print ("gerade")
            if gvn:
                brd += 2  # gvn stays True
#        print (i, B [i], brd, gvn)
    if not B [n - 1] % 2:
        if gvn: return "NO"
    return brd

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    B = list (map (int, input ().rstrip ().split ()))
    result = fairRations (n, B)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
