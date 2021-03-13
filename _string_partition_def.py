def minPartition (S, n, S1 = 0, S2 = 0, lookup = {}):
    # Base case: if the list becomes empty, return the absolute
    # difference between both sets
    if n < 0: return abs (S1 - S2)
    # Construct a unique key from dynamic elements of the input.
    # Note that we can uniquely identify the subproblem with `n` and `S1` only,
    # as `S2` is nothing but `S-S1`, where `S` is the sum of all elements
    key = (n, S1)
    # If the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
        # Case 1. Include the current item in subset `S1` and recur
        # for the remaining items `n-1`
        inc = minPartition (S, n - 1, S1 + S [n], S2, lookup)
        # Case 2. Exclude the current item from subset `S1` and recur for
        # the remaining items `n-1`
        exc = minPartition (S, n - 1, S1, S2 + S [n], lookup)
        lookup [key] = min (inc, exc)
    return lookup [key]
S = [33,70,5,40,26,24,64,63,49,53,23,26,51,54,41,95,13,10,90,79,10,59,29,39,30,91,74,38,93,69,31,38,29,57,94,60,99,19,97,30,85,99,41,20,69,25,32,87,48,86,89,67,96,18,0,88,24,33,93,80,5,43,73,21,98,80,2,83,71,10,62,80,80]
n = 73
print (minPartition (S, n - 1))
