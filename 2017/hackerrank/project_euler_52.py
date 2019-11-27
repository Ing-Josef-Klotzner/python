#!/usr/bin/python3
# -*- coding: utf-8 -*-

#from math import factorial as fac
#from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit (1030)

factorials = {}

def fac (n):
    """ factorial from lookup table ready or generate it to there """
    def fc (n_):
        if n_ == 0: return 1
        else: return n_ * fc (n_ - 1)
    if n not in factorials:
        #factorials [n] = 1 if  n == 0 else n * fac_ (n - 1)
        factorials [n] = fc (n)
    return factorials [n]

def ncr (n, r):
    return fac (n) // (fac (r) * fac (n - r))

def main ():
    i = 0
    for x in range (1, 1001):
        for y in range (0, x):
            if ncr (x, y) > 1000000: i += 1
    print (i)

if __name__ == '__main__':
    main ()

