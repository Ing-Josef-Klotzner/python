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
def bisect_left (sa, x, text, lo = 0, hi = None):
    if lo < 0:
        raise ValueError ('lo must be non-negative')
    if hi is None: hi = len (sa)
    while lo < hi:
        mid = (lo + hi) // 2
        if text [sa [mid] : ] < x: lo = mid + 1
        else: hi = mid
    if not text [sa [lo] : ].startswith (x):
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        #raise IndexError ('not found')
        return -1
    return sa [lo]

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

def solve (a, b, sta, stb):
    # lcp - palindrome  ('abc' (from a) + x (from a) + 'cba' (from b))
    # found by lcp of a and reversed b    x ... if exists
    a_ = a [::-1]; b_ = b [::-1]; s = a + b_
    n = len (s); la = len (a);  lb = len (b)
    sa = suffixArray (s, n)
    """umg. auf kasai lcp   l_p longest common prefix (length list)"""
    l = kasai_lcp (s, sa, n)
    _l_ix_ = 0   # find max l, where found lcp is in a and b_
    mx = 0
    ctl = defaultdict (tuple)
    for i in range (n):
        if not l [i]: 
            continue
        # l  Liste der Längen gemeinsamer prefixe zwischen a und b
        # check, if found lcp is in a and b_ and not in a only or b_ only
        """ mk m_l list from lcp l of tuples (plen, pix) - keep it lexographical 
            valid entries only if length of com prefix is from a and b_ and not a only or b_ only
            keep it lexogr. by ctl dict (right border is key and content is (length / indices to lcp/SA))
            only add different prefixes to dict - how identify different ones? -> different right border
            - when combining prefixes with existing palins in a or b they could overlap !
            ... so not just search for R_prefix == L_exist_pal, search if within others L to R """
        if (sa [i] < la and sa [i + 1] >= la or
            sa [i] >= la and sa [i + 1] < la):
            if len (sa) > 1:
                isa = i; isb = isa + 1
                if sa [isb] < sa [isa]: isa, isb = isb, isa
                ct = l [i]; L = sa [isa]; R = L + ct
                Lb = lb - sa [isb] + la - ct; Rb = Lb + ct
#            ct = l [i]; L = sa [i] if sa [i] < la else sa [i + 1]; R = L + ct
            # if same right side, it is same prefix, change entry if longer
            min_pre_len = max (1, mx - 2)
            if ct > min_pre_len:
                if R in ctl:
                    ctd, _, _, _, _, _ = ctl [R]
                    if ct >= ctd:
#                        print ("enlarge", s [R - ctl [R] [0] : R], "->", R - L, i, s [L : R], end = " ")
                        ctl [R] = (ct, i, L, R, Lb, Rb)
                else:
#                    print ("uniques: ", R - L, i, s [L : R], end = "  ")
                    ctl [R] = (ct, i, L, R, Lb, Rb)
            if ct > mx:
                mx = ct
                _l_ix = i   # index of longest prefix
    # build m_l list from dict ctl
    m_l = sorted (list (ctl.values ()))

    if len (sa) > 1:
        isa = _l_ix; isb = isa + 1
        if sa [isb] < sa [isa]: isa, isb = isb, isa
        l_ct = l [_l_ix]; L = sa [isa]; R = L + l_ct
        Lb = lb - sa [isb] + la - l_ct; Rb = Lb + l_ct
    else: return "-1"
    x1 = a [R] if R < la else ""
    x1 = a [R : R + 2] if R + 1 < la and a [R] == a [R + 1] else x1
    x1 = a [R : R + 3] if R + 2 < la and a [R] == a [R + 2] else x1
    x2 = b [Lb - 1] if Lb - 1 >= 0 else ""   #and Lb - 1 < lb else ""
    x2 = b [Lb - 2 : Lb] if Lb - 2 >= 0 and b [Lb - 2] == b [Lb - 1] else x2
    x2 = b [Lb - 3 : Lb] if Lb - 3 >= 0 and b [Lb - 3] == b [Lb - 1] else x2
    x = ""
    lx1 = len (x1); lx2 = len (x2)
    if lx1 < lx2 or lx1 == lx2 and x2 < x1: x = x2
    elif lx2 < lx1 or lx1 == lx2 and x1 < x2: x = x1
    lcp_palin_l = a [L : R]; lcp_palin_r = b [Lb : Rb]
    lcp_palin = lcp_palin_l + x + lcp_palin_r if lcp_palin_l else ""

    res_pal = lcp_palin

    # trying to find part of palindrome in a + a_ and b + b_
    # these are no standalone answers, as it is not ollowed to 
    # combine with empty string from other (b or a)
    s_a = a + a_; na = la * 2; s_b = b + b_; nb = lb * 2
    saa = suffixArray (s_a, na)
    l_a = kasai_lcp (s_a, saa, na)
    sab = suffixArray (s_b, nb)
    l_b = kasai_lcp (s_b, sab, nb)

    """          puzzle palindrome 2         """
    # combine and find maximum palindrome:
    # combine m_l list with all palindromes in a and in b, check if overlap / fit, find maximum
    tim = time ()
    p2_ca_pal = ""; l_p2_ca_pal = 0
    for isaa, l_a_ct in enumerate (l_a):
        if l_a_ct < 1: continue
        isaa_ = isaa + 1
        if saa [isaa_] < saa [isaa]: isaa, isaa_ = isaa_, isaa
        if saa [isaa] > la or isaa_ < na and saa [isaa_] < la: continue
        Lax = saa [isaa]; Rax = Lax + l_a_ct
        pala = a [Lax : Rax]
        if pala != pala [::-1]: continue
        for ct, i, L, R, Lb, Rb in m_l:
            if R >= Lax and R < Rax: 
                df = R - Lax; fd = a [L : Lax]; fd_ = b [Lb + df: Rb]
                p2_ca_palin = fd + pala + fd_ if fd else ""
                l_p2_ca_palin = 2 * (Lax - L) + Rax - Lax
                if (l_p2_ca_palin > l_p2_ca_pal or 
                    l_p2_ca_palin == l_p2_ca_pal and p2_ca_palin < p2_ca_pal):
                        l_p2_ca_pal = l_p2_ca_palin
                        p2_ca_pal = p2_ca_palin
    if l_p2_ca_pal > len (res_pal): res_pal = p2_ca_pal
    elif len (p2_ca_pal) == len (res_pal) and p2_ca_pal < res_pal:
        res_pal = p2_ca_pal
    p2_cb_pal = ""; l_p2_cb_pal = 0
    for isab, l_b_ct in enumerate (l_b):
        if l_b_ct < 1: continue
        isab_ = isab + 1
        if sab [isab_] < sab [isab]: isab, isab_ = isab_, isab
        if sab [isab] > lb or isab_ < nb and sab [isab_] < lb: continue
        Lbx = sab [isab]; Rbx = Lbx + l_b_ct
        palb = b [Lbx : Rbx]
        if palb != palb [::-1]: continue
        for ct, i, L, R, Lb, Rb in m_l:
            if Rbx >= Lb and Rbx < Rb:
                df = Rbx - Lb; fd = a [L : R - df]; fd_ = b [Rbx : Rb]
                p2_cb_palin = fd + palb + fd_ if fd else ""
                l_p2_cb_palin = 2 * (Rb - Rbx) + Rbx - Lbx
                if (l_p2_cb_palin > l_p2_cb_pal or 
                    l_p2_cb_palin == l_p2_cb_pal and p2_cb_palin < p2_cb_pal):
                        l_p2_cb_pal = l_p2_cb_palin
                        p2_cb_pal = p2_cb_palin
    if l_p2_cb_pal > len (res_pal): res_pal = p2_cb_pal
    elif len (p2_cb_pal) == len (res_pal) and p2_cb_pal < res_pal:
        res_pal = p2_cb_pal

    return res_pal
    

def buildPalindrome (a, b):
    sta = set (a); stb = set (b)
    if sta.isdisjoint (stb) or a == "" and b == "": return "-1"
    res = solve (a, b, sta, stb)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        a = input ()
        b = input ()
        result = buildPalindrome (a, b)
#        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
