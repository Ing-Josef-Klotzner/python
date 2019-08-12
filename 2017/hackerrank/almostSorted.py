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

def almostSorted (n, A):
    As = A [:]
    As.sort ()
    # find out unequal positions
    uep = []
    for i in range (n):
        if A [i] != As [i]:
            uep.append (i)
    ln = len (uep)
    if uep == []: return "yes"
    elif ln == 2:
        return "yes\nswap " + str (uep [0] + 1) + " " + str (uep [1] + 1)
    else:
        b = uep [0]
        e = uep [-1] + 1
        if A [b:e] [::-1] == As [b:e]:
            return "yes\nreverse " + str (b + 1) + " " + str (e)
        else: return "no"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    A = list (map (int, input ().rstrip ().split ()))
    result = almostSorted (n, A)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
