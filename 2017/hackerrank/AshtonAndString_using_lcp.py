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

def kasai_lcp (s, sa, n):   # sa  suffix array
    k = 0
    lcp = [0] * n; rank = [0] * n
    for i in range (n): rank [sa [i]] = i
    for i in range (n):
        k -= 1 if k else 0
        if rank [i] == n - 1: k = 0; continue
        j = sa [rank [i] + 1]
        while i + k < n and j + k < n and s [i + k] == s [j + k]: k += 1
        lcp [rank [i]] = k
    return lcp

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

def gauss_sum (x):
#    global gauss   # table not really faster !
    return (x * x + x) // 2
    #return gauss [x]

# using LCP (longest common prefix) - fastest
def ashtonString (s, k):
    n = len (s)
    s_a = suffixArray (s, n)
    l = kasai_lcp (s, s_a, n)
    count = 0
    dstnctSet = set ()
    lcp_max = 0
    for i, lcp in enumerate (l):
        lcp_max = max (lcp_max, lcp)
        dstnct_substr_len = n - s_a [i]
        lcp_str = s [s_a [i] : s_a [i] + lcp_max]
        lcp_ = 0
        for il in range (1, len (lcp_str) + 1):
            if lcp_str [ : il] in dstnctSet: lcp_ += 1
            else: break
#        print ("lcp_", lcp_, "lcp_str", lcp_str, end = " ")
        cnt_dstnct = gauss_sum (dstnct_substr_len) - gauss_sum (lcp_)
#        print (count, dstnct_substr_len, cnt_dstnct)
        if count + cnt_dstnct >= k:
            for d_sub_len in range (dstnct_substr_len -1, -1, -1):
                diff = gauss_sum (d_sub_len) - gauss_sum (lcp_)
                if count + diff < k:
                    break
#            print ("d_sub_len", d_sub_len, "diff", diff, "index", k - 1 - diff)
            return s [s_a [i] + k - 1 - count - diff] 
        #if substr of lcp_str not in dstnctSet: dstnctSet.add (lcp_str ["substring"])
        for il in range (1, len (lcp_str) + 1):
            if lcp_str [ : il] not in dstnctSet:
                dstnctSet.add (lcp_str [ : il])
        count += cnt_dstnct
#        print (count, end = " ")
#    print (n, i, s_a [i], k, count, end = " ")
    return "k too big"

def ashtonString_ (s, k):
    n = len (s)
    s_a = suffixArray (s, n)
#    print (s_a)
    # substrings can be built (but i think no need - faster: calculate distances)
    con_subs = ""
    distinctSet = set ()
    count = 0
#    fst = True
    for i in s_a:
        for j in range (i + 1, n + 1):
            sub = s [i : j]
            if hash (sub) not in distinctSet:
                # uncomment if build string with concatenated substrings
#                if fst:
#                    con_subs += sub + " "
#                    fst = False
                if count + len (sub) >= k:
#                    print (con_subs, end = "   ")
#                    print ("len distinctSet", len (distinctSet))
                    return sub [k - 1 - count]
                count += len (sub)
                distinctSet.add (hash (sub))
#        fst = True
    return "k too big"

def main ():
#    global gauss
#    gauss = [0] * 100001
#    gauss [1] = 1
#    for i in range (2, 100001):
#        gauss [i] = gauss [i - 1] + i
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        s = input ()
        k = int (input ())
#        print ("richtig", ashtonString_ (s, k))
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
