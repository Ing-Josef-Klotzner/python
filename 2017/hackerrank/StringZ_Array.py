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

# Python3 program that implements z algorithm
# for pattern searching
# Fills z array for given string str []
def get_z_arr (string, z):
    n = len (string)
    # [l,r] make a window which matches
    # with prefix of s
    l, r, k = 0, 0, 0
    for i in range (1, n):
        # if i > r nothing matches so we will calculate.
        # z [i] using naive way.
        if i > r:
            l, r = i, i
            # r - l == 0 starting, so we start checking from 0'th index
            # for "ababab" (i = 1), the value of r remains 0 and z [i]
            # becomes 0. For string "aaaaaa" and i = 1, z [i] and r become 5
            while r < n and string [r - l] == string [r]: r += 1
            z [i] = r - l
            r -= 1
        else:
            # k = i - l so k == [l,r] interval.
            k = i - l
            # if z [k] < remaining interval then z [i] = z [k].
            # For example, str = "ababab", i = 3, r = 5 and l = 2
            if z [k] < r - i + 1: z [i] = z [k]
            # For example str = "aaaaaa" and i = 2,    r is 5, l is 0
            else:
                # else start from r and check manually
                l = i
                while r < n and string [r - l] == string [r]:
                    r += 1
                z [i] = r - l
                r -= 1
# prints all occurrences of pattern# in text using z algo
def search (text, pattern):
    # Create concatenated string "P$T"
    concat = pattern + "$" + text
    l = len (concat)
    # Construct z array
    z = [0] * l
    get_z_arr (concat, z)
    # now looping through z array for matching condition
    for i in range (l):
        # if z [i] (matched region) is equal to pattern
        # length we got the pattern
        if z [i] == len (pattern):
            print ("Pattern found at index", i - len (pattern) - 1)

# Driver Code
def main ():
    text = "GEEKS FOr GEEKS"
    pattern = "GEEK"
    search (text, pattern) 

if __name__ == "__main__":
    main ()
