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

def preOrder (root):
    if root:
        print (root.info, end = " ")
        preOrder (root.left)
        preOrder (root.right)

def main ():
    tree = BinarySearchTree ()
    t = int (input ())
    arr = list (map (int, input ().split ()))
    for i in range (t):
        tree.create (arr [i])
    tree.preOrder (tree.root)
    #preOrder (tree.root)

if __name__ == '__main__':
    main ()
