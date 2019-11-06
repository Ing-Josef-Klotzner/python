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
from itertools import permutations
from bisect import bisect_right, bisect_left
#from math import factorial as fac
#from collections import deque   #, defaultdict
#from time import time   #sleep
from functools import reduce
#from copy import deepcopy
#from operator import add    #mul
#from itertools import product, combinations
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

N = 10 ** 9 + 7

# calculations for binary indexed tree    
def update (bit, i, v):
    n = len (bit)
    while i < n:
        bit [i] += v
        i += i & (-i)

def getsum (bit, i):
    s = 0
    while i > 0:
        s += bit [i]
        i -= i& (-i)
    return s

def getnP (P, fixed):
    n = len (P)
    m = max (P)
    nI = [0]
    for i in range (2, n + 1):
        nI.append (nI [-1] + fixed [i - 2] ) 
    bit = [0 for i in range (m + 1)]
    nP = [0 for i in range (n)]
    for i in range (n - 1, -1, -1):
        if P [i] > 0:
            nP [i] = nI [P [i] - 1] - getsum (bit, P [i] - 1) 
            update (bit, P [i], 1)  
        else:
            nP [i] = -1
    nP [0] = 0
    return nP
    
def solve (P, n):
    fixed = n * [0]
    for v in P:
        if v > 0 :
            fixed [v-1] = 1
    idZ   = [i for i in range (n) if P [i] == 0]
    idNZ  = [i for i in range (n) if P [i] > 0]
    vP    = [i for i in range (1, n + 1) if not fixed [i - 1]]
    nz    = len (idZ)
    nV, nZ, f = [0], [0], [1]
    for i in range (1, n):
        f.append ( f [-1] * i % N)
        nV.append (nV [-1] + (not fixed [i - 1])) 
        nZ.append (nZ [-1] + (not P [i - 1]))
    f.append (f [-1] * n % N)          
    nP = getnP (P, fixed)
    Tnz = sum ((P [i] - 1 - nP [i]) * f [n - i - 1] for i in idNZ) 
    Tz  = sum ((i - nZ [i]) * f [n - i - 1] for i in idZ)
    S  = f [nz] * (Tnz - Tz + 1) % N
    if nz > 0:
        svP = sum (j - 1 for j in vP)
        snPV = [0]
        for i in range (1, n):
            snPV.append (snPV [-1] + nV [P [i - 1] - 1] * (P [i - 1] > 0))
        Tnz = sum (nZ [i] * nV [P [i] - 1] * f [n - i - 1] for i in idNZ)
        Tz  = sum ((svP + snPV [i]) * f [n - i - 1] for i in idZ)
        S += f [nz - 1] * (Tz - Tnz ) % N
    if nz > 1:
        Tz = sum (nZ [i] * f [n - i - 1] for i in idZ) * sum (nV [l - 1] for l in vP if l > 1)
        S -= f [nz - 2] * Tz % N
    return S % N

def solve_ (a, n):  # correct, but way too slow
    M = 10 ** 9 + 7 #1000000007
    l = list (permutations (range (1, n + 1)))
    r = 0
    for nr in a:
        pnr = '0' if nr == 0 else ' '
        print (pnr, end = ",")
    print ()
    for i, p in enumerate (l):
        s = set (0 if x == y or y == 0 else x for x, y in zip (p, a))
        if len (s) == 1 and 0 in s:
            for nr in p:
                print (nr, end = ",")
            print ("", end = ",")
            print (i)
            r = (r + i + 1) % M
    print ("result", r, "count of permuations", i + 1)
    return r

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    a = list (map (int, input ().rstrip ().split ()))
    result = solve (a, n)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

