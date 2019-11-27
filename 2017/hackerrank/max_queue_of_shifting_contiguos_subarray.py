#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Python program to find the maximum for each
# and every contiguous subarray of size k

from collections import deque

# A Deque (Double ended queue) based method for printing 
# maximum element of all subarrays of size k
def printMax (arr, n, k):
    """ Create a Double Ended Queue, Qi that will store indexes
    of array elements. The queue will store indexes of largest
    elements in every window and it will maintain decreasing
    order of values from front to rear in Qi, i.e.
    arr [Qi.front ()] to arr [Qi.rear ()] are in decreasing order"""
    Qi = deque ()
    # Process first k (or first window) elements of array
    for i in range (k):
        # Remove all elements smaller than current element to add
        while Qi and arr [i] >= arr [Qi [-1]]: Qi.pop ()
        # Add new element at rear of queue
        Qi.append (i)
    # Process rest of the elements, i.e. from arr [k] to arr [n-1]
    for i in range (k, n):
        # front queue element is largest of previous window → print it
        print (str (arr [Qi [0]]) + " ", end = "")
        # Remove the elements which are out of current window
        while Qi and Qi [0] <= i - k: Qi.popleft ()
        # Remove all elements smaller than current element to add
        while Qi and arr [i] >= arr [Qi [-1]]: Qi.pop ()
        # Add current element at the rear of Qi
        Qi.append (i)
    # Print the maximum element of last window
    print (str (arr [Qi [0]]))
    
# Driver programm to test above fumctions
def main ():
    arr = [12, 1, 78, 90, 57, 89, 56]
    k = 3
    printMax (arr, len (arr), k)
if __name__ == "__main__":
    main ()    
# This code is contributed by Shiv Shankar

