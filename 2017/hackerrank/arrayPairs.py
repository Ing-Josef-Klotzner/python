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
from bisect import bisect_right
#from math import factorial as fac
from collections import deque   #, defaultdict
#from time import time   #sleep
#from functools import reduce
from copy import deepcopy
#from operator import mul
#from itertools import product, combinations
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

# when using enable deque and deepcopy import above
def solve_p (a):  # with pre-computed init lists for j
    res = 0   # simple, faster with windowing max
    q = deque ([0])   # slower than solve ()
    qL = [0]   # initial lists of deques for each j
    for j in range (1, len (a)):
        while q and a [j] >= a [q [-1]]: q.pop ()
        q.append (j)
        qL.append (deepcopy (q))
    for j in range (1, len (a)):
        for i in range (j):
            #print (j, end = " ")
            mx = a [qL [j] [0]]
            while qL [j] and qL [j] [0] <= i: qL [j].popleft ()
            if (a [i] * a [j] <= mx): res += 1
    return res

def solve_w (a):
    res = 0   # simple, faster with windowing max
    q = q_init = deque ([0])
    for j in range (1, len (a)):
        q = deepcopy (q_init)
        while q and a [j] >= a [q [-1]]: q.pop ()
        q.append (j)
        q_init = deepcopy (q)
        for i in range (j):
            mx = a [q [0]]
            while q and q [0] <= i: q.popleft ()
            if (a [i] * a [j] <= mx): res += 1
    return res

def solve__ (arr):
    res = 0   # simple but slowest - combining all
    for j in range (1, len (arr)):
        for i in range (j):
            mx = max (arr [i : j + 1])
            if (arr [i] * arr [j] <= mx): 
                res += 1
#                print (res, arr [i], "*", arr [j], "=", arr [i] * arr [j], "<=", mx, end = "  ")
    return res

# check for pairs in left / right along with max
def check (max_, left, right):
    if not left and not right: return
    # check max w. left / max w. right / left w. right
    global counter
    left = sorted (left)
    right = sorted (right)
    if left and left [0] == 1: counter += bisect_right (left, 1)
    if right and right [0] == 1: counter += bisect_right (right, 1)
    if left and right: counter += lrCheck (left, right, max_)
# finding counts while comparing left and right parts of max
def lrCheck (left, right, max_):
    global counter
    total = 0
    ll = len (left)
    lr = len (right)
    l = bisect_right (left, max_ // right [0])   # len (left) - 1
    if l > ll - 1: l -= 1
    r = 0
    lbr = bisect_right (right, max_ // left [0])
    while l >= 0 and r < lbr:
        if left [l] * right [r] <= max_:
            r += 1
            total += l + 1
        else: l -= 1
    return total

# return mid most position of max elem and max elem
def getMidMax (arr):
    max_list = []
    max_value = 0
    for i, value in enumerate (arr):
        if value > max_value:
            max_value = value
            max_list = []
        if value == max_value:
            max_list.append (i)
    mid_index = max_list [len (max_list) // 2]
    return max_value, mid_index

def solve (arr):
    global counter
    solve_n (arr)
    return counter

def solve_n (arr):
    global counter
    if not arr: return
    max_value, index = getMidMax (arr)
    left = arr [ : index]
    right = arr [index + 1: ]
    solve_n (left)
    solve_n (right)
    check (max_value, left, right)

def main ():
    global counter
    counter = 0
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    arr_count = int (input ())
    arr = list (map (int, (input ().rstrip ().split ())))
    result = solve (arr)
    fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

