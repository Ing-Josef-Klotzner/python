#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
from sys import argv
"""
Created on Wed Aug 16 15:55:12 2017

@author: josef
"""
from collections import deque

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
 
primes = list()
primes_to_half = list()   # liste der primzahlen bis n//2+1
# -> wenn bis halb n nicht teilbar, dann auch nicht durch restliche Primzahlen
prime_tops = deque()   # Liste der hohen Primzahlen zum Füllen von primes_to_half
end = int(argv[1])

for n in firsts(2, end+1):
    for x in primes_to_half:
        if n % x == 0:
            if not sil: print( n, 'equals', x, '*', n//x, end=" ")
            if n//x in primes and not sil:
                print("(prime)")
            elif not sil:
                print()
            break
    else:
        # loop fell through without finding a factor
        primes.append(n)
        prime_tops.append(n)
        if prime_tops[0] <= n//2+1:
            primes_to_half.append(prime_tops.popleft())
        if not sil: print("primes to half of number to check for prime: ", primes_to_half)
        if not sil: print(n, 'is a prime number')

cnt=len(primes)        
print(cnt, " Primzahlen bis ", end)
print(primes)