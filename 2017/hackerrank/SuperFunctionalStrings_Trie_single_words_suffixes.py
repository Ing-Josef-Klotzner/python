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

# Python program for insert and search
# operation in a Trie calculating distinct
# count of (distint) suffixes

class TrieNode:
    # Trie node class
    def __init__ (self):
        self.children = [None] * 26
        self.child_ixs_objs = []
        self.len_bra = 0       # length of branch
        self.dst_cnt = 0
        self.papaIsRoot = False
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
    def insert (self, key, dst_cntL_ = []):
        # If not present, inserts key into trie. If the key
        # is prefix of trie node, just marks leaf node
        pCrawl = self.root
        for il, char, in enumerate (key):
            ix = self._charToIndex (char)
            # if current character is not present
            child = pCrawl.children [ix]
            if not child:
                pCrawl.children [ix] = child = self.getNode ()
                pCrawl.child_ixs_objs.append ((ix, child))
                pCrawl.isEndOfWord = True
                if pCrawl == self.root:
                    child.papaIsRoot = True
                child.len_bra = len (key) - il
                child.dst_cnt = dst_cntL_ [il]
            pCrawl = child
        # mark last node as leaf
        pCrawl.isEndOfWord = True
    def isIn (self, key):
        # Search key in the trie. Returns true if key 
        # is present in trie, else false
        pCrawl = self.root
        for char in key:
            index = self._charToIndex (char)
            if not pCrawl.children [index]:
                return False
            pCrawl = pCrawl.children [index]
        return pCrawl != None and pCrawl.isEndOfWord
    def printTrie (self):
        pCrawl = self.root
        def dfs (pCrl):
            for ix, ob in pCrl.child_ixs_objs:
                if ob.papaIsRoot: 
                    print ()
                    print ("Ast:", end = " ")
                print (chr (ix + ord ('a')), end = " ")
                ln = len (ob.child_ixs_objs)
                if ln > 1: print (ln, end = "")
                if ob.isEndOfWord: print ('*', end = "  ")
                dfs (ob)
        dfs (pCrawl)
    def get_len_dist (self):
        pCrawl = self.root
        def dfs (pCrl):
            for _, ob in pCrl.child_ixs_objs:
                yield (ob.len_bra, ob.dst_cnt)
                yield from dfs (ob)
        yield from dfs (pCrawl)

class DistinctCounter:
    def __init__ (self):
        self.a_z_arr = [0] * 26
        # distinct count
        self.d_cnt = 0
        self.d_cntL = []
    def get_ix (self, x):  # get index
        return ord (x) - ord ('a')
    def init (self, s):
        n = len (s)
        for i in range (n):
            self.add (s [i])
        # init self.d_cntL
        for i in range (n):
            self.d_cntL.append (self.d_cnt)
            self.sub (s [i])
        return self.d_cntL
    # if count was 0 increment distint counter
    # add char to a-z array (relative index - shift by 65)
    def add (self, x):
        ix = self.get_ix (x)
        if not self.a_z_arr [ix]: self.d_cnt += 1
        self.a_z_arr [ix] += 1
    # subtract char from a-z array (relative index)
    # decrement distinct counter when reaching 0
    def sub (self, x):
        ix = self.get_ix (x)
        self.a_z_arr [ix] -= 1
        if not self.a_z_arr [ix]: self.d_cnt -= 1

# driver function
def main ():
    # Input keys (use only lower case 'a' through 'z'
    # building prefixes of test word "azaza"
    testword = "aba"
    # each suffix has list holding it's distinct count (to end of string)
    dst = DistinctCounter ()
    dst_cntL = dst.init (testword)
    def suffixes (_testword):
        for i in range (len (_testword)):
            yield (_testword [i : ], dst_cntL [i : ])
    keys = suffixes (testword)
    output = ["Not present in trie",
              "Present in trie"]
    # Trie object
    t = Trie ()
    # Construct trie with suffixes and distinct count lists of testword
    for key, dst_cntL_ in keys:
        t.insert (key, dst_cntL_)
    # Search for different keys
    print ("{} ---- {}".format ("a", output [t.isIn ("a")]))
    print ("{} ---- {}".format ("ab", output [t.isIn ("ab")]))
    print ("{} ---- {}".format ("aba", output [t.isIn ("aba")]))
    print ("{} ---- {}".format ("b", output [t.isIn ("b")]))
    print ("{} ---- {}".format ("ba", output [t.isIn ("ba")]))
    print ("trie content:")
    t.printTrie ()
    print ()
    print ("* indicates word¹ ending, number shows count of following")
    print ("branches creating new words together with word¹")
    for _, ob in t.root.child_ixs_objs:
        print (ob.len_bra, end = " ")
    print ()
    print ("these are alle pairs of (length, and distinct substring length)")
    for len_, distinct_len in t.get_len_dist ():
        print (len_, distinct_len, end = "  ")

if __name__ == '__main__':
    main ()

