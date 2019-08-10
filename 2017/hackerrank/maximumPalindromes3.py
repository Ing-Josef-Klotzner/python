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
    if x in fmD: return fmD [x]
    res = 1
    for i in range (2, x + 1):
        res = res * i % m
    fmD [x] = res
    return res

# fills list of factorials % (10 ** 9 + 7) up to x
def fmlg (x, m = 10 ** 9 + 7):
    global fmL
    fmL = [1]
#    global rfL
#    rfL = [1]
    res = 1
    for i in range (1, x):
        fmL.append (fmL [i - 1] * i % m)
        # precompution of all reversed factorials is slower - skip
        #rfL.append (power (fmL [i - 1], m - 2, m))

def modInv (a, m = 10 ** 9 + 7):
    if a in miD: return miD [a]
    # result only valid if m is prime !
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
    miD [a] = r
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

def maximumPalindromes (l, r):
    dvn = 0
    dvr = 1
    nofc = 0
    for v in dfL (cL [l - 1], cL [r]):
        if not v: continue
        vh = v // 2
        dvn += vh
        if vh: dvr = dvr * modInv (fmL [vh]) % m  # rfL [vh] % m
        if v % 2: nofc += 1
    nofc = max (1, nofc)
    return fmL [dvn] * dvr % m * nofc % m

def dfL (l1, l2):
    ln = len (l1)
    res = []
    for i in range (ln):
        res.append (l2 [i] - l1 [i])
    return res

def initialize (s):
    # create 2D array ([s.length] [26]) with character counts
    # of each character at each specific position in s
    ln = len (s)
    ls = [0] * 26
    global cL
    cL = [ls.copy ()]
    for i in range (ln):
        c = s [i]
        ls [ord (c) - 97] += 1
        cL.append (ls.copy ())
    # precompute all factorials % m up to 100000   (precompution of
    # all inverses of factorials % m up to 100000 is slower than
    # calculate only the needed ones and use dict of calculations)
    fmlg (100000)
    print ("initialized")
    
def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    s = list (input ())
    q = int (input ())
    global m
    m = 10 ** 9 + 7
    global fmD
    fmD = dict ()
    global miD
    miD = dict ()
    initialize (s)
    for _ in range (q): # q
        [l, r] = list (map (int, input ().split ()))
        result = maximumPalindromes (l, r)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
