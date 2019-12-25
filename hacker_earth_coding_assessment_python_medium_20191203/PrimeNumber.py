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

def main ():
    numString = input ()
    ln = len (numString)
    res = ""
    def nxt_sm (d):
        if d >= '7': return '7'
        elif d >= '5': return '5'
        elif d >= '3': return '3'
        else: return '2'
    # set f.e. 1000 to 999
    for i, c in enumerate (numString):
        if c < '2':
            res += '7' * (ln - 1 - i)
            break
        elif c == '2' or c == '3' or c == '5' or c == '7': res += nxt_sm (c)
        else:
            res += nxt_sm (c) + '7' * (ln - 1 - i)
            break
    print (res)
if __name__ == '__main__':
    main ()

"""
in
9090842252
out
7777777777
"""

