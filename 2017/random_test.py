#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Wed Feb 07 18:38:02 2018

@author: josef
"""
import random

# ran(lower limit, upper limit)  ... min 
def ran(ll=0, ul=1):
    ra = random.random()
    return ra * (ul - ll) + ll

print(ran())
print("ran(ll, ul) returns a random numer in range of lower limit (ll) and upper limit (ul)")
print("default range for ran () is 0 - 1")

#range of r (random() ... 0 - 1)
#  ul - ll  ...  random range
#  r * (ul - ll ) + ll 
