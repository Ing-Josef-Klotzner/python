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
5
383
484
392
975
321
out:
383
484
392
975
321
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
        print (self.data)
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

def insertNodeAtTail (llist, data):
    return llist.insert_node (data)

def main ():
    #fptr = open (environ['OUTPUT_PATH'], 'w')
    llist_count = int (input())
    llist = SinglyLinkedListNode ()
    for i in range (llist_count):
        llist_item = int (input())
        llist = insertNodeAtTail (llist, llist_item)
    llist.print_linkedList ()

if __name__ == '__main__':
    main ()
