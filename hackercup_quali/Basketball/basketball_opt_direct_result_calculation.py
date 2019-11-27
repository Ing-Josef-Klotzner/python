#! /usr/bin/env python2
# -*- coding: iso-8859-15 -*-
from operator import itemgetter
import re
PT = 0  # playtime
i_file_line_ct=0
fobj = open("basketball_game_input.txt", "r") 
#fobj = open("testdata3-filtered.txt", "r") 
#fobj = open("testdata4.txt", "r") 
fobj2 = open("basketball_output.txt", "w")
def rotate(l, x):
    return l[-x % len(l):] + l[:-x % len(l)]
for line in fobj:   # line is a string
    line_list = re.findall(r'\w+',line)  # converts string line to list line_list
    line_list.append(PT)
    i_file_line_ct += 1
    is_nmbr = line_list[0].isdigit()   # true if first tuple is number
    if i_file_line_ct == 1:
        T=line    # line 1 of input file helds count of test cases
        T_c=1
    if i_file_line_ct>1 and is_nmbr:
        # N number of players  M minutes   P playercount playing
        # 1 <= T <= 50   2 * P <= N <= 30   1 <= M <= 120   1 <= P <= 5
        team=[];team_a=[];team_b=[]
        px = []
        PL = []
        PLS = ""
        N = int(line_list[0])
        NC = N
        M = int(line_list[1])
        P = int(line_list[2])
    elif i_file_line_ct <> 1 and (N < 1 or N > 30) and is_nmbr:
        print ("invalid count of N teamplayers "+N+" in line "+str(i_file_line_ct)+" of inputfile")
        size_out_of_range=1
    if not is_nmbr:
        # next N lines are in format "<name> <shot_percentage> <height>".
        line_list[1] = int(line_list[1])
        line_list[2] = int(line_list[2])
        team.append(line_list)
        NC -= 1
        if NC == 0:
#            print "calculation for team rotation takes place"
            BL = " "
            team.sort(key=itemgetter(1,2),reverse=True)   #pre-sort height  -- only if needed
            #team.sort(key=itemgetter(1),reverse=True)   #sort shot percentage
            team_a += team[0::2]
            team_b += team[1::2]
#            print M
            # leave away x times moving same cycle
            if N % 2:
                Ma = M % len(team_a)
                Mb = M % len(team_b)
            else:
                Ma = Mb = (M % N)
#            print M
#            print "team a",team_a; print "team b",team_b
            # create lists for team_bench and team_pl
            team_a_pl = team_a[0:P]
            team_b_pl = team_b[0:P]
            team_a_bench = team_a[P:len(team_a)]
            team_b_bench = team_b[P:len(team_b)]
            team_a_bench.sort(key=itemgetter(1,2),reverse=False)
            team_b_bench.sort(key=itemgetter(1,2),reverse=False)
            team_a_to_rotate = team_a_pl + team_a_bench
            team_b_to_rotate = team_b_pl + team_b_bench
            team_a_rotated = rotate(team_a_to_rotate,Ma)
            team_b_rotated = rotate(team_b_to_rotate,Mb)
            # now testcase is complete - write to output
            TC=0   # create team name list
#            print team_a_pl;print team_a_bench#;print team_b_pl;print team_b_bench
            while TC < P:
                PL.append(team_a_rotated[TC][0])
                PL.append(team_b_rotated[TC][0])
                TC += 1
            PL.sort()
            BLC = 0
            for px in PL:
                if BLC == len(PL)-1:
                    BL=""
                PLS += str(px) + BL
                BLC += 1
            print >> fobj2,"Case #"+str(T_c)+": "+str(PLS)
#            print "Case #"+str(T_c)+": "+str(PLS)
            T_c += 1
fobj.close()
fobj2.close()
print
print ("count of testcases: "+T)
