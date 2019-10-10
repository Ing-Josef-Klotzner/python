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
from collections import Counter

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
2
abcd
abab
out:
0
2
"""
def isValid (s):
    ln = len (s)
    print (ln)
    if ln < 2: return "YES"
    # [2, 2, 2, 2, 3, 2, 2, 2]
    counts = list (Counter (s).values ())
    print (counts)
    ccntsMp = Counter (counts)
    # [7, 1]
    ccnts = list (ccntsMp.values ())
    print (ccnts)
    ln1 = len (ccnts)
    if ln1 == 1: return "YES"  # all chars have same count
    if ln1 > 2: return "NO"
    # [2, 3]
    keys = list (ccntsMp.keys ())
    print (keys)
    # if count of count of chars is 1 and count of char is either 1 higher
    # than other count or 1, then "YES"
    if (ccnts [0] == 1 and (keys [0] == keys [1] + 1 or keys [0] == 1) or
        ccnts [1] == 1 and (keys [1] == keys [0] + 1 or keys [1] == 1)):
            return "YES"
    return "NO"
    
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = isValid (s)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
