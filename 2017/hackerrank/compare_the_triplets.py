#!/usr/bin/python3

import os
import sys

#
# Complete the solve function below.
#
def solve(a0, a1, a2, b0, b1, b2):
    al = 0
    bob = 0
    if a0 > b0: al += 1
    if a1 > b1: al += 1
    if a2 > b2: al += 1
    if a0 < b0: bob += 1
    if a1 < b1: bob += 1
    if a2 < b2: bob += 1
    return str(al) + " " + str(bob)

if __name__ == '__main__':
#    f = open(os.environ['OUTPUT_PATH'], 'w')
    a0A1A2 = input().split()
    a0 = int(a0A1A2[0])
    a1 = int(a0A1A2[1])
    a2 = int(a0A1A2[2])
    b0B1B2 = input().split()
    b0 = int(b0B1B2[0])
    b1 = int(b0B1B2[1])
    b2 = int(b0B1B2[2])
    result = solve(a0, a1, a2, b0, b1, b2)
#    f.write(' '.join(map(str, result)))
#    f.write('\n')
#    f.close()
    print(result)
    


#Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

#We define the rating for Alice's challenge to be the triplet A, and the rating for Bob's challenge to be the triplet B.

#Your task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

#If a[i] > b[i], then Alice is awarded 1 point.
#If a[i] < b[i], then Bob is awarded 1 point.
#If a[i] = b[i], then neither person receives a point.
#Comparison points is the total points a person earned.

#Given A and B, can you compare the two challenges and print their respective comparison points?

#Input Format

#The first line contains  space-separated integers, , , and , describing the respective values in triplet . 
#The second line contains  space-separated integers, , , and , describing the respective values in triplet .

#Constraints
#1 <= a[i] <= 100
#1 <= b[i] <= 100
#Output Format

#Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

#Sample Input

#5 6 7
#3 6 10
#Sample Output

#1 1 
#Alice's comparison score is 1, and Bob's comparison score is 1. Thus, we print 1 1 (Alice's comparison score followed by Bob's comparison score) on a single line.


