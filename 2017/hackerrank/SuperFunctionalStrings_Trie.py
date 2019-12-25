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
# operation in a Trie

class TrieNode:
    # Trie node class
    def __init__ (self):
        self.children = [None] * 26
        self.child_ixs_objs = []

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
    def insert (self, key):
        # If not present, inserts key into trie. If the key
        # is prefix of trie node, just marks leaf node
        pCrawl = self.root
        for char in key:
            ix = self._charToIndex (char)
            # if current character is not present
            if not pCrawl.children [ix]:
                pCrawl.children [ix] = self.getNode ()
                pCrawl.child_ixs_objs.append ((ix, pCrawl.children [ix]))
            pCrawl = pCrawl.children [ix]
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
                print (chr (ix + ord ('a')), end = " ")
                ln = len (ob.child_ixs_objs)
                if ln > 1: print (ln, end = "")
                if ob.isEndOfWord: print ('*', end = "  ")
                dfs (ob)
        dfs (pCrawl)

# driver function
def main ():
    # Input keys (use only lower case 'a' through 'z'
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]
    # Trie object
    t = Trie ()
    # Construct trie
    for key in keys:
        t.insert (key)
    # Search for different keys
    print ("{} ---- {}".format ("the", output [t.isIn ("the")]))
    print ("{} ---- {}".format ("these", output [t.isIn ("these")]))
    print ("{} ---- {}".format ("their", output [t.isIn ("their")]))
    print ("{} ---- {}".format ("thaw", output [t.isIn ("thaw")]))
    print ("trie content:")
    t.printTrie ()
    print ()
    print ("* indicates word¹ ending, number shows count of following")
    print ("suffixes creating new words together with word¹")

if __name__ == '__main__':
    main ()

