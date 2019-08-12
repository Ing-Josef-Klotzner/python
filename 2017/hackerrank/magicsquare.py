#!/usr/bin/python3
import math
import os
import random
import re
import sys
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    pre = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        ]
    totals = []
    for p in pre:
        total = 0
        for p_row, s_row in zip(p, s):
            for i, j in zip(p_row, s_row):
                if not i == j:
                    total += max([i, j]) - min([i, j])
        totals.append(total)
    return min(totals)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
#    fptr.write(str(result) + '\n')
#    fptr.close()
    print(result)
    for a in os.environ:
        print('Var: ', a, 'Value: ', os.getenv(a))
#We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

#You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

#Note: The resulting magic square must contain distinct integers in the inclusive range .

#For example, we start with the following matrix :

#5 3 4
#1 5 8
#6 4 2
#We can convert it to the following magic square:

#8 3 4
#1 5 9
#6 7 2
#This took three replacements at a cost of .

#Input Format

#Each of the lines contains three space-separated integers of row .

#Constraints

#Output Format

#Print an integer denoting the minimum cost of turning matrix  into a magic square.

#Sample Input 0

#4 9 2
#3 5 7
#8 1 5
#Sample Output 0

#1

#Sample Input 1

#4 8 2
#4 5 7
#6 1 6
#Sample Output 1

#4

#Medium
#Submitted 17375 times
#Max Score 20


