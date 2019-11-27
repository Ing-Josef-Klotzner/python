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
#from collections import deque

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
1
abcdcbax
out: 7
1
hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh
out: 44
"""

def palindromeIndex (p):
    ln = len (p)
    mid = ln // 2   #- (ln + 1) % 2
    sft_l = 0
    sft_r = 0
    pos = 0
    # odd / even ?
    for i in range (mid):
        if p [i + sft_l] == p [ln - 1 - i - sft_r]:
            continue
        if not sft_l and not sft_r:
            if p [i + 1] == p [ln - 1 - i] and i < mid - 1 and p [i + 2] == p [ln - 2 - i] or i == mid - 1 and p [i + 1] == p [ln - 1 - i]:
                sft_l += 1
                pos = i
                continue
            if p [i] == p [ln - 2 - i] and i < mid - 1 and p [i + 1] == p [ln - 3 - i] or i == mid - 1 and p [i] == p [ln - 2 - i]:
                sft_r += 1
                pos = ln - 1 - i
                continue
        return -1
    return pos if sft_l or sft_r else -1

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        p = input ()
        result = palindromeIndex (p)
        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
