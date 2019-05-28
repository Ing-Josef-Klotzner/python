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
from math import log
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def kaprekarNumbers (p, q):
    no_result = "INVALID RANGE"
    res = []
    fres = []
    if p == 1:
        res.append (1)
        if q > 9:
            p = 9
        else: print ("1")
    for z in range (p, q + 1):
        # rounding error for log (1000, 10) ... 2.9999999999999996
        part = int (log (z, 10) + .000000000000001) + 1
        squ_z = z * z
        lp = squ_z // 10 ** part
        rp = squ_z % 10 ** part
        if lp + rp == z:
            res.append (z)
#            print (z, squ_z, lp, rp)
    if res != []:
        fres.append (str (res [0]))
        for el in res [1:]:
            fres.append (" ")
            fres.append (str (el))
        print ("".join (fres))
    else: print (no_result)    

def main ():
    p = int (input ())
    q = int (input ())
    result = kaprekarNumbers (p, q)

if __name__ == '__main__':
    main ()
