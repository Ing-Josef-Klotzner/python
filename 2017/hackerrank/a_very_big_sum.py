#!/usr/bin/python3

import os
import sys

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    return sum(ar)

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(n, ar)
    print(result)

# test input:
# 5
# 100000000001 100000000002 100000000003 100000000004 100000000005
