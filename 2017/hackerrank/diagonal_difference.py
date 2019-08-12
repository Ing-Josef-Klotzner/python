#!/usr/bin/python3

import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(n, a):
    diag1 = 0
    diag2 = 0
    for j in range (n):
            diag1 += a[j][j]
            diag2 += a[j][n-j-1]
    return abs(diag1 - diag2)

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(n, a)
    print(result)
    
# Sample Input

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output

# 15
