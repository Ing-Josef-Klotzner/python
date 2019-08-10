#!/usr/bin/python2
from random import *

def brute (a, b):
    L = R = m = 0
    for i in range (len (a)):
        for j in range (i + m + 1, len (a) + 1):
            if a [i: j] in b:
                m = j - i
                L, R = i, j
    return L + 1, R

def suffix_array_slow (s):
    S = []
    for i in range (len (s)):
        S += [(s [i:], i)]
    S.sort ()
    return [x [1] for x in S]

def slow1 (a, b):
    # slow suffix array, slow lcp
    s = a + '!' + b
    S = suffix_array_slow (s)
    L = R = m = 0
    for i in range (1, len (S)):
        x = S [i - 1]
        y = S [i]
        p = s [x:] + '#'
        q = s [y:] + '$'
        h = 0
        while p [h] == q [h]:
            h += 1
        if h > m and len (a) == sorted ([x,y, len (a)]) [1]:
            m = h
            L = min (x, y)
            R = L + h
    return L + 1, R

def verify (a, b, L, R):
    if L < 1 or R > len (a) or a [L - 1: R] not in b:
        return 0
    LL, RR = brute (a, b)
    return R - L == RR - LL

def rand_string ():
    if randint (0, 1):
        n = randint (0, 8)
    else:
        n = randint (0, 24)
    a = 'zyxwvutsrq' [: randint (1,10)]
    s = ''
    for _ in range (n):
        s += choice (a)
    return s

def stress_test (f):
    numtrials = 2000
    for trial in range (numtrials):
        a = rand_string ()
        b = rand_string ()
        L, R = f (a, b)
        if not verify (a, b, L, R):
            LL, RR = brute (a, b)
            print 'failed on', (a, b)
            print 'expected:', LL, RR
            print 'actual:', L, R
            return
    print 'ok'

def slow2 (a, b):
    # slow suffix array, linear lcp
    s = a + '!' + b + '#'
    S = suffix_array_slow (s)
    I = S * 1
    for i in range (len (S)):
        I [S [i]] = i
    L = R = m = h = 0
    for i in range (len (S)):
        if I [i]:
            j = S [I [i] - 1]
            while s [i + h] == s [j + h]:
                h += 1
            if h > m and len (a) == sorted ([i, j, len (a)]) [1]:
                m = h
                L = min (i, j)
                R = L + h
            h -= h > 0
    return L + 1, R

def suffix_array (s, K):
    # skew algorithm
    n = len (s);  s += [0] * 3
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
    B = [0] * n02;   t = m = 0
    for x in A [ : n02]:
        u = s [x : x + 3];  m += t < u;  t = u
        B [x // 3 + x % 3 // 2 * n0] = m
    A [ : n02] = 1 // n02 * [0] or suffix_array (B, m)
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

def solve (a, b):
    # linear
    s = a + '!' + b + '#'
    S = suffix_array (map (ord, s), 128)
    I = S * 1
    for i in range (len (S)): I [S [i]] = i
    L = R = m = h = 0
    for i in range (len (S)):
        if I [i]:
            j = S [I [i] - 1]
            while s [i+h] == s [j + h]: h += 1
            if h > m and len (a) == sorted ([i, j, len (a)]) [1]:
                m = h
                L = min(i,j)
                R = L + h
            h -= h > 0
    return L + 1, R
stress_test(solve)
