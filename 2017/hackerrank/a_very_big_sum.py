#!/usr/bin/python3

#
# Complete the aVeryBigSum function below.
#
def aVeryBigSum(n, ar):
    return sum(ar)

def main ():
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(n, ar)
    print (result)

if __name__ == '__main__':
    main ()

# test input:
# 5
# 100000000001 100000000002 100000000003 100000000004 100000000005
