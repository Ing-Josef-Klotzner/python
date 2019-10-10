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
6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
out:
3
1
-1
2
0
1
"""

def anagram (s):
    ln = len (s)
    lh = ln // 2
    if ln % 2: return -1
    s1 = s [ : lh]
    s2 = s [lh : ]
    res = 0
    s2i = [0] * 26
    for i in range (lh):
        s2i [ord (s2 [i]) - ord ('a')] += 1
    for i in range (lh):
        ix = ord (s1 [i]) - ord ('a')
        if s2i [ix]:
            s2i [ix] -= 1
        else:
            res += 1
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    for _ in range (q):
        s = input ()
        result = anagram (s)
        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
