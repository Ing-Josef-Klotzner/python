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
#from time import sleep   #time
#from sys import exit  #, maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
"""

class Node:
    def __init__ (self, d): self.data = d
    
def build_tree (indexes):
    f = lambda x: None if x == -1 else Node (x)
    children = [list (map (f,x)) for x in indexes]
    nodes = {n.data: n for n in filter (None, sum (children, []))}
    nodes [1] = Node (1)
    for idx, child_pair in enumerate (children):
        nodes [idx + 1].left = child_pair [0]
        nodes [idx + 1].right = child_pair [1]
    return nodes [1]

def inorder (root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append (curr)
            curr = curr.left
        elif stack:
            curr = stack.pop ()
            yield curr.data
            curr = curr.right
        
def swapNodes (indexes, queries):
    root = build_tree (indexes)
    for k in queries:
        h = 1
        q = deque ([root])
        while q:
            for _ in range (len (q)):
                node = q.popleft ()
                if not h % k: node.left, node.right = node.right, node.left
                q += filter (None, (node.left, node.right))
            h += 1
        yield inorder (root)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    indexes = []
    for _ in range (n):
        indexes.append (list (map (int, input ().rstrip ().split ())))
    queries_count = int (input ())
    queries = []
    for _ in range (queries_count):
        queries.append (int (input ()))
    result = swapNodes (indexes, queries)
    fptr.write ('\n'.join ([' '.join (map (str, x)) for x in result]))
    fptr.write ('\n')
    fptr.close ()

if __name__ == '__main__':
    main ()