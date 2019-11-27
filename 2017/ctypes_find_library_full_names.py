#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Fri Sep  8 02:34:12 2017

@author: josef
"""

from ctypes.util import find_library
 
llibs = ('bz2', 'c', 'm',)
 
for s in llibs:
    print (s + ':  ' + str(find_library(s)))