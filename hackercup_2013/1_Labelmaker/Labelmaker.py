#! /usr/bin/env python2
# -*- coding: iso-8859-15 -*-
import re
i_file_line_ct=0
fobj = open("labelmaker_example_input.txt", "r") 
fobj2 = open("Labelmaker_output.txt", "w")
#def rotate(l, x):
#    return l[-x % len(l):] + l[:-x % len(l)]
for line in fobj:   # line is a string
    line_list = re.findall(r'\w+',line)  # converts string line to list line_list
    i_file_line_ct += 1
    #is_nmbr = line_list[0].isdigit()   # true if first tuple is number
    if i_file_line_ct == 1:
        T=line    # line 1 of input file helds count of test cases
        T_c=1
    if i_file_line_ct>1:
        # Each test case consists of the string L and the integer N, separated by a space
        # 1 <= T <= 20   1 <= N <= 263-1   1 <= length(L) <= 25 
        # L will be in alphabetical order, consist of only uppercase letters A-Z, and contain each letter at most once 
        L = line_list[0]
        N = int(line_list[1])
        x = len(L)
        Res = ""
        print L,N,x;
        Rest = N
        # get digit_count
        dcc=N
        dc=1   # count of digits
        while dcc > x:
            dcc /= x
#            print dcc
            dc += 1
        digit = pow(x,dc)
        # subtract x¹,x²,...x^dc
        x_c = dc-1
        while x_c > 0:
            Rest-=pow(x,x_c)
            x_c -=1
        x_c = dc-1
        while x_c >= 0:
            digit = pow(x,x_c)
            Index = Rest / digit
            Rest -= Index * digit# reduce by
            if Rest % digit:
                Index += 1
            Res +=str(L[Index-1])
            x_c -= 1
        print >> fobj2,"Case #"+str(T_c)+": "+str(Res)
        print "Case #"+str(T_c)+": "+str(Res)
        T_c += 1
    elif i_file_line_ct <> 1 and (T < 1 or T > 30):
        print ("invalid count of Testcases ")
        size_out_of_range=1

fobj.close()
fobj2.close()
print
print ("count of testcases: "+T)
