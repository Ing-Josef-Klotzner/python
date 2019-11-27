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

def reverse (x):
    res = 0
    while (x > 0):
        res = res * 10 + x % 10
        x //= 10
    return res
 
def viralAdvertising (n):
    receipt = 5
    sum_liked = 0
    for i in range (n):
        liked = receipt // 2
        sum_liked += liked
        receipt = liked * 3
    return sum_liked

def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    n = int (input ())
    result = viralAdvertising (n)
    print ("\n" + str (result))
    fptr.write(str(result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
