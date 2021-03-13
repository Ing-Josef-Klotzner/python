#!/bin/python3

import os
import sys

def __substr (string):
    j = 1
    a = set ()
    while True:
        for i in range (len (string) - j + 1):
            a.add (string [i: i + j])
        if j == len (string): break
        j += 1
    return a

def __distinct (p):
    ch = set (p)
    return len (ch)

def __f (p, M):
    return len (p) ** __distinct (p) % M

def __ans(foo):
    ret = __substr(foo)
    val = 0
    M = 10 ** 9 + 7
    for data in ret:
        val = (val + __f (data, M)) % M
    return val

def superFunctionalStrings(s):
    return __ans (s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = superFunctionalStrings(s)

        fptr.write(str(result) + '\n')

    fptr.close()
