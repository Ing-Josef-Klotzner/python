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
"""
"""
def almostIncreasingSequence (sq):
    ls = len (sq)
    # fst occurance of not being in strictly increasing sequence
    fst = rc = False
    if sq [1] <= sq [0]: fst = True
    for i in range (2, ls):
        if rc:
            rc = False
            if sq [i] <= sq [i - 2]: return False
        elif sq [i] <= sq [i - 1]:
            if fst: return False
            else: fst = True
        if fst and sq [i] <= sq [i - 2]: rc = True
        # "take left out": check with i - 2 now
        #                   if <= : right check (rc) = True
        # "take right out": if rc: next check with i - 2
    return True
        
def main ():
    sequence = list (map (int, input ().split ()))
    print (almostIncreasingSequence (sequence))

if __name__ == '__main__':
    main ()
