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
from collections import Counter

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
week
2
1 4
2 3
out:
2
1
"""
#def initialize (s):
    # This function is called once before all queries.

# factorial (x) % (10 ** 9 + 7)
def fm (x, m = 10 ** 9 + 7):
    res = 1
    for i in range (2, x + 1):
        res = res * i % m
    return res

def modInv (a, m = 10 ** 9 + 7):
    # result only valid if m is prime
#    g = gcd (a, m)
#    if (g != 1):
#        #print ("Inverse doesn't exist")
#        return 0
#    else:
#        # If m is prime, then modulo inverse is a^(m-2) mod m
#        r = power (a, m - 2, m)
#        #print ("Modular multiplicative inverse is ", r)
#        return r
    r = power (a, m - 2, m)
    return r
# To compute x^y under modulo m 
def power (x, y, m):
    if (y == 0): return 1
    p = power (x, y // 2, m) % m
    p = (p * p) % m
    if y % 2 == 0: return p
    else: return (x * p) % m
# Function to return gcd of a and b 
def gcd (a, b):
    if (a == 0):
        return b
    return gcd (b % a, a)
## Driver Program 
#a = 3; m = 11
#modInverse(a, m) 

def maximumPalindromes (s):
    m = 10 ** 9 + 7
    cnt = Counter (s)
#    print (cnt)
    dvn = 0
    dvr = 1
    nofc = 0   # number of odd frquency characters - middle of palindrome
    for k in cnt:
        v = cnt [k]
        vh = v // 2
        dvn += vh
        if vh: dvr = dvr * modInv (fm (vh)) % m
        if v % 2: nofc += 1
    nofc = max (1, nofc)
#    print (dvn, dvr, nofc)
    return fm (dvn) * dvr % m * nofc % m

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = list (input ())
#    initialize (s)
    q = int (input ())
    for _ in range (q): # q
        [l, r] = list (map (int, input ().split ()))
        s1 = s [l - 1 : r]
#        print (s1)
        result = maximumPalindromes (s1)
#        print (result)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
