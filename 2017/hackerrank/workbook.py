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

def workbook (n, k, arr):
    s = 1; res = 0
    for cnt in arr:
        pgdfi = pgdf = (cnt - 1) // k        # page difference
        while pgdf > -1:
            prdf = pgdf * k + 1     # problem difference
            pg = pgdf + s
            prdful = cnt + 1 if cnt + 1 < prdf + k else prdf + k
            print (cnt, prdf, prdful, s, pg)
            if pg >= prdf and pg < prdful:
                print ("hit")
                res += 1
            pgdf -= 1
        s += pgdfi + 1
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, k] = map (int, input ().split ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = workbook (n, k, arr)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
