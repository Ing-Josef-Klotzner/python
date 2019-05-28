#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Thu Aug 17 00:52:10 2017

@author: josef
"""
import random


def firstn(g, n):
    for i in range(n):
        yield g.next()

def signal():
    while 1:
        yield random.randrange(-5, 5)

def cross_detect(a, b):
    if ((a > 0) and (b < 0)): return -1
    elif ((a < 0) and (b > 0)): return 1
    else: return 0

def zerocross(g):
    a = g.next()
    b = g.next()
    while 1:
        yield cross_detect(a, b)
        a, b = b, g.next()
		
def smooth(g):
    a = g.next()
    b = g.next()
    while 1:
        yield (a+b)/2.0
        a, b = b, g.next()
  
if __name__ == '__main__':
    print(list(firstn(zerocross(signal()),16)))
    print(list(firstn(zerocross(smooth(signal())),16)))