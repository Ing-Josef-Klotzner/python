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
          - - 1 - -
        /           \
        2           3
      /   \       /   \
     4     5     6     7
          / \
         8   9
Euler Tour:
Index  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
Node # 1 2 4 2 5 8 5 9 5 2  1  3  6  3  7  3  1   -> 1)
level  0 1 2 1 2 3 2 3 2 1  0  1  2  1  2  1  0   -> 2)

Node # 1 2  3 4 5  6  7 8 9
fstAp  0 1 11 2 4 12 14 5 7   -> 3)

1) Nodes visited in order of Euler tour of T
2) Level of each node visited in Euler tour of T
3) Index of the first appearance of a node in Euler tour of T
(since any occurrence would be good, let’s track the first one)

Algorithm:

1. Do a Euler tour on the tree, and fill the euler,
    level and first appearance arrays.
2. Using the first appearance array, get the indices corresponding
    to the two nodes which will be the corners of the range in the
    level array that is fed to the RMQ algorithm for the minimum value.
3. Once the algorithm return the index of the minimum level in the range,
    we use it to determine the LCA using Euler tour array.

Better approach - see kittysCalculationsOnTree.cpp
using centroid decomposition
"""
class RangeMinimum (object):
    "Data structure providing efficient range-minimum queries."
    def __init__ (self, numbers):
        "Build a RangeMinimum object for the given sequence of numbers."
        # Mapping from (start, step) to min (numbers [start : start + 2**step])
        self._rmq = rmq = {(i, 0): m for i, m in enumerate (numbers)}
        n = len (numbers)
        for step, i in product (range (1, n.bit_length ()), range (n)):
            j = i + 2 ** (step-1)
            if j < n:
                rmq [i, step] = min (rmq [i, step - 1], rmq [j, step - 1])
            else:
                rmq [i, step] = rmq [i, step - 1]
    def query (self, start, stop):
        "Return min (numbers [start : stop])."
        if start > stop: start, stop = stop, start
        j = max ((stop - start).bit_length () - 1, 0)
        x = self._rmq [start, j]
        y = self._rmq [stop - 2 ** j, j]
        return min (x, y)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n, q = map (int, input ().split ())
    # build the tree as list, Euler path, level and first appearance list
    tree = [[] for _ in range (n + 1)] # Adjacency list representation of tree
    tree [0] = [[], 0]
#    Euler = []   # Array to store Euler Tour
    Eu_lvl = []  # Array to store level on Euler Tour
    fstAp = [0] * (n + 1)
    lstAp = [0] * (n + 1)
    def add_edge (u, v): # Function to add edges to tree 
#        if u > v: u, v = v, u
        if not tree [u]: tree [u] = [[v], 0]  # [[children], level]
        else: tree [u] [0].append (v); # u, v ... nodes
        if not tree [v]: tree [v] = [[u], tree [u] [1] + 1]
        else: tree [v] [0].append (u); 
    def mkEuler (u = 1, prev = 0, lvl = 0):  # store Euler Tour of tree
        global once, btl, btr
        if not fstAp [u]: fstAp [u] = len (Eu_lvl)
        #lstAp [u] = len (Eu_lvl)
#        Euler.append (u)
        Eu_lvl.append (lvl)
        # fstAp, Eu_lvl Liste füllen ... Euler Liste selbst brauch ma nicht
        if len (tree [u] [0]) == 1:
            if once: once = False; btl = u
            if tree [u] [1] >= tree [btr] [1]: btr = u # last lowest level = btr
        for it in tree [u] [0]:
#            if it == tree [u] [0] [0]:
#                if tree [u] [1] > tree [btl] [1]: btl = u # first lowest level = btl
            if it != prev:
                mkEuler (it, u, lvl + 1)
#                Euler.append (u)
                Eu_lvl.append (lvl)
                lstAp [it] = len (Eu_lvl)
    for _ in range (n - 1):
        b, a = map (int, input ().rstrip ().split ())
        add_edge (a, b)
    global once, btl, btr  # bottom left, bottom right
    nr = 23
#    print ("Node", nr, tree [nr])
#    if len (tree [nr] [0]) > 1:
#        for chld in tree [nr] [0]:
#            if chld == tree [nr] [0] [0]: continue
#            print ("child", chld, tree [chld], end = "   ")
#        print () 
    once = True; btl = 1; btr = 1
    mkEuler ()
#    print ("bottom left", btl)
    rmq = RangeMinimum (Eu_lvl)
    for _ in range (q):
        k = int (input ())   # size of set
        set_ = list (map (int, input ().rstrip ().split ()))
        result = 0
        if k < 2:
            fptr.write (str (result) + "\n")
            continue

#        set_ = sorted (set_, key = lambda x: -fstAp [x], reverse = True)
##        print (set_)
#        lca_l = [0] * (n + 1)
#        lca_l [set_ [0]] = rmq.query (fstAp [set_ [0]], fstAp [set_ [1]])
#        for nx in range (1, k):
#            st_1 = set_ [nx - 1]
#            st = set_ [nx]
#            lca = (rmq.query (fstAp [st_1], fstAp [st]))
#            lca_l [st] = lca

        #set_ = sorted (set_, key = lambda x: (lca_l [x], -fstAp [x]), reverse = True)
#        set_ = sorted (set_, key = lambda x: lca_l [x], reverse = True)

#        set_r = sorted (set_, key = lambda x: lca_r [x], reverse = True)
        #print (btl, tree [btl], lca_l [btl], btr, tree [btr],lca_r [btr])
#        for i in range (k):
#            print (set_ [i], tree [set_ [i]], lca_l [set_ [i]])

#        for i in set_:
#            print (i, lca_l [i], end = "  ")


#        c1 = c2 = 0
#        def c2_ (x, mx):
#            if not x: return 0
#            return set_ [x - 1] * (tree [set_ [x - 1]] [1] - tree [set_ [mx]] [1]) + c2_ (x - 1, mx)
#        for nx in range (1, k):
#            c1 = c1 + set_ [nx - 1]
#            c2 = c2_ (nx - 1, nx - 1)
##            print (c1, c2)
#            lca = rmq.query (fstAp [set_ [nx - 1]], fstAp [set_ [nx]])
#            dp_lca = tree [set_ [nx - 1]] [1] - lca
#            dc_lca = tree [set_ [nx]] [1] - lca
#            result += (c1 * dp_lca + c2) * set_ [nx] + set_ [nx] * dc_lca * c1
##            print (result)

        for u, v in combinations (set_, 2):
            lca = rmq.query (fstAp [u], fstAp [v])
            dist = tree [u] [1] + tree [v] [1] - 2 * lca
#            print (u, tree [u] [1], v, tree [v] [1], lca, dist)
            result += u * v * dist
        result %= (10 ** 9 + 7)
        fptr.write (str (result) + "\n")
    fptr.close ()

if __name__ == '__main__':
    main ()
