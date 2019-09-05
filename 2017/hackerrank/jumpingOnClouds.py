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

def jumpingOnClouds (n, c, k):
    e = 100; i = 0
#    c.append (c [0])
#    # shortened c, only n + 1 // k elements
#    s_c = [c[i] for i in range (k, n + 1, k)]
    while True:
        if c [i]: e -= 2
        e -= 1
        print (i, c [i], e)
        i += k
        if not i % n or i > n:
            break
    return e

def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    nk = input ().split ()
    n = int (nk [0])
    k = int (nk [1])
    c = list (map (int, input ().rstrip ().split ()))
    result = jumpingOnClouds (n, c, k)
    print (result)
    fptr.write(str (result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main ()

"""
tc0:
8 2
0 0 1 0 0 1 1 0
out: 92

tc1:
constraint n % k == 0 not held !!
10 3
1 1 1 0 1 1 0 0 0 0
out: 94
"""
