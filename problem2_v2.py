#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys
import argparse
import re
import operator

debugflag=False
def debug(key, value=None):
    if (debugflag):
        if (value):
            sys.stderr.write("*DBG* {!s}: {!s}\n".format(key, value))
        else:
            sys.stderr.write("*DBG* {!s}\n".format(key))

class player:
    def __init__(self, name, shot_p, height):
        self.name=name
        self.shot_p=shot_p
        self.height=height

    def __lt__(self, player_b):
        if (self.shot_p > player_b.shot_p):
            return(True)
        if ((self.shot_p == player_b.shot_p) and (self.height > player_b.height)):
            return(True)
        else:
            return(False)

    def __str__(self):
        return("player({}, {}, {})".format(self.name, self.shot_p, self.height))

    def __repr__(self):
        return(str(self))

class problem:
    def __init__(self, i):
        self.i=i

class solver:
    def __init__(self, debug=False):
        global debugflag

        debugflag=debug

        # Init
        pass
        # end Init

    def solve(self, pr):
        #debug("Problem Data", pr.players)
        
        # Solve problem
        pr.players.sort(reverse=True)

        team_a=pr.players[0::2]
        players_a=len(team_a)
        team_b=pr.players[1::2]
        players_b=len(team_b)

        team_a_bottom=team_a[0:-pr.P]
        team_a_bottom.sort()
        team_a=(team_a[-pr.P:]+team_a_bottom)*2

        team_b_bottom=team_b[0:-pr.P]
        team_b_bottom.sort()
        team_b=(team_b[-pr.P:]+team_b_bottom)*2

        solution=map(operator.attrgetter("name"), team_a[(pr.M%players_a):(pr.M%players_a)+pr.P]+team_b[(pr.M%players_b):(pr.M%players_b)+pr.P])
        solution.sort()
        # End solve

        return(solution)

    def solve2(self, pr):
#        debug("Problem Data", pr.data)
        
        # Solve problem Brute Force
        solution=[pr.data]
        # End solve

        return(solution)

class pparser:
    
    def __init__(self, pfile):
        self.pfile=pfile
        self.reader=csv.reader(pfile, delimiter=" ")

        row=self.reader.next()
        self.N=int(row[0])
        self.i=0

    def next(self):
        self.i+=1

        if (self.i > self.N):
            raise StopIteration()

        p=problem(self.i)        
        p.players=list()

        # Parse problem here
        row=self.reader.next()
        p.N=int(row[0])
        p.M=int(row[1])
        p.P=int(row[2])
        for i in range(p.N):
            row=self.reader.next()
            p.players.append(player(row[0], int(row[1]), int(row[2])))
        # End parse

        return(p)

    def __iter__(self):
        return(self)
        

def solve():
    parser=argparse.ArgumentParser("Solve the problem.")
    parser.add_argument("--debug", "-d", action="store_true")
    parser.add_argument("--test", "-t", action="store_true")
    parser.add_argument("file", type=file)
    
    opt=parser.parse_args()

    if (opt.test):
        opt.debug=True

    s=solver(opt.debug)
    pfile=opt.file

    pparse=pparser(pfile)

    outwriter=csv.writer(sys.stdout, delimiter=" ", quoting=csv.QUOTE_NONE, lineterminator='\n')
    for p in pparse:
        solution=s.solve(p)
        
        if (opt.test):
            solution2=s.solve2(p)
            if (solution2 != solution):
                debug("Differing Solution", [solution, solution2])

        outwriter.writerow(["Case", "#{:d}:".format(p.i)]+solution)
    
    pfile.close()


if (__name__ == "__main__"):
    solve()
