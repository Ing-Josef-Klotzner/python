#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Mon Sep 25 23:16:54 2017

@author: josef
"""

from subprocess import call

def main():
    call("python /usr/lib/python2.7/lib-tk/turtle.py", shell=True)

if __name__ == '__main__':
    main()
