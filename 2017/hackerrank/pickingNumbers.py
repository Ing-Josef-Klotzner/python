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

def pickingNumbers (a):
    # count for number is held by its index
    nmbrCnt = [0] * 100
    # count occurance of each number
    # alternativ, aber langsamer, weil dict: from collections import Counter
    # >>> Counter ([1,1,4,7,9,4,3,6,4,3])
    # Counter({4: 3, 1: 2, 3: 2, 7: 1, 9: 1, 6: 1})
    for nr in a:
        nmbrCnt [nr] += 1
    # find out maximum count of "neighboured" numbers
    maxCt = 0
    for i in range (1, 99):
        maxCt = max (maxCt, nmbrCnt [i] + nmbrCnt [i + 1])
    return maxCt
    
    # genialer mit "fold" (reduce)
    # print reduce(lambda y, x:max(arr[x] + arr[x + 1], y), range(100), -1)

if __name__ == '__main__':
    fptr = open(environ['OUTPUT_PATH'], 'w')
    n = int (input().strip ())
    a = list (map (int, input ().rstrip ().split ()))
    result = pickingNumbers (a)
    print (result)
    fptr.write(str (result) + '\n')
    fptr.close()
