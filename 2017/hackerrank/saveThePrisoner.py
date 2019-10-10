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
 
def saveThePrisoner (n, m, s):
    def smod (x, y):
        mod = x % y
        return mod if mod else y
    return smod (smod (m, n) + (s - 1), n)
    
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nms = input ().split ()
        n = int (nms [0])
        m = int (nms [1])
        s = int (nms [2])
        result = saveThePrisoner (n, m, s)
        print ("\n" + str (result))
        fptr.write(str(result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
