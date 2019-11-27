#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Wed Aug 16 23:06:48 2017

@author: josef
"""

def sqr(x):
    return x*x

def firstn(g, n):
    for i in range(n):
        yield g.next()

def pi_series():
    sum = 0
    i = 1.0; j = 1
    while(1):
        sum = sum + j/i
        yield 4*sum
        i = i + 2; j = j * -1

def euler_accelerator(g):
    s0 = g.next() # Sn-1
    s1 = g.next() # Sn
    s2 = g.next() # Sn+1
    while 1:
        yield s2 - (sqr(s2 - s1))/(s0 - 2*s1 + s2)
        s0, s1, s2 = s1, s2, g.next()

if __name__ == '__main__':
    print(list(firstn(euler_accelerator(pi_series()), 8)))