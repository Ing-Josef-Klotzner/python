#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

def depositProfit (deposit, rate, threshold):
    for i in range (1, 1000):
        deposit *= (1 + (rate / 100))
        #print (deposit)
        if deposit >= threshold:
            break
    return i

def main ():
    deposit = 100; rate = 20; threshold = 170
    print (depositProfit (deposit, rate, threshold))

if __name__ == '__main__':
    main ()
