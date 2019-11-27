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
from itertools import combinations

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
2
abba
abcd
out:
4
0

2
ifailuhkqq
kkkk
out:
3
10

1
cdcd
out:
5
"""
def nCr(n, r):  # r out of n combinations
    if (n, r) in nCrD: return nCrD [(n, r)]
    res = fact (n) // (fact (r) * fact (n - r))
    nCrD [(n, r)] = res
    return res

# Returns factorial of n 
def fact (n): 
    if n in fD: return fD [n]
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    fD [n] = res
    return res

def sherlockAndAnagrams_ (s):
    ln = len (s)
    count = []
    for i in range (1, ln + 1):
        a = ["".join (sorted (s [j : j + i])) for j in range (ln - i + 1)]
        c = Counter (a)
#        print (c.values ())
#        cmb = [len (list (combinations (['a'] * c [k], 2))) for k in c]
        # faster - using nCr
        #cmb = [nCr (c [k], 2) for k in c]
        # fastest: in special case of n choose 2: n (n - 1) / 2 
        cmb = [c [k] * (c [k] - 1) // 2 for k in c]
#        print (cmb)
        count.append (sum (cmb))
    return sum (count)

# faster, but more effort (precomputing)
def sherlockAndAnagrams (string):
    # returns difference count list   p2 - p1 (diff of each element)
    def dfcL (p1, p2):
        res = []
        for i in range (26):
            diff = ccs [p2] [i] - ccs [p1] [i]
            res.append (diff)
        return res
    lenS = len (string)
    # create table of char counts along string
    ct = [0] * 26
    ccs = [ct.copy ()]
    for i in range (lenS):
        ci = ord (string [i]) - ord ('a')
        ct [ci] += 1
        ccs.append (ct.copy ())
#    print ("table created")
    count = []
    for ln in range (1, lenS + 1):
        a = [tuple (dfcL (j, j + ln)) for j in range (lenS - ln + 1)]
        c = Counter (a)
        cmb = [v * (v - 1) // 2 for v in c.values ()]
        count.append (sum (cmb))
    return sum (count)

# short and middle fast
def sherlockAndAnagrams2 (string):
    buckets = {}
    for i in range (len (string)):
        for j in range (1, len (string) - i + 1):
            key = frozenset (Counter (string [i : i + j]).items ()) # O(N) time key extract
            buckets [key] = buckets.get (key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets [key] * (buckets [key] - 1) // 2
    return count

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    q = int (input ())
    global nCrD
    nCrD = dict ()
    global fD
    fD = dict ()
    for _ in range (q): # q
        s = input ()
        result = sherlockAndAnagrams (s)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
