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

# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev

class DoublyLinkedListNode (object):
    def __init__ (self, data = None, prev_node = None, next_node = None):
        self.data = data
        self.prev = prev_node
        self.next = next_node
        self.head = self
    def print_doubly_linked_list (self):
        print (self.data, end = " ")
        if self.next: self.next.print_doubly_linked_list ()
    def insert_node (self, item):
        if self.data == None:
            self.data = item; self.next = None
        else:
            temp = self
            while temp.next: temp = temp.next
            temp.next = DoublyLinkedListNode (item, temp)
        return self
    def sorted_insert (self, item):
        resL = self; prev = None
        while resL and resL.data:
            if item <= resL.data:
                new = DoublyLinkedListNode (item, resL.prev, resL)
                if resL.prev: resL.prev.next = new
                else: self = new
                resL.prev = new
                return self
            prev = resL
            resL = resL.next
        new = DoublyLinkedListNode (item, prev)
        if prev: prev.next = new
        else: self = new
        return self

def sortedInsert (llist, item):
    return llist.sorted_insert (item)

def main ():
    #fptr = open (environ['OUTPUT_PATH'], 'w')
    tests = int (input ())
    for _ in range (tests):
        llist_count = int (input ())
        llist = DoublyLinkedListNode ()
        for _ in range (llist_count):
            llist.insert_node (int (input ()))
        data = int (input ())
        resultL = sortedInsert (llist, data)
        resultL.print_doubly_linked_list ()

if __name__ == '__main__':
    main ()
