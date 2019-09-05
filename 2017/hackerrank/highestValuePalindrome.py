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

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
6 2
932239
out:
992299

5 1
12321
out:
12921
"""
def highestValuePalindrome (s, n, k):
    if n == 1 and k == 0: return s
    elif n == 1 and k > 0: return ("9")
    n2 = n // 2
    diff = 0
    mustL = []
    for i in range (n2):
        if s [i] != s [n - 1 - i]:
            mustL.append (1)
            diff += 1
        else: mustL.append (0)
    print ("diff", diff, "k", k)
    print (mustL)
    if diff > k: return "-1"
    for i in range (n2):
        si = s [i]
        sni = s [n - 1 - i]
        mi = mustL [i]
        if mi:
            if si == '9' or sni == '9':
                if si > sni: s [n - 1 - i] = '9'
                else: s [i] = '9'
            elif k > diff:
                k -= 1
                s [i] = '9'
                s [n - 1 - i] = '9'
            else:
                if si > sni: s [n - 1 - i] = s [i]
                else: s [i] = s [n - 1 - i]
            diff -= 1; k -= 1
        elif k - 2 >= diff and si != '9' and sni != '9':
            s [i] = '9'
            s [n - 1 - i] = '9'
            k -= 2
    if n % 2 and k >= 1: s [n // 2] = '9'
    print ("diff", diff, "k", k)
    return "".join (s)
    
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, k] = list (map (int, input ().split ()))
    s = list (input ())
    result = highestValuePalindrome (s, n, k)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
