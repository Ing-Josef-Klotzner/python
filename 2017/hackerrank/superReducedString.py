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

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
expected out:
tqauhujtmxnsbzpykwlvpfyqijvdhuhirdmuxiobyvxupqwydkpbxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh
"""
def index (c):
    return ord (c) - ord ('a')

def superReducedString_ (s):
    ln = len (s)
    emp = "Empty String"
    if ln < 2: return emp
    i = 0
    while i < ln - 1:
        print (i, s)
        c = s [i]
        cn = s [i + 1]
        if c == cn:
            s = s [ : i] + s [i + 2 : ]
            ln -= 2
            if i > 0: i -= 1
        else:
            i += 1
    return s if s else emp

def superReducedString__ (s1):
    # faster variant using deque
    s = deque (s1)
    ln = len (s)
    emp = "Empty String"
    if ln < 2: return emp
    res = deque ()
    while ln > 0:
#        print (ln, res, s)
        c = s [0]
        cn = s [1] if ln > 1 else '&'
        if c == cn:
            for i in range (2):
                ln -= 1
                if s: s.popleft ()
        elif res and res [-1] == c:
            res.pop ()
            s.popleft ()
            ln -= 1
        else:
            s.popleft ()
            res.append (c)
            ln -= 1
    r = "".join (res)
    return r if r else emp

def superReducedString (s):
    # even faster variant using list as stack
    ln = len (s)
    emp = "Empty String"
    if ln < 2: return emp
    res = []
    for i in range (ln):
#        print (res, i, s [i], end = ", ")
        if not res or s [i] != res [-1]:
            res.append (s [i])
        else: res.pop ()
    r = "".join (res)
    return r if r else emp

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    result = superReducedString (s)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
