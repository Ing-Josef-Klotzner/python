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
2
1
1
0
3
3
2
1
2
out:
1
3
"""

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedListNode (object):
    def __init__ (self, data = None, next_node = None):
        self.data = data
        self.next = next_node
        self.head = self
    def print_linkedList (self):
        print (self.data, end = " ")
        if self.next:
            self.next.print_linkedList ()
    def insert_node (self, item):
        if self.data == None:
            self.data = item; self.next = None
        else:
            temp = self
            while temp.next: temp = temp.next
            temp.next = SinglyLinkedListNode (item)
        return self
    def insert_node_at_head (self, item):
        if self.data == None: self = SinglyLinkedListNode (item)
        else: self = SinglyLinkedListNode (item, self)
        return self
    def insert_node_at (self, item, pos):
        x = 0
        temp = self
        while temp != None and x < pos:
            prev = temp
            temp = temp.next
            x += 1
        # temp is NodeAtPos
        new = SinglyLinkedListNode (item, temp)
        if pos > 0: prev.next = new
        else: self = new
        return self
    def delete_node (self, node, pos):
        if pos == 0: return node.next
        node.next = self.delete_node (node.next, pos - 1)
        return node
    def rev_print_linkedL (self):
        if self and self.next:
            self.next.rev_print_linkedL ()
        print (self.data)
    def reverse_list (self):   # recursive solution
        if not self or not self.next:
            return self
        nxt = self.next.reverse_list ()
        self.next.next = self
        self.next = None
        return nxt
    def reverse_list_iterative (self):
        prev = None
        while self:
            prev = SinglyLinkedListNode (self.data, prev)
            self = self.next
        return prev
    def merge_lists (self, other):
        temp = self
        if self.data <= other.data:
            temp = temp_head = self; self = self.next
        else: temp = temp_head = other; other = other.next
        while self and other:
            if self.data <= other.data:
                temp.next = self; temp = temp.next; self = self.next
            else: temp.next = other; temp = temp.next; other = other.next
        if not self and other: temp.next = other
        elif self and not other: temp.next = self
        return temp_head
    def get_node (self, pos):
        res = cur = self; x = 0
        while cur.next:
            x += 1
            cur = cur.next
            if x > pos: res = res.next
        return res.data

def getNode (llist, pos):
    return llist.get_node (pos)

def main ():
    #fptr = open (environ['OUTPUT_PATH'], 'w')
    tests = int (input ())
    for _ in range (tests):
        llist_count = int (input())
        llist = SinglyLinkedListNode ()
        for i in range (llist_count):
            llist.insert_node (int (input ()))
        pos = int (input ())
        result = getNode (llist, pos)
        print (result)

if __name__ == '__main__':
    main ()
