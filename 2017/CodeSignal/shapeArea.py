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
n
1
out: 1
2
out: 5
3
out: 13
4
out: 25
n:   1, 2, 3,  4  =>  1 + map list from 2nd el by (x - 1) * 4 and sum list
row: 1, 5, 13, 25, 41
diff:  4  8  12  16
diffsum:4 12 24  40  => result = 1 + (1 + (n - 1)) / 2 * (n - 1) * 4 
=> if n == 1: result = 1
else:       2-1     3-1     4-1 
result = 1 + 1 * 4 + 2 * 4 + 3 * 4 ... + (n - 1) * 4
"""
def shapeArea (n):
    return 1 + (1 + (n - 1)) / 2 * (n - 1) * 4
        
def main ():
    n = int (input ())
    print (shapeArea (n))

if __name__ == '__main__':
    main ()
