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

def flatlandSpaceStations (m, n, ca):
    ca.sort ()
    # find maximum distance between 2 cities
    mx = 0
    for i in range (m - 1):
        mx = max (mx, (ca [i + 1] - ca [i]) // 2)
#        print (i, mx)
    # not to forget: the outer cities
    mx = max (mx, ca[0], n - 1 - ca [-1])
    return mx

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    [n, m] = map (int, input ().split ())
    c = list (map (int, input ().rstrip ().split ()))
    result = flatlandSpaceStations (m, n, c)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
