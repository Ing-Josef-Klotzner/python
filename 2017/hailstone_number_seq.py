#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
# Hailstone Number Sequence -  www.101computing.net/the-collatz-conjecture/

n = int(input("Type a positive whole number to start your hailstone sequence:"))
if n % 2 == 0:
    print("N IST GERADE")
#complete the code here...
def hailstone_r(nx):
    if nx == 1:
        return nx
    if nx % 2 == 0:
        return nx, hailstone_r(nx//2)
    else:
        return nx, hailstone_r(nx*3+1)

def hailstone_p(np):
    hail = list()
    while np > 1:
        if np % 2 == 0:
            hail.append(np)
            np = np // 2
        else:
            hail.append(np)
            np = np * 3 + 1
    hail.append(1)
    return hail
    
def hailstone_g(np):
    while np > 1:
        if np % 2 == 0:
            yield np
            np = np // 2
        else:
            yield np
            np = np * 3 + 1
    yield 1

print("Hailstone rekursiv: ")
print(hailstone_r(n))

print("Hailstone progressiv: ")
print(hailstone_p(n))

print("Hailstone als Generator: ")
for i in (hailstone_g(n)):
    print (i, end=" ")
print()
