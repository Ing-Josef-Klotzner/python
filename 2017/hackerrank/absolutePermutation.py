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

def absolutePermutation (n, k):
    # |pos [i] - i| = k
    # Given n and k, print the lexicographically smallest absolute permutation P
    if k != 0:
        if (n / k) % 2 != 0: return "-1"
#    ar = [0] + [1 + k] + [0] * (n - 1)
    ar = []
    add = True
    for i in range (1, n + 1):
        if add: ar.append (str (i + k))
        else: ar.append (str (i - k))
        if k != 0:
            if i % k == 0: add = not add
    res = ar [0]
    res += "".join (map (lambda x: " " + x, ar [1:]))
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        [n, k] = map (int, input ().split ())
        result = absolutePermutation (n, k)
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()


"""
1
100 2

Output:

3 4 1 2 7 8 5 6 11 12 9 10 15 16 13 14 19 20 17 18 23 24 21 22 27 28 25 26 31 32 29 30 35 36 33 34 39 40 37 38 43 44 41 42 47 48 45 46 51 52 49 50 55 56 53 54 59 60 57 58 63 64 61 62 67 68 65 66 71 72 69 70 75 76 73 74 79 80 77 78 83 84 81 82 87 88 85 86 91 92 89 90 95 96 93 94 99 100 97 98 

"""
