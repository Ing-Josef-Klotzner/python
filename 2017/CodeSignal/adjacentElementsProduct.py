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
3 6 -2 -5 7 3
out: 21
"""
def adjacentElementsProduct (inputArray):
    if inputArray == []: return 0
    mx = -1000
    it = iter (inputArray)
    prev = 1000 if inputArray [0] < 0 else 0
    for ix, el in enumerate (it):
        try:
            nxt = next (it)
        except StopIteration: nxt = 1000 if el < 0 else 0
        print ("prev", prev, "el", el, "nxt", nxt)
        if prev * el > mx: mx = el * prev
        if el * nxt > mx: mx = el * nxt
        prev = nxt
    return mx
        
def main ():
    inputArray = map (int, input ().split ())
    print (adjacentElementsProduct (inputArray))

if __name__ == '__main__':
    main ()
