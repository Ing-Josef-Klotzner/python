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
from collections import defaultdict
from time import time
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Output
2
1
0
"""
def sparseArrays (strings, queries):
    res = []
    sD = defaultdict (int)
    print (type (sD [0]))
    for s in strings:
        sD [s] += 1
    for q in queries:
        if q in sD:
            res.append (sD [q])
        else: res.append (0)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    sc = int (input ())
    strings = []
    for _ in range (sc):
        si = input ()
        strings.append (si)
    qc = int (input ())
    queries = []
    for _ in range (qc):
        qi = input ()
        queries.append (qi)
    result = sparseArrays (strings, queries)
    fptr.write ('\n'.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
