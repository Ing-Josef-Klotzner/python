#!/usr/bin/env python

import sys
import random


class my_randint:
    def __init__(self, seed):
        self.x=8071721
        self.y=3746545
        self.state=seed
    def __call__(self, a, b):
        self.state=(self.state+self.x)%self.y
        return(a+self.state%(b-a+1))
    
rint=my_randint(0)
T=50000
Pmax=50
Nmax=300
Mmax=9999999

print T

for t in range(T):
    P=rint(1,Pmax)
    N=rint(2*P,Nmax)
    M=rint(1,Mmax)
    print "{} {} {}".format(N,M,P)
    shot_height=list()
    for n in range(N):
        namelen=rint(0,20)
        name=chr(rint(ord('A'), ord('Z')))
        for l in range(namelen):
            name = name + chr(rint(ord('a'), ord('z')))
        perc=rint(0,100)
        height=rint(10000,24000)
        while [perc, height] in shot_height:
            perc=rint(0,100)
            height=rint(10000,24000)
        shot_height.append([perc, height])
        print "{} {} {}".format(name, perc, height)

