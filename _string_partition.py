#!/bin/python3
from os import environ

# Partition set `S` into two subsets, `S1` and `S2`, such that the
# difference between the sum of elements in `S1` and the sum
# of elements in `S2` is minimized
def minPartition(S, total):
    # Create a boolean table to store solutions to subproblems
    T = [[False] * (total + 1) for _ in range(len(S) + 1)]
    # Fill the lookup table in a bottom-up manner
    for i in range(len(S) + 1):
        # elements with zero-sum are always true
        T[i][0] = True
        j = 1
        while i > 0 and j <= total:
            # exclude the i'th element
            T[i][j] = T[i - 1][j]
            # include the i'th element
            if S[i - 1] <= j:
                T[i][j] |= T[i - 1][j - S[i - 1]]
            j = j + 1
    # Find the maximum value of `j` between 0 and `sum/2` for which the
    # last row is true
    j = total // 2
    while j >= 0 and not T[len(S)][j]:
        j = j - 1
    print (total, j)
    return total - 2*j

def indianJob (n, g, a):
    # n -- count of robbers    g -- time guard enters
    if max (a) > g: return "NO"
    s = sum (a)
    if s < g: return "YES"
    if s > 2 * g: return "NO"
    mindiff = minPartition (a, s)
    print ("s", s, "mindiff", mindiff, "s + mindiff", s + mindiff, "2 * g", 2 * g, s + mindiff > 2 * g)
    if s + mindiff > 2 * g: return "NO" + str (2 * g)
    return "YES"

if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for t_itr in range (t):
        ng = input ().split ()
        n = int (ng [0])
        g = int (ng [1])
        arr = list (map (int, input ().rstrip ().split ()))
        result = indianJob (n, g, arr)
        fptr.write (result + '\n')
    fptr.close ()
