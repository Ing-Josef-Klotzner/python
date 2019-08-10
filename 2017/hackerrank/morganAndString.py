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
from collections import deque
from io import StringIO
from collections import defaultdict
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
2
JACK
DANIEL
ABACABA
ABACABA
out:
DAJACKNIEL
AABABACABACABA

1
MZBMWEYYDIADTLCOUEGMDBYFWURPWBPUVHIFNUAPWYNDMHTQVKGKBHTYTSZ
FGAKWMOAWLZQJYPMHLLBBUUHBPRIQSNIBYWLGJLXOWYZAGRFNQAFVCQWKTK
out:
FGAKMWMOAWLZBMWEYYDIADTLCOUEGMDBYFWURPWBPUVHIFNUAPWYNDMHTQVKGKBHTYTSZQJYPMHLLBBUUHBPRIQSNIBYWLGJLXOWYZAGRFNQAFVCQWKTKZ
"""
def morganAndString__ (a, b):
    debug = False; prnt = False
    la = lna = len (a); lb = lnb = len (b)
    a = deque (a); b = deque (b)
    a += 'Ö'; b += 'Ö'
    res = ""
    resc = 0
    popa = True; popb = True; cach = cache = False
    print ("next")
    ca = ""; cb = ""
    for _ in range (lna + lnb):
#    while la or lb:
        if popa:
            if la:
                cas = a.popleft ()
#                cas = a [0]
#                a = a [1 : ]
                if not cache: ca = cas
                la -= 1
            else: cas = ca = 'Ö'
            popa = False
        if popb:
            if lb:
                cbs = b.popleft ()
#                cbs = b [0]
#                b = b [1 : ]
                if not cache: cb = cbs
                lb -= 1
            else: cbs = cb = 'Ö'
            popb = False
        ixa = 0; ixb = 0 
        pos_ = 6062
        if debug:
            prnt = resc > pos_ - 5 and resc < pos_ + 5
        if prnt:
            print (lna, la, lnb, lb)
        while ixa < la + 1 and ixb < lb + 1 and ca == cb and not cache:
            if prnt:
                print ("cache add", end = ", ")
            ca += a [ixa]
            cb += b [ixb]
            ixa += 1; ixb += 1
            cach = True
        if cach:
            cache = True
            if prnt:
                print ()
            cach = False
        if ca < cb:
            if prnt:
                print (ca, "ca < cb", cb, cas, cbs)
            if debug: resc += 1
            res += cas
            if not lb:
                a.pop ()   # append rest of string if other has ended
                res += "".join (a)
                if cache: res += "".join (deque (cbs))
                break
            popa = True
            if len (ca) > 1: ca = ca [1 : ]
            else:
                cb = cbs
                cache = False
        else:
            if prnt:
                print (cb, "cb <= ca", ca, cbs, cas)
            if debug: resc += 1
            res += cbs
            if not la:
                b.pop ()   # append rest of string if other has ended
                res += "".join (b)
                if cache: res += "".join (deque (cas))
                break
            popb = True
            if len (cb) > 1: cb = cb [1 : ]
            else:
                ca = cas
                cache = False
    return res

# mmattrw solution - shorter and faster  :() !
def morganAndString_ (a, b):
    a += '['
    b += '['
    output = StringIO () #[] #deque()
    for _ in range (len (a) + len (b) - 2):
        if a < b:
            if b == '[':
                a = a [ : -1]
                output.write (a)
                break   # append rest of string if other has ended
            output.write (a [0])
            a = a [1 : ]
        else:
            if a == '[':
                b = b [ : -1]
                output.write (b)
                break   # append rest of string if other has ended
            output.write (b [0])
            b = b [1 : ]
    return output.getvalue ()

# fastest version without string manipulation for search and compare
def pick_smaller ():
    global idx1; global idx2; global i1; global i2
    global len1; global len2; global s1; global s2   
    if len1 <= idx1: idx2_ = idx2; idx2 = len2; return s2 [idx2_ : ]
    if len2 <= idx2: idx1_ = idx1; idx1 = len1; return s1 [idx1_ : ]
    if s1 [idx1] > s2 [idx2]: idx2 += 1; return s2 [idx2 - 1]
    elif s1 [idx1] < s2 [idx2]: idx1 +=1; return s1 [idx1 - 1]
    else:
        if i1 < idx1 or i2 < idx2: i1 = idx1; i2 = idx2
        while i1 < len1 and i2 < len2 and s1 [i1] == s2 [i2]:
            i1 += 1; i2 += 1
        if (i1 < len1 and i2 < len2) and s1 [i1] != s2 [i2]: # found a tie breaker
            if s1 [i1] > s2 [i2]: idx2 += 1; return s2 [idx2 - 1]
            else: idx1 +=1; return s1 [idx1 - 1]
        elif i1 < len1 and i2 >= len2: # ran out of s2, it was all equal until
            idx1 += 1; return s1 [idx1 - 1]
        elif i1 >= len1 and i2 < len2: # ran out of s1, it was all equal until
            idx2 += 1; return s2 [idx2 - 1]
        else: #everything is the same on both sides
            i1 = 0; i2 = 0; idx1 += 1; return s1 [idx1 - 1]
#            if len1 - idx1 > len2 - idx2: idx1 += 1; return s1 [idx1 - 1]
#            else: idx2 += 1; return s2 [idx2 - 1]

# fastest version withoug string manipulation for search and compare
def morganAndString (word1, word2):
    global idx1; global idx2; global i1; global i2
    global len1; global len2; global s1; global s2   
    word = StringIO ()
    s1 = word1; s2 = word2
    len1 = len (s1); len2 = len (s2)
    idx1 = 0; idx2 = 0; i1 = 0; i2 = 0
    while len1 - idx1 > 0 or len2 - idx2 > 0:
        word.write (pick_smaller ())
    return word.getvalue ()

def sort_bucket (str, bucket, order):
    d = defaultdict (list)
    for i in bucket:
        key = str [i : i + order]
        d [key].append (i)
    result = []
    for k,v in sorted (d.items ()):
        if len (v) > 1:
            result += sort_bucket (str, v, order * 2)
        else:
            result.append (v [0])
    return result
 
def suffix_array_ManberMyers (str):
    return sort_bucket (str, (i for i in range (len (str))), 1)

# method suffix_array from editorial slowest (40 x slower !)
def suffix_array (s):
    n = len (s)
    ALPH = 34   # (A - Z, a, b)
    p = [0] * n; c = [0] * n; cnt = [0] * (n + ALPH)
    pn = [0] * n; cn = [0] * n
    for i in range (n): cnt [ord (s [i]) - 65] += 1
    for i in range (1, ALPH): cnt [i] += cnt [i - 1]
    for i in range (n): cnt [ord (s [i]) - 65] -= 1; p [cnt [ord (s [i]) - 65]] = i
    count = 1
    for i in range (1, n):
        if s [p [i]] != s [p [i - 1]]: count += 1
        c [p [i]] = count - 1
    for h in (2 ** i for i in range (20)):
        if h >= n: break
        for i in range (n):
            pn [i] = p [i] - h
            if pn [i] < 0: pn [i] += n
        cnt = [0] * n
        for i in range (n): cnt [c [i]] += 1
        for i in range (1, count): cnt [i] += cnt [i - 1]
        for i in range (n - 1, -1, -1):
            cnt [c [pn [i]]] -= 1
            p [cnt [c [pn [i]]]] = pn [i]
        count = 1
        for i in range (1, n):
            pos1 = (p [i] + h) % n
            pos2 = (p [i - 1] + h) % n
            if c [p [i]] != c [p [i - 1]] or c [pos1] != c [pos2]: count += 1
            cn [p [i]] = count - 1
        c = cn.copy ()
    return c

def morganAndString4 (a, b):
    a += 'a'; b += 'b'
    lae = len (a)
    la = lae - 1; lb = len (b) - 1
    s = a + b
    sfxAr = suffix_array (s)
#    print ("".join(map (lambda x: s [x], sfxAr)))
    print ("SuffixArray finished")
    res = ""
    pos1 = 0; pos2 = 0
    while True:
        if pos1 >= la and pos2 >= lb: break
        if pos1 >= la: res += b [pos2 : -1]; break
        if pos2 >= lb: res += a [pos1 : -1]; break
        if sfxAr [pos1] < sfxAr [lae + pos2]: res += a [pos1]; pos1 += 1
        else: res += b [pos2]; pos2 += 1
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        a = input ()
        b = input ()
        result = morganAndString (a, b)
#        print (result)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
