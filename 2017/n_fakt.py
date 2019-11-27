#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Wed Aug 23 15:59:32 2017

@author: josef
"""
from sys import argv

def fakt(n):   # n!
    if n == 1:
        return 1
    else:
        n -= 1
        return (n+1) * fakt(n)

def main():
    if len(argv) == 1:
    	print ("usage: "+argv[0]+" 'number'")
    	print ("Es wird per default n!(8) berechnet")
    	argv.append(8)
    
    if int(argv[1]) > 0:
        print(fakt(int(argv[1])))
    else:
        print("0")


if __name__ == "__main__":
    main()
