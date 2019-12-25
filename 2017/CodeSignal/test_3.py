#!/usr/bin/python3

def meanGroups (a):
    meanToGroup = [-1] * 101
    meanGroupsL = []
    groupCt = 0
    for i in range (len (a)):
        mean = sum (a [i]) // len (a [i])
        if meanToGroup [mean] == -1:
            meanToGroup [mean] = groupCt
            meanGroupsL.append ([groupCt])
            groupCt += 1
        else:
            meanGroupsL [meanToGroup [mean]].append (i)
    return meanGroupsL

def main ():
    a = [[3,3,4,2], [4,4], [4,0,3,3], [2,3], [3,3,3]]
    print (meanGroups (a))

if __name__ == '__main__':
    main ()

"""
Input:
a:
[[3,3,4,2], 
 [4,4], 
 [4,0,3,3], 
 [2,3], 
 [3,3,3]]
Output:
[[0], 
 [1], 
 [2,3], 
 [3]]
Expected Output:
[[0,4], 
 [1], 
 [2,3]]
"""
