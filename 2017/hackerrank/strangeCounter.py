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

def strangeCounter (t):
    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21
    # 3 2 1 6 5 4 3 2 1 12 11 10  9  8  7  6  5  4  3  2  1
    # new range after 3, 9 (+6), 21 (+12), 45 (+24) counting backwards in each range
    # ranges: 3 * 2 ** rn (rn Rangenumber)  
    # getting rangenumber: (t (21) + 2) / 3 = 7
    # 1 2 4  8 16 32
    #  +
    # 1 3 7 15 31 63   int (log (7, 2)) = 2 (= rn)
    # 1 - 3 -> 0    4 - 9 -> 1    10 - 21 -> 2
    rn = int (log ((t + 2) / 3, 2))
    ll = 3 * 2 ** rn - 2        # lower limit
    nl = 3 * 2 ** (rn + 1) - 2  # next limit
    dl = nl - ll  # difference - size of range
#    print (ll, nl)
    return str (dl - (t - ll))
    
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    result = strangeCounter (t)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
