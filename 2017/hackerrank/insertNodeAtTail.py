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
    def insert_node (self, item):
        if self.head == None: 
            self.head = SinglyLinkedListNode (item) 
            return self.head
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = SinglyLinkedListNode (item)
        return self.head

def printLinkedList (head):
    if head is not None:
        print (head.data)
        printLinkedList (head.next)

def insertNodeAtTail(head, data):
    if head == None: 
        head = SinglyLinkedListNode (data) 
        return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = SinglyLinkedListNode (data)
    return head

def main ():
    #fptr = open (environ['OUTPUT_PATH'], 'w')
    llist_count = int (input())
    llist = SinglyLinkedListNode ()
    for i in range (llist_count):
        llist_item = int (input())
        llist_head = insertNodeAtTail (llist.head, llist_item)
        llist.head = llist_head
    printLinkedList (llist.head)

if __name__ == '__main__':
    main ()
