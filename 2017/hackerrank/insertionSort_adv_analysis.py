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
from collections import deque
from sys import stdin
#from sys import setrecursionlimit
#setrecursionlimit (11000)

def insertionSortAna (n, l):
    # fastest - modified merge sort
    # Function to Use Inversion Count. number inversion = number shifts
    def inversionsCount (x):
        global count
        ln = len (x)
        midsection = ln // 2
        leftArray = x [: midsection]
        rightArray = x [midsection :]
        if ln > 1:  # Divide and conquer 
            inversionsCount (leftArray)
            inversionsCount (rightArray)
            # Merge, keep count of split inversions
            i, j = 0, 0
            a = leftArray; b = rightArray
            la = len (a); lb = len (b)
            for k in range (la + lb):
                ai = a [i]
                bj = b [j]
                if ai <= bj:
                    x [k] = ai
                    i += 1
                    if i == la:
                        while j != lb:
                            k += 1
                            x [k] = b [j]
                            j += 1
                        break
                else:
                    x [k] = bj
                    count += (la - i)
                    j += 1
                    if j == lb:
                        while i != la:
                            k += 1
                            x [k] = a [i]
                            i += 1                    
                        break   
        return count
    global count
    count = 0
    return inversionsCount (l)

    # slower - binary indexed tree (BIT) used
    # Python3 program to count inversions using Binary indexed tree
    # Returns sum of arr[0..index]. This function assumes that the
    # array is preprocessed and partial sums are stored in BITree [] 
    def getSum (BITree, index): 
        sum = 0 # Initialize result
        # Traverse ancestors of BITree[index]  
        while (index > 0):  
            sum += BITree [index]  
            index -= index & (-index)  
        return sum
    def updateBIT (BITree, m, index, val):
        # Traverse all ancestors and add 'val'  
        while (index <= m):  
            BITree [index] += val  
            index += index & (-index)  
    # Returns count of inversions of size three  
    def getInvCount (arr, n): 
        invcount = 0 # Initialize result  
        # Find maximum element in arrays  
        maxElement = max (arr) 
        # Create a BIT with size equal to maxElement+1
        BIT = [0] * (maxElement + 1)  
        for i in range(n - 1, -1, -1): 
            v = arr [i]
            invcount += getSum (BIT, v)  
            updateBIT (BIT, maxElement, v, 1)  
        return invcount  
    return getInvCount (l, n)

    # slowest - BIT as class
    class BIT: # binary indexed tree
        def __init__(self, n):
            n += 1
            self.size = n
            self.data = [0] * n
        def query(self, i):
            s = 0
            while i > 0:
                s += self.data[i]
                i -= i & -i
            return s
        def add(self, i, x):
            while i < self.size:
                self.data[i] += x
                i += i & -i 
                
    def count_inversion(n, ls):
        """
            Count inversions in a sequence of numbers
        """
        cnt = 0
        m = max (ls)
        tree = BIT(m)
        for i in range (n - 1, -1, -1):
            v = ls [i]
            cnt += tree.query (v)
            tree.add(v, 1)
       
        return cnt
    return count_inversion (n, l)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        n = int (input ())
        arr = list (map (int, input ().rstrip ().split ()))
        result = insertionSortAna (n, arr)
        fptr.write (str (result) + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
