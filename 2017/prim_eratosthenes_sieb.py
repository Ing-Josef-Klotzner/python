#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Thu Aug 17 01:49:22 2017

@author: josef
"""
from sys import argv

if len(argv) == 1:
	print ("usage: "+argv[0]+" 'Anzahl'")
	print ("Es wird per default Anzahl 8 berechnet")
	argv.append(8)

anz = int(argv[1])

def firstn(g, n):
	for i in range(n):
		yield g.next()

def intsfrom(i):
	while 1:
		yield i
		i = i + 1

def exclude_multiples(n, ints):
	for i in ints:
		if (i % n): yield i

def sieve(ints):
	while 1:
		prime = ints.next()
		yield prime
		ints = exclude_multiples(prime, ints)
	
if __name__ == '__main__':
	for i in firstn(sieve(intsfrom(2)), anz):
		print(i, end=" ")
