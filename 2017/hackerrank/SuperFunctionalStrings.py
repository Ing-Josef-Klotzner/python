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
#from itertools import permutations, combinations, product
#from bisect import bisect_right, bisect_left
#from math import factorial as fac
#from collections import defaultdict   # , deque
#from time import time   #sleep
from functools import reduce
#from operator import add    #mul
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (10000)

class TrieNode:
    # Trie node class
    def __init__ (self):
        #self.children = defaultdict (list)
        self.children = dict ()   #[None] *26
        self.child_ixs_objs = []
        self.len_bra = 0
        self.dst_cnt = 0
#        self.papaIsRoot = False
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False

class Trie:
    # Trie data structure class
    def __init__ (self):
        self.root = self.getNode ()
    def getNode (self):
        # Returns new trie node (initialized to NULLs)
        return TrieNode ()
    def _charToIndex (self, ch):
        # private helper function - Converts key current character
        # into index. Use only 'a' through 'z' and lower case
        return ord (ch) - ord ('a')
    def insert (self, key_):
        # If not present, inserts key_ into trie. If the key_
        # is prefix of trie node, just marks leaf node
        pCrawl = self.root
        dst = DistinctCounter ()
        for il in range (len (key_)):
            char = key_ [il]
            pCrawl.isEndOfWord = True
            ix = self._charToIndex (char)
            # if current character is not present
            child = None
            if ix in pCrawl.children:
                child = pCrawl.children [ix]
            if not child:
                pCrawl.children [ix] = child = self.getNode ()
                pCrawl.child_ixs_objs.append ((ix, child))
                pCrawl.children [ix].isEndOfWord = True
#                if pCrawl == self.root:
#                    child.papaIsRoot = True
            dst_cnt = dst.add (char)
#            print (il, char, key_, il + 1, dst_cnt, end = "  ")
            #yield (len (key_) - il, dst_cnt)
            child.len_bra = il + 1
            child.dst_cnt = dst_cnt
#            print (child.len_bra, child.dst_cnt)
            pCrawl = child
        # mark last node as leaf
        pCrawl.isEndOfWord = True
    def isIn (self, key_):
        # Search key_ in the trie. Returns true if key_ 
        # is present in trie, else false
        pCrawl = self.root
        for char in key_:
            index = self._charToIndex (char)
            if not pCrawl.children [index]:
                return False
            pCrawl = pCrawl.children [index]
        return pCrawl != None and pCrawl.isEndOfWord
    def printTrie (self):
        pCrawl = self.root
        def dfs (pCrl):
            for ix, ob in pCrl.child_ixs_objs:
#                if ob.papaIsRoot: 
#                    print ()
#                    print ("Ast:", end = " ")
#                print (chr (ix + ord ('a')), end = " ")
                ln = len (ob.child_ixs_objs)
                if ln > 1: print (ln, end = "")
                if ob.isEndOfWord: print ('*', end = "  ")
#                if len (pCrl.child_ixs_objs) == ix + 1:
#                    print ('|', end = "")
                dfs (ob)
        dfs (pCrawl)
#        print ()
#        print ("* indicates word¹ ending, number shows count of following")
#        print ("branches creating new words together with word¹")
    def get_len_dist (self):
        pCrawl = self.root
        def dfs (pCrl):
            for _, ob in pCrl.child_ixs_objs:
#                print (ob.len_bra, ob.dst_cnt, end = "  ")
                yield (ob.len_bra, ob.dst_cnt)
                yield from dfs (ob) #, bra)
        yield from dfs (pCrawl)

class DistinctCounter:
    def __init__ (self):
        self.a_z_arr = [0] * 26
        # distinct count
        self.d_cnt = 0
    def get_ix (self, x):  # get index
        return ord (x) - ord ('a')
    # if count was 0 increment distint counter
    # add char to a-z array (relative index - shift by 65)
    def add (self, x):
        ix = self.get_ix (x)
        if not self.a_z_arr [ix]: self.d_cnt += 1
        self.a_z_arr [ix] += 1
        return self.d_cnt
    # subtract char from a-z array (relative index)
    # decrement distinct counter when reaching 0
    def sub (self, x):
        ix = self.get_ix (x)
        self.a_z_arr [ix] -= 1
        if not self.a_z_arr [ix]: self.d_cnt -= 1



def superFunctionalStrings_ (s):
    mod = 1000000007
    res = 0
    def suffixes (_testword):
        lt = len (_testword)
        for i in range (lt):
            yield _testword [i : ]
    # Trie object
    t = Trie ()
    # Construct trie with suffixes and distinct count lists of testword
    for key in suffixes (s):
#        print ()
#        print (key, end = "  ")
        t.insert (key)
    for len_, distinct_len in t.get_len_dist ():
        res = (res + len_ ** distinct_len) % mod
#    t.printTrie ()
    return res

# simple, correct, but slow - lower memory using generator - little faster
def superFunctionalStrings__ (s):
    length = len (s)
    mod = 10 ** 9 + 7
    res = 0
    # precalculate break even point where distinct does not change any more
    dst = DistinctCounter ()
    mx = 0
    for j in range (length):
        dst.add (s [j])
        mx_new = max (mx, dst.d_cnt)
        if mx_new > mx:
            mx = mx_new
            mx_i = j
            print ("initial new max", mx, "at", j, end = "   ")
    def subs ():
        d_subs = set ()
        for j in range (length):
            dst = DistinctCounter ()
            for i in range (j + 1, length + 1):
                sub = s [j: i]
                subh = hash (sub)
                dst.add (s [i - 1])
                if subh not in d_subs:
                    yield (len (sub), dst.d_cnt)
                    #print (s [j : i], dst.d_cnt)  #, end = " ")
                    d_subs.add (subh)
    for b, d in subs ():
        res = res + (b ** d) % mod
    
#    def f (y, x): return (y + x) % mod
#    return reduce (f, (b ** d for b, d in subs ()))
    #return sum (len (b) ** len (set (b)) for b in substrs) % mod
    return res

# simple, correct, but slowvon
def superFunctionalStrings (s):
    length = len (s) + 1
    mod = 10 ** 9 + 7
    substrs = {s [j: i] for j in range (length) for i in range (j + 1, length)}
    def f (y, x):
        return (y + x) % mod
    return reduce (f, (len (b) ** len ( set (b)) for b in substrs))
    #return sum (len (b) ** len (set (b)) for b in substrs) % mod

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        s = input ().rstrip ()
        result = superFunctionalStrings__ (s)
#        print ("neu", result)
#        print ("richtig", superFunctionalStrings (s))
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
There are 26 characters, and only maximum 26 times will the distinct characters count change. So instead of 100K operations you only need 26 (give or take) operations per suffix. some preprocessing and precomputing similar to your cached precomputed powers is required. 
"""
