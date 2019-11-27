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

class Node:
    def __init__ (self, info, left = None, right = None, level = None):
        self.info = info
        self.left = left
        self.right = right
        self.level = level
        self.hd = 0
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
                    else: current.left = Node (value, level = 1); break
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

def main ():
    tree = BinarySearchTree ()
    t = int (input ())
    arr = list (map (int, input ().split ()))
    for i in range (t): tree.create (arr [i])
    tree.levelOrder (tree.root)

if __name__ == '__main__':
    main ()
