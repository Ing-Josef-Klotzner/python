#!/usr/bin/python3
# -*- coding: utf-8 -*-

def recip_square_cy2 (i):
    x = i ** 2
    s = 1 / x
    return s

def apr_pi (n):
    """Compute an approximate value of pi."""
    val = 0
    for k in range (1, n + 1):
        x = recip_square_cy2 (k)
        val += x
    pi = (6 * val) ** .5
    return pi
