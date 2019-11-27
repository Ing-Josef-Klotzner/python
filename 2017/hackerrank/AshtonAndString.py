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
#from itertools import permutations, combinations, product
from bisect import bisect_right, bisect_left
#from math import factorial as fac
#from collections import deque   #, defaultdict
#from time import time   #sleep
from functools import reduce
#from operator import add    #mul
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

def suffixArray (s, n):
    def suffix_array (s, n, K):
        # skew algorithm
        s += [0] * 3
        n0 = (n + 2) // 3;  n1 = (n + 1) // 3;  n2 = n // 3
        n02 = n0 + n2;   adj = n0 - n1
        def radix_pass (a, o, n = n02):
            c = [0] * (K + 3)
            for x in a [ : n]: c [s [x + o] + 1] += 1
            for i in range (K + 3): c [i] += c [i - 1]
            for x in a [ : n]:
                j = s [x + o]; a [c [j]] = x; c [j] += 1
        A = [x for x in range (n + adj) if x % 3] + [0] * 3
        radix_pass (A, 2); radix_pass (A, 1); radix_pass (A, 0)
        B = [0] * n02;   t = [];   m = 0
        for x in A [ : n02]:
            u = s [x : x + 3];  m += t < u;  t = u
            B [x // 3 + x % 3 // 2 * n0] = m
        A [ : n02] = 1 // n02 * [0] or suffix_array (B, n--~n//3, m)
        I = A * 1
        for i in range (n02): I [A [i]] = i + 1
        B = [3 * x for x in A if x < n0]
        radix_pass (B, 0, n0)
        R = [];  p = 0;  t = adj
        while t < n02:
            x = A [t];  b = x >= n0
            i = (x - b * n0) * 3 - ~b;  j = B [p]
            if p == n0 or ((s [i : i + 2], I [A [t] - n0 + 1]) < (s [j : j + 2], I [j // 3 + n0]) if b else (s [i], I [A [t] + n0]) < (s [j], I [j // 3])): R += i,; t += 1
            else: R += j,; p += 1
        return R + B [p : n0]
    return suffix_array (list (map (ord, s)), n, 128)


def ashtonString (s, k):
    n = len (s)
    s_a = suffixArray (s, n)
#    print (s_a)
    # substrings can be built (but i think no need - faster: calculate distances)
#    con_subs = ""
    distinctSet = set ()
    count = 0
    for i in s_a:
        for j in range (i + 1, n + 1):
            sub = s [i : j]
            if hash (sub) not in distinctSet:
                # uncomment if build string with concatenated substrings
#                con_subs += sub + " "
                if count + len (sub) >= k:
#                    print (con_subs)
#                    print ("len distinctSet", len (distinctSet))
                    return sub [k - 1 - count]
                count += len (sub)
                distinctSet.add (hash (sub))
#        print (count, end = " ")

#    # check by comparing if correct sorted
#    l = con_subs.split ()
#    print (" ".join (sorted (l)))
    return "k too big"

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        s = input ()
        k = int (input ())
        result = ashtonString (s, k)
        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
5
nvzjkcahjwlhmdiuobjdwbanmvrtadopapbktdtezellktgywrdstdhhayaadqrdhspavjgxprk
2071
szkkcedhlkhjnjofbrnvhntsushncjavkmfn
465
wcweojncpqwcofrhxnzgbdrd
251
pfpgrnlorzzhdoxzsnemubzvkcbbfb
77
judaioobpoiteiszvzlscmpmpqqwuvtdqzdapudfimaowsnttalwndievaapwusmtyoksrpcfpqbkgvfiibvlkbjkcy
2473
out:
b
d
d
o
w
"""
