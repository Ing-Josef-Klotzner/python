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
from bisect import bisect
from functools import reduce

#    position = bisect.bisect_left(l, r)
#    bisect.insort_left(l, r)

def angryProfessor (k, a):
    studentsInTime = reduce (lambda y, x: y + 1 if x <= 0 else y, a, 0)
    print (studentsInTime)
    if k > studentsInTime: return "YES"
    else: return "NO"

def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    t = int (input())
    for t_itr in range (t):
        nk = input ().split ()
        n = int (nk [0])
        k = int (nk [1])
        a = list (map (int, input ().rstrip ().split ()))
        result = angryProfessor (k, a)
#        print ("\n" + result)
        fptr.write(result + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()
