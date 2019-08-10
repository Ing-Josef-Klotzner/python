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
def makeArrayConsecutive2 (n):
    ln = len (n)
    if ln < 2: return 0
    srtd = sorted (n)
    res = 0
    for i in range (1, len (n)):
        res += srtd [i] - srtd [i - 1] - 1
    return res
        
def main ():
    statues = list (map (int, input ().split ()))
    print (makeArrayConsecutive2 (statues))

if __name__ == '__main__':
    main ()
