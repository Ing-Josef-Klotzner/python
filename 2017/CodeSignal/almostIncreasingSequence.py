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
def almostIncreasingSequence (seq):
    ls = len (seq)
    ctr = 0  # count occurance of not being in strictly increasing sequence
    if seq [1] <= seq [0]: ctr += 1
    for i in range (2, ls):
        if seq [i] <= seq [i - 1]: ctr += 1
        if seq [i] <= seq [i - 2]: ctr += 1
        if ctr > 1: return False
    return True
        
def main ():
    sequence = list (map (int, input ().split ()))
    print (almostIncreasingSequence (sequence))

if __name__ == '__main__':
    main ()
