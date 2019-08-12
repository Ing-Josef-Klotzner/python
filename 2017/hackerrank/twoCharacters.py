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
from itertools import combinations
#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
tc1 ... 268
"""

def alternate (s, l):
    st = set (s)
    cmb = list (combinations (st, 2))
#    print (cmb)
    #[[x for x in "abracadabra" if x == y or x == z] for y, z in [('a', 'b'), ('c', 'r')]]
    def alt (cs):
        ln = len (cs)
        if ln < 2: return False
        a = cs [0]; b = cs [1]
        for x in range (2, ln):
            if x % 2:
                if cs [x] != b: return False
            else:
                if cs [x] != a: return False
        return True
    tst = [[x for x in s if x == y or x == z] for y, z in cmb]
#    print (tst)
    als = [x for x in tst if alt (x)]
#    print (als)
    return len (max (als, key = len)) if als else 0
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    l = int (input ().strip ())
    s = input ()
    result = alternate (s, l)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
