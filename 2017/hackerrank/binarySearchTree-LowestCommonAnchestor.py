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
#from collections import deque   #defaultdict
#from time import sleep   #time
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
"""
class Node:
    def __init__ (self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 
    def __str__ (self):
        return str (self.info) 

class BinarySearchTree:
    def __init__ (self): self.root = None
    def create (self, val):  
        if self.root == None: self.root = Node (val)
        else: 
            current = self.root
            while True:
                if val < current.info:
                    if current.left: current = current.left
                    else: current.left = Node (val); break
                elif val > current.info:
                    if current.right: current = current.right
                    else: current.right = Node (val); break
                else: break

def lca (root, v1, v2):
    while True:
        if root.info > v1 and root.info > v2: root = root.left
        elif root.info < v1 and root.info < v2: root = root.right
        else: return root

def main ():
    tree = BinarySearchTree ()
    t = int (input ())
    arr = list (map (int, input ().split()))
    for i in range (t):
        tree.create (arr [i])
    v = list (map (int, input ().split()))
    ans = lca (tree.root, v [0], v [1])
    print (ans.info)

if __name__ == '__main__':
    main ()
