#!/usr/bin/python3
# -*- coding: utf-8 -*-
def sol():
    N, A, B = map(int, input().strip().split())
    S = input().strip()
    res = [0]*N
    res[0] = A
    maxl = 0
    for i in range(1,N):
        minv = res[i-1] + A
        cp, idx, newl = False, i, 0
        for k in range(maxl,-1,-1):
            if S[i-k:i+1] in S[0:i-k]:
                cp, idx, newl = True, i-k, k+1
                break
        if cp: minv = min(minv, res[idx-1]+B)
        maxl = newl
        res[i] = minv
    print (res[-1])
T = int(input().strip())
for x in range(T):
    sol()
