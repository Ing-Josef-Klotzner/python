#!/usr/bin/python3

if __name__ == '__main__':
    n = int (input ())
    lst = []
    gradeS = set ([])
    for st in range (n):
        student = input ()
        grade = float (input ())
        gradeS.add (grade)
        lst += [(grade, student)]
    gradeX = (sorted (list (gradeS))) [1]
    result = filter (lambda x: gradeX in x, (sorted (lst)))
    for res in result:
        print (res [1])
