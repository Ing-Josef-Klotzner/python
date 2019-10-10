#!/usr/bin/python3

from os import environ

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range (n - 1):
        for j in range (i + 1, n):
            if (ar [i] + ar [j]) % k == 0:
                res += 1
    return res
 
if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    nk = input ().split ()
    n = int (nk [0])
    k = int (nk [1])
    ar = list (map (int, input ().rstrip ().split ()))
    result = divisibleSumPairs (n, k, ar)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

