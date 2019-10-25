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
from itertools import product, combinations
#from collections import deque   #defaultdict
#from time import sleep   #time
#from sys import exit  #, maxsize

from sys import setrecursionlimit
setrecursionlimit (100000)

"""
Level k: 10^(2^(k-1)) =>
Level 0: 10^0         => [0-0], [1-1] ... [10-10]
Level 1: 10^1         => [1-10], [11-20] ... [91-100]
Level 2: 10^2         => [1-100], [101-200] ... [9901-10000]
Level 3: 10^4         => [1-10000], [10001-20000] ... [99990001-100000000]
Level 4: 10^8         => [1-100000000], [100000001-200000000] ... [9999999900000001-10000000000000000]

L=42 R=1024 Output : 5, 0 9, 1 5, 2 9, 1 2, 0 4
How is output came?
    [42; 1024] =
    [42; 42] + [43; 43] + ... + [50; 50] (9 of level 0) +
    [51; 60] + [61; 70] + ... [91; 100] (5 of level 1) +
    [101; 200] + [201; 300] + ... + [901; 1000] (9 of level 2) +
    [1001; 1010] + [1011; 1020] (2 of level 1) +
    [1021; 1021] + [1022; 1022] + [1023;1023] + [1024; 1024] (4 of level 0)
"""

def solve (l, r, k, num_digits):
    if k == 0:
        return [(0, r - l + 1)]
    step = int ('1' + '0' * (num_digits [k] - 1))
    k_left = 0 if l == 0 else ((l - 1) // step + 1) * step
    k_right = (r + 1) // step * step - 1
    res = []
    if k_left > k_right:
        return solve (l, r, k - 1, num_digits)
    if k_left != l:
        res += solve (l, min (k_left - 1, r), k - 1, num_digits)
    if k_left < k_right:
        res += [(k, (k_right + 1 - k_left) // step)]
    if k_right != r:
        res += solve (max (l, k_right + 1), r, k - 1, num_digits)
    return res


def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')

    l, r = map (lambda x: int (x) - 1, [input (), input ()])
    l_str, r_str = map (str, [l, r])

    num_zeros = [0, 1]

    while num_zeros [-1] < len (r_str) - 1:
        num_zeros.append (num_zeros [-1] * 2)

    num_digits = list (map (lambda x: x + 1, num_zeros))
    print (l, r, num_zeros, num_digits)
    res = solve (l, r, len (num_digits) - 1, num_digits)
    #print (len (res))
    fptr.write (str (len (res)) + "\n")
    for el in res:
        #print (el [0], el [1])
        fptr.write (str (el [0]) + " " + str (el [1]) + "\n")
    fptr.close ()

if __name__ == '__main__':
    main ()
