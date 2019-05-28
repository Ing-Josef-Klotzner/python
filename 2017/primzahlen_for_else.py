#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from sys import argv
"""
Created on Wed Aug 16 15:55:12 2017

@author: josef
"""
def firsts(b, e):   # viel schneller als range, weil range immer ganze liste baut, auch wenn nicht gebraucht
    while b < e:
        yield b
        b += 1

if len(argv) == 1:
	print ("usage: "+argv[0]+" 'end number' [any word for 'silent']")
	print ("Es wird per default bis Endnummer 8 berechnet")
	argv.append(8)

if len(argv) == 3:
    sil = True
else:
    sil = None
 
prime = list()
end = int(argv[1])

for n in firsts(2, end+1):
    y = n//2+1   # wenn es bis halbe Zahl durch nichts teilbar, dann sicher nicht mehr -> etwa 2 mal schneller
#    y = n
    for x in firsts(2,y):
        if n % x == 0:
            if not sil: print( n, 'equals', x, '*', n//x, end=" ")
            if n//x in prime and not sil:
                print("(prime)")
            elif not sil:
                print()
            break
    else:
        # loop fell through without finding a factor
        prime.append(n)
        if not sil: print(n, 'is a prime number')

cnt=len(prime)        
print(cnt, " Primzahlen bis ", end)
print(prime)