#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
"""
Created on Thu Aug 17 02:08:21 2017

@author: josef
"""

class node:
    def __init__(self, dat):
        self.dat = dat
        self.left = 0
        self.right = 0
		

def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.dat
        for x in inorder(t.right):
            yield x


if __name__ == '__main__':
    h = node(50)
    h.left = node(40) ; h.right = node(60)
    h.left.right = node(45); h.right.left = node(55)

    for x in inorder(h):
        print (x, end=" ")
    print()
