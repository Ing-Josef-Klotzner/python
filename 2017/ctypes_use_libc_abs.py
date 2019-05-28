#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Fri Sep  8 00:56:00 2017

@author: josef
"""

from ctypes import CDLL
 
slibc = 'libc.so.6'
hlibc = CDLL(slibc)
 
iret = hlibc.abs(-7)
print (iret)