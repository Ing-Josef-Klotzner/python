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

  
# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def check_binary_search_tree_ (root):
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    return isBST (root, INT_MIN, INT_MAX)

# Return true if the given tree is a BST and its values
# >= mini and <= maxi
def isBST (node, mini, maxi):
    # An empty tree is BST
    if node is None: return True
    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi: return False
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBST (node.left, mini, node.data - 1) and
          isBST (node.right, node.data + 1, maxi))

def main ():
    # Driver program to test above function 
    INT_MAX = 2147483647
    INT_MIN = -2147483648
    root = Node (4)
    root.left = Node (2)
    root.right = Node (5)
    root.left.left = Node (1)
    root.left.right = Node (3)
      
    if (isBST (root, INT_MIN, INT_MAX)):
        print ("Is BST")
    else:
        print ("Not a BST")
  
if __name__ == '__main__':
    main ()

