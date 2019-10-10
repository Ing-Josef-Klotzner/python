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

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
"""
def weight (u):
    ln = len (u)
    if ln == 0: return 0
    return v (u [0]) * ln

def v (c):
    return ord (c) - 96

# all divisors of a number
def adoan (x):
    pass
    
def weightedUniformStrings (s, quL, qc):
#    # creating list of uniform substrings
#    ufsS = set ()
#    pu = ""   # previous unified c
#    subu = ""
#    for c in s:
#        if c not in ufsS:
#            subu = c
#            ufsS.add (subu)
#            pu = c
#        elif pu == c:
#            subu += c
#            ufsS.add (subu)
#        elif pu != c:
#            subu = c
#            pu = c
#    vL = map (weight, ufsS)
#    print (list (zip (ufsS, vL)))
#    # convert uniform substrings to weights
#    ufsW = set (map (weight, ufsS))
#    print ("weights")
#    print (ufsW)
    
    # create set of weights directly
    ufsW = set ()
    pu = ""
    subv = 0
    for c in s:
        vc = v (c)
        if vc not in ufsW:
            subv = vc
            ufsW.add (subv)
            pu = c
        elif pu == c:
            subv += vc
            ufsW.add (subv)
        elif pu != c:
            subv = vc
            pu = c
#    print ("directly generated weights")
#    print (ufsW)

    res = []
    for q in quL:
        if q in ufsW: res.append ("Yes")
        else: res.append ("No")
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = input ()
    qc = int (input ())
    quL = []
    for _ in range (qc):
        itm = int (input ())
        quL.append (itm)
    result = '\n'.join (weightedUniformStrings (s, quL, qc))
    print (result)
    fptr.write (result)
    fptr.write ("\n")
    fptr.close ()

if __name__ == '__main__':
    main ()
