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

from os import environ

def getMoneySpent(keyboards, drives, b):
    maxCost = -1
    for kb_cost in keyboards:
        for usb_cost in drives:
            cost = kb_cost + usb_cost
            if cost <= b: maxCost = max (cost, maxCost)
    return maxCost

if __name__ == '__main__':
    fptr = open(environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    #
    # The maximum amount of money she can spend on a keyboard and USB drive,
    # or -1 if she can't purchase both items
    #
    moneySpent = getMoneySpent(keyboards, drives, b)
    print (moneySpent)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
