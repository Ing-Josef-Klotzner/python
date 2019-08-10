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
"""
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

def get_max_ (lcp, n):
    lcp.append (0)
    length = n
    ans, st = length, []
    count = 1
    for i, l in enumerate (lcp):
        pos = i
        while st and st [-1] [1] > l:
            j, h = st.pop ()
            pos = j
            ct = (i - j + 1)
            if ct * h > ans:
                ans = ct * h
                length, count = h, ct
        if not st or st [-1] [1] < l:
            st.append((pos, l))
    return ans

def sort_bucket (str_, bucket, order):
    d = defaultdict (list)
    for i in bucket:
        key = str_ [i : i + order]
        d [key].append (i)
    result = []
    for k,v in sorted (d.items ()):
        if len (v) > 1:
            result += sort_bucket (str_, v, order * 2)
        else:
            result.append (v [0])
    return result
 
def suffix_array_ManberMyers (str_, n):
    return sort_bucket (str_, (i for i in range (n)), 1)


def suffix_array_simple (s, n):
    return [t [1] for t in sorted ((s [i :], i) for i in range (n))]

def suffix_array_simple2 (s, n):
    return sorted (range (n), key = lambda i: s [i : ])

# O (n)    !!   slower as below one - without optimization
def suffixArray_ (s, n):
    G = range;  z = L, m , h = [0] * 3;  I = z * n
    def f (s, n):
        def r (o):
            b = [[] for _ in s]; c = []
            for x in B [ : N]: b [s [x + o]] += x,
            for x in b: c.extend (x)
            B [ : N] = c
        M = N = n - - ~n // 3; t = n % 3 % 2; B = list (G (n + t))
        n02 = (n + 2) // 3 + n // 3
        del B [ : : 3]; r (2); u = []; m = p = 0; r (1); r (0); N -= n // 3
        for x in B * 1:
            v = s [x : x + 3]
            m += u < v; u = v
            B [x // 3 + x % 3 // 2 * N] = m
        A = 1 // M * z or f (B + z, M) + z
        B = [x * 3 for x in A if x < N]
        J = I [r (0) : n]; C = list (G (n))
        for k in C:
            b = A [t] // N
            a = i, j = A [t] % N * 3 - ~b, B [p]
            q = p < N and (s [i : i - ~b], J [i // 3 + b + N - b * N]) > (s [j + t // M : j -~b], J [j // 3 + b * N])
            C [k] = x = a [q]
            I [x] = k; p += q
            t += 1 - q
        return C
    S = f (list (map (ord, s)) + z * 40, n)
    return S

# O (n)    !!   fastest
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


# 3 x faster than Manber Myers
def suffix_array(line):
    isa, sa, lb = [0] * len(line), [0] * len(line), [0] * len(line)
    for i in range(len(line)): sa[i] = ord(line[i])

    size = 1
    while size <= len(line):
        for i in range(len(lb)):
            if i + size < len(line): lb[i] = ((sa[i], sa[i + size]), i)
            else: lb[i] = ((sa[i], -1), i)
        lb.sort()
        sa[lb[0][1]] = 0
        for i in range(1, len(lb)):
            cls, idx = lb[i]
            if cls == lb[i - 1][0]: sa[idx] = sa[lb[i - 1][1]]
            else: sa[idx] = sa[lb[i - 1][1]] + 1
        size *= 2

    for i, p in enumerate(sa): isa[p] = i
    return isa, sa

def lcpF(line, sa, rank):
    lcp = [0] * len(sa)
    h = 0
    for i in range(len(line)):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while line[i + h] == line[j + h]: h += 1
        lcp[rank[i]] = h
        if h > 0: h -= 1
    return lcp



def maxValue (t):
    n = len (t)
    start = time ()
    #sa = suffix_array_ManberMyers (t, n)
    #sa = suffix_array_simple2 (t, n)
    sa = suffixArray (t, n)
    #sa, rank = suffix_array (t + chr (0))
    #print (sa)
    #print (sa, rank)
    print ("suffix_array created. time: (s)", time () - start)
    start = time ()
    lcp = kasai_lcp (t, sa, n)
    #lcp = lcpF (t + chr (0), sa, rank)
    print ("lcp created. time (s)", time () - start)
    start = time ()
    res = get_max_ (lcp, n)
    print ("max lcp diff evaluated. time (s)", time () - start)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = input ()
    result = maxValue (t)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
