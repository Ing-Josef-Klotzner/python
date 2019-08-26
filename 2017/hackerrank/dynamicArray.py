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
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
out:
5
7
"""

def query1 (x, y, n, seqL, lastA):
    seq_ix = (x ^ lastA) % n
    seqL [seq_ix].append (y)
def query2 (x, y, n, seqL, lastA):
    seq_ix = (x ^ lastA) % n
    size = len (seqL [seq_ix])
    return seqL [seq_ix] [y % size]   #  returning new lastA
    

def dynamicArray (n, q):
    seqL = [[] for _ in range (n)]
    lastA = 0
    resL = []
    for q_nr, x, y in q:
        if q_nr == 1:
            query1 (x, y, n, seqL, lastA)
        else:
            lastA = query2 (x, y, n, seqL, lastA)
            resL.append (lastA)
    return resL

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n, q = map (int, input ().rstrip ().split ())
    qs = []
    for _ in range (q):
        qs.append (list (map (int, input ().rstrip ().split ())))
    result = dynamicArray (n, qs)
#    print (result)
    fptr.write ('\n'.join (map (str, result)))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
