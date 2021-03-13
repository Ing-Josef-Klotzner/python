#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPeople function below.
def maximumPeople(cities,clouds):
    cities=sorted(cities)
    res=0
    for i in range(len(clouds)):
        a=search_lower(cities,clouds[i][0])
        b=search_upper(cities,clouds[i][1])
        for j in range(a,b):
            cities[j][2]+=1
            cities[j][3].append(i)
    for i in range(len(cities)):
        if cities[i][2]==1:
            clouds[cities[i][3]][2]+=cities[i][1]
        elif cities[i][2]==0:
            res+=cities[i][1]
    pop=max(clouds,key=lambda x:x[2])
    return pop[2]+res
 # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
def search_upper(seq, limit):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if m == (len(seq) -1) or (seq[m][0] <= limit and seq[m+1][0] > limit):
            return m
        elif seq[m][0] < limit:
            min = m+1
        else:
            max = m - 1

def search_lower(seq, limit):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if m == 0 or (seq[m][0] >= limit and seq[m-1][0] < limit):
            return m
        elif seq[m][0] < limit:
            min = m+1
        else:
            max = m - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))
    cities=[[xi,pi,0,[]] for xi,pi in zip(x,p)]
    m = int(input())
    y = list(map(int, input().rstrip().split()))
    r = list(map(int, input().rstrip().split()))
    clouds=[[yi-ri,yi+ri,0] for yi,ri in zip(y,r)]
    result = maximumPeople(cities, clouds)
    fptr.write(str(result) + '\n')
    fptr.close()
