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
    for i in range (n):
        if not l [i]: 
            continue
        # l  Liste der Längen gemeinsamer prefixe zwischen a und b
        # check, if found lcp is in a and b_ and not in a or b_ only
        if (sa [i] < la and sa [i + 1] >= la or
            sa [i] >= la and sa [i + 1] < la):
            if l [i] > mx:
                mx = l [i]
                _l_ix_ = i
    if len (sa) > 1:
        l_ix = _l_ix_
        isa = l_ix; isb = l_ix + 1
        if sa [isb] < sa [isa]: isa, isb = isb, isa
        l_ct = l [l_ix]; L = sa [isa]; R = L + l_ct
        Lb = lb - sa [isb] + la - l_ct; Rb = Lb + l_ct
    else: return -1
    x1 = a [R] if R < la else ""
    x2 = b [Lb - 1] if Lb - 1 >= 0 and Lb - 1 < lb else ""
    if x1 == "": x = x2
    elif x2 == "": x = x1
    elif x1 < x2: x = x1
    else: x = x2
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
    """ code used for super palindrome and puzzle palindrome """
    # find a_palin which "La" == R
    La = Ra = 0
    for ix, La in enumerate (saa):
        if ix > 0 and La == R:
            ix_ = ix if l_a [ix] > l_a [ix - 1] else ix - 1
            Ra = La + l_a [ix_]
            if Ra == La: continue
            break
    p_a = a [La : Ra]
    p_a_palin = p_a if p_a == p_a [::-1] else ""
    # find b_palin which "Rbp" == Lb
    Lbp = Rbp = 0
    twice = False
    for ix, Lbp in enumerate (sab):
        if ix > 0 and Lbp + l_b [ix - 1] == Lb:
            Rbp = Lbp + l_b [ix - 1]
            if Rbp == Lbp: continue
            if twice == False:
                twice = True
                continue
            break
    p_b = b [Lbp : Rbp]
    p_b_palin = p_b if p_b == p_b [::-1] else ""
    """ super palindrome, if exists
this is a palindrome consistent of 
part of palindrome + found pal in a or b + part of palindrome_
    """
    s_pal = lcp_palin_l + p_a_palin + lcp_palin_r if La == R else ""
    if len (s_pal) > len (res_pal): res_pal = s_pal
    elif len (s_pal) == len (res_pal) and s_pal < res_pal:
        res_pal = s_pal
    s_pal_ = lcp_palin_l + p_b_palin + lcp_palin_r if Rbp == Lb else ""
    if len (s_pal_) > len (res_pal): res_pal = s_pal_
    elif len (s_pal_) == len (res_pal) and s_pal_ < res_pal:
        res_pal = s_pal_
    
    """          puzzle palindrome          """
    # find in a, combine with b and vice versa
    # for all longest common prefixes > 1 of l_a,
    # which are palindromes (pal): cut text from a until begin
    # of each palindrome; get sap, lcpp lists of cutted text + b_ 
    # -> plcp (puzzle lcp)
    # build   plcp + pal + plcp_ (reverse) and take longest
    # with b cut text from end of pal to end of b
    p_ca_pal = ""
    for l_a_ix, l_a_ct in enumerate (l_a):
        if l_a_ct < 1: continue
        isaa = l_a_ix; isaa_ = l_a_ix + 1
        if saa [isaa_] < saa [isaa]: isaa, isaa_ = isaa_, isaa
        Lax = saa [isaa]; Rax = Lax + l_a_ct
        pala = a [Lax : Rax]
        if pala != pala [::-1]: continue
        # pala now are only palindromes for further processing
        cuta_ = a [ : Lax] [::-1]; s_ca = cuta_ + '$' + b + '|'
        nca = len (s_ca)
        saca = suffixArray (s_ca, nca)
        l_ca = kasai_lcp (s_ca, saca, nca)
        l_ca_ix = l_ca.index (max (l_ca)); lca_ct = l_ca [l_ca_ix]
        isaca = l_ca_ix; isaca_ = l_ca_ix + 1
        if saca [isaca_] < saca [isaca]: isaca, isaca_ = isaca_, isaca
        Lca = saca [isaca]; Rca = Lca + lca_ct
        # finde den prefix dessen Eintrag in saca 0 ist 
        aix = saca.index (0)
        # wenn l_ca [aix - 1] > l_ca [aix], dann nimm aix - 1, weil nächster anderer prefix ist
        if aix and l_ca [aix - 1] > l_ca [aix]: aix -= 1
        # wenn beide prefixe in cuta_ oder beide in b liegen -> ungültig, continue
        lca = len (cuta_)
        if (saca [aix] < lca and saca [aix + 1] < lca or 
            saca [aix] >= lca and saca [aix + 1] >= lca): continue
#        if palb == "sys": print (sacb, sacb [aix], l_cb [aix])
        found_ = s_ca [saca [aix] : saca [aix] + l_ca [aix]]
        found = found_ [::-1]
        p_ca_palin = found + pala + found_ if found else ""
        if len (p_ca_palin) > len (p_ca_pal):
            p_ca_pal = p_ca_palin
        elif len (p_ca_palin) == len (p_ca_pal):
            p_ca_pal = p_ca_palin if p_ca_palin < p_ca_pal else p_ca_pal
    if len (p_ca_pal) > len (res_pal): res_pal = p_ca_pal
    elif len (p_ca_pal) == len (res_pal) and p_ca_pal < res_pal:
        res_pal = p_ca_pal
        
    p_cb_pal = ""
    for l_b_ix, l_b_ct in enumerate (l_b):
        if l_b_ct < 1: continue
        isab = l_b_ix; isab_ = l_b_ix + 1
        if sab [isab_] < sab [isab]: isab, isab_ = isab_, isab
        Lbx = sab [isab]; Rbx = Lbx + l_b_ct
        palb = b [Lbx : Rbx]
        if palb != palb [::-1]: continue
        # palb now are only palindromes for further processing
        cutb = b [Rbx : ]; s_cb = cutb + '$' + a_ + '|'
        ncb = len (s_cb)
        sacb = suffixArray (s_cb, ncb)
        l_cb = kasai_lcp (s_cb, sacb, ncb)
        l_cb_ix = l_cb.index (max (l_cb)); lcb_ct = l_cb [l_cb_ix]
        isacb = l_cb_ix; isacb_ = l_cb_ix + 1
        if sacb [isacb_] < sacb [isacb]: isacb, isacb_ = isacb_, isacb
        Lcb = sacb [isacb]; Rcb = Lcb + lcb_ct
        # finde den prefix dessen Eintrag in sacb 0 ist 
        bix = sacb.index (0)
        # wenn l_cb [bix - 1] > l_cb [bix], dann nimm bix - 1, weil nächster anderer prefix ist
        if bix and l_cb [bix - 1] > l_cb [bix]: bix -= 1
        # wenn beide prefixe in cuta_ oder beide in b liegen -> ungültig, continue
        lcb = len (cutb)
        if (sacb [bix] < lcb and sacb [bix + 1] < lcb or 
            sacb [bix] >= lcb and sacb [bix + 1] >= lcb): continue
        found_ = s_cb [sacb [bix] : sacb [bix] + l_cb [bix]]
        found = found_ [::-1]
        p_cb_palin = found + palb + found_ if found else ""
        if len (p_cb_palin) > len (p_cb_pal):
            p_cb_pal = p_cb_palin
        elif len (p_cb_palin) == len (p_cb_pal):
            p_cb_pal = p_cb_palin if p_cb_palin < p_cb_pal else p_cb_pal
    if len (p_cb_pal) > len (res_pal): res_pal = p_cb_pal
    elif len (p_cb_pal) == len (res_pal) and p_cb_pal < res_pal:
        res_pal = p_cb_pal
    
    return res_pal
    

def buildPalindrome (a, b):
    sta = set (a); stb = set (b)
    if sta.isdisjoint (stb) or a == "" and b == "": return -1
    res = solve (a, b, sta, stb)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        a = input ()
        b = input ()
        result = buildPalindrome (a, b)
        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
