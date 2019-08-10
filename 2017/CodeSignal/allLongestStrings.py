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
def allLongestStrings (arr):
    mxl = 0
    res = []
    for stg in arr:
        lstg = len (stg)
        if lstg > mxl:
            mxl = lstg
            res = [stg]
        elif lstg == mxl: res.append (stg)
    return res

def main ():
#    sequence = list (map (int, input ().split ()))
    arr = ["aba", "aa", "ad", "vcd", "aba"]
    print (allLongestStrings (arr))

if __name__ == '__main__':
    main ()
