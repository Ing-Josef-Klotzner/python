#!/usr/bin/python3
from __future__ import absolute_import, division, print_function
# there are 137 loosing and 3139 winning states in chomp 3/25

n,m = 3,25
init = frozenset((x,y) for x in range(n) for y in range(m))

# conversion from (row1,row2,row3) board into y,x board
def bd(a,b,c):
    e = frozenset((0,x) for x in range(a))
    f = frozenset((1,x) for x in range(b))
    g = frozenset((2,x) for x in range(c))
    return e | f | g
    
def memoize(f):
    cache = dict()
    def memof(x):
        try: return cache[x]
        except:
            cache[x] = f(x)
            return cache[x]
    return memof

def moves(board):
    return [frozenset([(y,x) for (y,x) in board if y < py or x < px]) for (py,px) in board]

@memoize
def wins(board):
    if not board: return True
    return any(not wins(move) for move in moves(board))

def show_moves(board):
    for move in moves(board):
        show(move)
        print()

def show(board):
    for y in range(n-1,-1,-1):
        print (str(y + 1) + '|' + ''.join('x ' if (y,x) in board else '  ' for x in range(m)))

if __name__ == '__main__':
    (a, b, c) = input("board please: (int for row1, int for row2, int for row3)")

#    l = []
#    for a in range (0,26):
#        for b in range (0,a+1):
#            for c in range(0,b+1):
#                brd = bd(a,b,c)
#                if not wins(brd):
#                    l.append((a,b,c))
#    print(l)
#    print("printed all LOSE states of chomp 3/25")

    brd = bd(a,b,c)

    show(brd)

    print("".join("WIN" if wins(brd) else "LOSE"))

    show_moves(brd)

#all LOSE states:
#[(1, 0, 0), (2, 1, 0), (2, 2, 1), (3, 1, 1), (3, 2, 0), (4, 2, 2), (4, 3, 0), (5, 3, 2), (5, 4, 0), (5, 5, 3), (6, 3, 3), (6, 4, 2), (6, 5, 0), (7, 4, 3), (7, 5, 2), (7, 6, 0), (7, 7, 4), (8, 4, 4), (8, 6, 2), (8, 7, 0), (9, 5, 4), (9, 6, 5), (9, 7, 2), (9, 8, 0), (9, 9, 6), (10, 5, 5), (10, 6, 4), (10, 8, 2), (10, 9, 0), (11, 6, 6), (11, 7, 5), (11, 9, 2), (11, 10, 0), (12, 7, 6), (12, 8, 5), (12, 9, 7), (12, 10, 2), (12, 11, 0), (12, 12, 8), (13, 7, 7), (13, 8, 6), (13, 9, 5), (13, 11, 2), (13, 12, 0), (14, 8, 7), (14, 9, 8), (14, 10, 5), (14, 11, 9), (14, 12, 2), (14, 13, 0), (14, 14, 10), (15, 8, 8), (15, 10, 7), (15, 11, 5), (15, 13, 2), (15, 14, 0), (16, 9, 9), (16, 10, 8), (16, 11, 7), (16, 12, 5), (16, 14, 2), (16, 15, 0), (17, 10, 9), (17, 11, 8), (17, 12, 7), (17, 13, 5), (17, 14, 11), (17, 15, 2), (17, 16, 0), (17, 17, 12), (18, 10, 10), (18, 12, 9), (18, 13, 7), (18, 14, 5), (18, 16, 2), (18, 17, 0), (19, 11, 10), (19, 12, 11), (19, 13, 9), (19, 14, 7), (19, 15, 5), (19, 16, 12), (19, 17, 2), (19, 18, 0), (19, 19, 13), (20, 11, 11), (20, 12, 10), (20, 14, 9), (20, 15, 7), (20, 16, 5), (20, 18, 2), (20, 19, 0), (21, 12, 12), (21, 13, 10), (21, 15, 9), (21, 16, 7), (21, 17, 5), (21, 18, 11), (21, 19, 2), (21, 20, 0), (22, 13, 11), (22, 14, 12), (22, 15, 13), (22, 16, 9), (22, 17, 7), (22, 18, 5), (22, 19, 14), (22, 20, 2), (22, 21, 0), (22, 22, 15), (23, 13, 12), (23, 14, 13), (23, 15, 11), (23, 16, 14), (23, 17, 9), (23, 18, 7), (23, 19, 5), (23, 20, 15), (23, 21, 2), (23, 22, 0), (23, 23, 16), (24, 13, 13), (24, 15, 12), (24, 16, 11), (24, 18, 9), (24, 19, 7), (24, 20, 5), (24, 22, 2), (24, 23, 0), (25, 14, 14), (25, 16, 13), (25, 17, 11), (25, 19, 9), (25, 20, 7), (25, 21, 5), (25, 23, 2), (25, 24, 0)]
