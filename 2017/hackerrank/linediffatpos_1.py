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

from sys import stdin
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
"""
#def linediffatpos (a, b):
#    pos = 0
#    return pos
def main ():
    af = stdin
    bf = stdin
    al = []; bl = []
    for i in range (1):
        al.append (af.readline ())
    for i in range (1):
        bl.append (bf.readline ())
    for i in range (1):
        lal = len (al [i]); lbl = len (bl [i])
        pos = 0
        if lal <= lbl: l = lal
        else: l = lbl
        for p in range (l):
            if al [i] [p] != bl [i] [p]: break
        print ("a", al [i] [ : 20])
        print ("b", bl [i] [ : 20])
        print ("first difference at position", p + 1)
        print ("length of a", lal, "length of b", lbl)
#    result = linediffatpos (a, b)
#    print (result)

if __name__ == '__main__':
    main ()
