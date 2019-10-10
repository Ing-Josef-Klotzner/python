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
from collections import deque   #defaultdict
from time import sleep   #time
from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
"""

import queue as Queue
cntr = 0
class Node:
    def __init__ (self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global cntr
        self._count = cntr
        cntr = cntr + 1
    def __lt__ (self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

class BinarySearchTree:
    def __init__ (self, root = None):
        self.root = root
    def create (self, value):
        if not self.root: self.root = Node (value)
        else:
            current = self.root
            while True:
                if value < current.info:
                    if current.left: current = current.left
                    else: current.left = Node (value); break
                elif value > current.info:
                    if current.right: current = current.right
                    else: current.right = Node (value); break
                else: break
    def preOrder (self, root):  #Preorder (Root, Left, Right)
        if root:
            print (root.info, end = " ")
            self.preOrder (root.left)
            self.preOrder (root.right)
    def postOrder (self, root):  #Postorder (Left, Right, Root)
        if root:
            self.postOrder (root.left)
            self.postOrder (root.right)
            print (root.info, end = " ")
    def inOrder (self, root):  #Postorder (Left, Root, Right)
        if root:
            self.inOrder (root.left)
            print (root.info, end = " ")
            self.inOrder (root.right)
    def height (self, root):
        if not root: return -1
        else:
            lheight = self.height (root.left)
            rheight = self.height (root.right)
            if lheight > rheight: return lheight + 1
            else: return rheight + 1
    def topView (self, root):
        if not root: return
        q = deque ([root]); m = dict ()
        while len (q):
            root = q [0]
            hd = root.hd
            if hd not in m: m [hd] = root.info
            if root.left: root.left.hd = hd - 1; q.append (root.left)
            if root.right: root.right.hd = hd + 1; q.append (root.right)
            q.popleft ()
        for i in sorted (m):
            print (m [i], end = " ")
    def levelOrder (self, root):
        if root is None: return
        q = [root]
        while (len (q) > 0):
            print (q [0].info, end = " ")
            n = q.pop (0)
            if n.left: q.append (n.left)
            if n.right: q.append (n.right)
    def insert (self, val):
        if not self.root: self.root = Node (value)
        else:
            current = self.root
            while True:
                if value < current.info:
                    if current.left: current = current.left
                    else: current.left = Node (value); break
                elif value > current.info:
                    if current.right: current = current.right
                    else: current.right = Node (value); break
                else: break

def huffman_hidden ():  #builds the tree and returns root
    global freq
    q = Queue.PriorityQueue ()
    for key in freq:
        q.put ((freq [key], key, Node (freq [key], key)))
    while q.qsize () != 1:
        a = q.get ()
        b = q.get ()
        obj = Node (a [0] + b [0], '\0' )
        obj.left = a [2]
        obj.right = b [2]
        q.put ((obj.freq, obj.data, obj))
    root = q.get ()
    root = root [2]  #contains root object
    return root

def dfs_hidden (obj, already):
    global code_hidden
    if not obj: return
    elif (obj.data != '\0'):
        code_hidden [obj.data] = already
    dfs_hidden (obj.right, already + "1")
    dfs_hidden (obj.left, already + "0")

def decodeHuff (root, s):
    ans = ''
    curr = root
    for i in range (len (s)):
        if (s [i] == '0'): curr = curr.left
        else: curr = curr.right
        if not curr.left and not curr.right:
            ans = ans + curr.data
            curr = root
    print (ans)

def main ():
    ip = input ()
    global freq
    freq = {}  #maps each character to its frequency
    cntr = 0
    for ch in ip:
        if not freq.get (ch): freq [ch] = 1
        else: freq [ch] += 1
    root = huffman_hidden ()  #contains root of huffman tree
    global code_hidden
    code_hidden = {}  #contains code for each object
    dfs_hidden (root, "")
    if len (code_hidden) == 1:  #if there is only one character in the i/p
        for key in code_hidden: code_hidden [key] = "0"
    toBeDecoded = ""
    for ch in ip: toBeDecoded += code_hidden [ch]
    decodeHuff (root, toBeDecoded)

if __name__ == '__main__':
    main ()
