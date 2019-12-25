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

def stringsRearrangement (inputArray):
    from copy import copy
    def adj (a, b):   # True if string a and b differ exactly in one character
        diff = 0
        for i in range (len (a)):
            if a [i] != b [i]: diff += 1
            if diff > 1: return False
        if diff != 1: return False
        else: return True
    iD = dict (zip (range (100), inputArray))
    print (iD)
    def solve (iDn, v):
        if len (iDn) < 1: return True  #Base case
        for ky, test in iDn.items ():
            if adj (v, test):
                iDn_ = copy (iDn)
                del iDn_ [ky]
                #print ("test OK", v, test, ky, iDn_)
                if solve (iDn_, test): return True
        return False
    for k, v in iD.items ():
        iDn = copy (iD)
        del iDn [k]
        sol = solve (iDn, v)
        if sol: return True
    return sol

def main ():
    a = ["aba", "bbb", "bab"]   # False
    #a = ["ab", "bb", "aa"]   #True
    #a = ["abc", "abx", "axx", "abx", "abc"]  # True
    #a = ["ff", "gf", "af", "ar", "hf"]   # True
    #a = ['q', 'q']   # False
    #a = ["ab", "ad", "ef", "eg"]   # False
    #a = ["zzzabzczaba", "zzzabzczaaa", "zzzabzczabb", "zzzabzczbbb"]   # True
    #a = ["abacabaabczzzzz", "abacababefzzzzz", "abacababcczzzzz", "abacababeczzzzz", "abacababbczzzzz", "abacababdczzzzz"]   # True
    #a = ["abc", "abx", "axx", "abc"]  # False
    #a = ["ah", "ar", "fh", "gg", "gh"]   # True
    #a = ["abbabbba", "abbabbca", "abbasbba", "abbsbbba", "acbabbba"]   # False
    a = ["abc","xbc","xxc","xbc","aby","ayy","aby"]   # True
    print (stringsRearrangement (a))

if __name__ == '__main__':
    main ()
