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
"""
"""
def commonCharacterCount(s1, s2):
    cL1 = [0] * 26; cL2 = [0] * 26
    ls1 = len (s1); ls2 = len (s2)
    for i in range (ls1):
        cL1 [ord (s1 [i]) - ord ('a')] += 1
    for i in range (ls2):
        cL2 [ord (s2 [i]) - ord ('a')] += 1
    def f (x_):
        i, x = x_
        return min (x, cL2 [i])
    res = sum (list (map (f, enumerate (cL1))))
    return res

def main ():
#    sequence = list (map (int, input ().split ()))
    s1 = "aabcc"; s2 = "adcaa"
    print (commonCharacterCount (s1, s2))

if __name__ == '__main__':
    main ()
