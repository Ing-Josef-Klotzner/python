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
from sys import maxsize
from bisect import bisect_left as bLeft, bisect_right as bRight
from collections import defaultdict

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
6
a b c aa d b
1 2 3 4 5 6
3
1 5 caaab
0 4 xyz
2 4 bcdybc
out:
0 19

tc6 expected out: 239720795 3131903231
tc7 expected out: 0 7353994
tc14 expected out: 5042937153 8619278502
"""

def determiningDNAhealth (n, g, h, fldL):
    # create dict of genes
    # px ... initial position (index start 1);   h ... health
    # values: [(p1, h1), (p2, h2), ... ]
    genD = defaultdict (lambda: [[], [0]])
    subs = set ()
    mxLen = 0
    for ix in range (n):
        gen = g [ix]; lg = len (gen)
        genD [gen] [0].append (ix)
        for j in range (1, lg + 1): subs.add (gen [ : j])
        mxLen = max (mxLen, lg)
    for v in genD.values ():
        lv = len (v [0])
        for i in range (lv):
            v [1].append (v [1] [i] + h [v [0] [i]])
    mn = maxsize; mx = 0
#    print ("dict max content length", mxLen)
#    print ("dict length", len (genD))
#    print (genD)
    for f, l, d in fldL:
        ln = len (d)
        sm = 0
        for i in range (ln):
            for j in range (1, mxLen + 1):
                if i + j > ln: break
                gn = d [i : i + j]
                if gn not in subs: break
                if gn not in genD: continue
#                print (i, j, gn)
                # eveluate precomputed healthes
                ids, hs = genD [gn]
                sm += hs [bRight (ids, l)] - hs [bLeft (ids, f)]
        mn = min (sm, mn)
        mx = max (sm, mx)
    return str (mn) + " " + str (mx)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    genes = input ().rstrip ().split ()
    health = list (map (int, input ().rstrip ().split ()))
    s = int (input ())
    fldL = []
    for _ in range (s):
        [first, last, d] = input ().split ()
        fldL.append ((int (first), int (last), d))
    result = determiningDNAhealth (n, genes, health, fldL)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
