#! /usr/bin/env python2
# Measure some strings:
# -*- coding: iso-8859-15 -*-
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

# Now call the function we just defined:
fib(2000)