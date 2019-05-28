#!/usr/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
# too slow for big numbers
#    sm = 0
#    xl = []
#    for x in range(0, n, 5):
#        sm += x
#        xl.append(x)
#    for y in range(0, n, 3):
#        if y not in xl:
#            sm += y
#    print(sm)
    bigst3 = 3 * ((n - 1) // 3)
    sumOf3 = (3 + bigst3) * bigst3 // 6
    bigst5 = 5 * ((n - 1) // 5)
    sumOf5 = (5 + bigst5) * bigst5 // 10
    bigst15 = 15 * ((n - 1) // 15)
    sumOf15 = (15 + bigst15) * bigst15 // 30
    sm = sumOf3 + sumOf5 - sumOf15
    print(int(sm))
    
#        3,5,6,9,10,12,15,18,20,21,24,25,27,30
#        3   3 3    3  3  3     3  3     3  3    165       +        (3+30)/2*10                   +
#          5     5     5     5        5     5    105 - 45  = 225    (5+30)/2*6   -  1*3*5+2*3*5   = 225
#     

#    Sample Input 0

#    2
#    10
#    100
#    Sample Output 0

#    23
#    2318
