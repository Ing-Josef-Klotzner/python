#! /usr/bin/env python2
# Measure some strings:
# -*- coding: iso-8859-15 -*-
def fib2(n): # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while b < n:
		result.append(b)    # see below
		a, b = b, a+b
	return result

f100 = fib2(100)    # call it
print f100                # write the result