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

def circularArrayRotation (n, a, k, queries):
    resL = []
    for index in queries:
        shifted = (index - k) % n
        res = a [shifted]
        print (res)
        resL.append (res)
    return resL
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    nkq = input ().split ()
    n = int (nkq [0])
    k = int (nkq [1])
    q = int (nkq [2])
    a = list (map (int, input ().rstrip ().split ()))
    queries = []
    for _ in range (q):
        queries_item = int (input ())
        queries.append (queries_item)
    result = circularArrayRotation (n, a, k, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

if __name__ == '__main__':
    main ()
