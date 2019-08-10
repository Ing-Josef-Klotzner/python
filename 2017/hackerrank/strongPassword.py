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
#from collections import deque

#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
    Its length is at least 6
    It contains at least one digit.
    It contains at least one lowercase English character.
    It contains at least one uppercase English character.
    It contains at least one special character. 
    The special characters are: !@#$%^&*()-+
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"""

def minimumNumber (n, password):
    special_characters = "!@#$%^&*()-+"
    num_mis = 1
    lc_mis = 1
    uc_mis = 1
    sc_mis = 1
    for i in range (n):
        c = password [i]
        if lc_mis and c >= 'a' and c <= 'z':
            lc_mis = 0
            continue
        if uc_mis and c >= 'A' and c <= 'Z':
            uc_mis = 0
            continue
        if num_mis and c >= '0' and c <= '9':
            num_mis = 0
            continue
        if sc_mis and c in special_characters:
            sc_mis = 0
        if not lc_mis and not uc_mis and not num_mis and not sc_mis:
            break
    mis = lc_mis + uc_mis + num_mis + sc_mis
    return max (mis, 6 - n)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    password = input ()
    result = minimumNumber (n, password)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
