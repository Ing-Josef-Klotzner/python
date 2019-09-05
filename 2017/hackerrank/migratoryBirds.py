#!/usr/bin/python3

from os import environ

# Complete the divisibleSumPairs function below.
def migratoryBirds (ar):
    birdTypeCount = [0,0,0,0,0,0]
    for birdType in ar:
        birdTypeCount [birdType] += 1
#    print (birdTypeCount)
    winCount = max (birdTypeCount)
    winType = 6
    for type_ in range (1, 5 + 1):
        count = birdTypeCount [type_]
        if count == winCount:
            if winType > type_:
                winType = type_
    return winType
 
if __name__ == '__main__':
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    arr_count = int (input ().strip ())
    arr = list (map (int, input ().rstrip ().split ()))
    result = migratoryBirds (arr)
    print (result)
    fptr.write (str (result) + '\n')
    fptr.close ()

