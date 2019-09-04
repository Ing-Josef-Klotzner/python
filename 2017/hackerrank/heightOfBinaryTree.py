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
#from collections import defaultdict
#from time import time
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

def height (root):
    if not root: return -1
    else:
        lheight = height (root.left)
        rheight = height (root.right)
        if lheight > rheight: return lheight + 1
        else: return rheight + 1

def main ():
    tree = BinarySearchTree ()
    t = int (input ())
    arr = list (map (int, input ().split ()))
    for i in range (t):
        tree.create (arr [i])
    print (height (tree.root))

if __name__ == '__main__':
    main ()
