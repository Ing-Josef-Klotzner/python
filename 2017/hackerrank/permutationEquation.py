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

def mkidxL (arr):
    idxL = arr + [0] # for index 1:1
    for i in range (len (arr)):
        idxL [arr [i]] = i + 1
    return idxL

# index can be evaluated by creating an index list -> lookup O(1)
def permutationEquation(n, p):
#    # O (n * n)
#    return [(p.index(p.index(i)+1)+1) for i in range(1, max(p)+1)]
    idxL = p + [0] # for index 1:1
    for i in range (n):
        idxL [p [i]] = i + 1
    # O (n)
    return [idxL [idxL [i]] for i in range (1, n + 1)]
        
def main ():
    fptr = open(environ['OUTPUT_PATH'], 'w')
    n = int (input ())
    p = list (map (int, input ().rstrip ().split ()))
    result = permutationEquation (n, p)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

if __name__ == '__main__':
    main ()

"""
18
2 5 11 10 1 14 7 3 16 9 8 6 18 12 15 17 13 4

p [p [13]] = 4
p [18] = 4

out:
2
5
11
13
1
14
7
3
4
18
8
6
16
12
15
10
9
17
"""
