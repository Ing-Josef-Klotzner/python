#! /usr/bin/env python2
import re
i_file_line_ct=0
field_size_ct=1
square_size=0
last_line=""
fehler=0
match=0
fobj = open("square_detector.txt", "r") 
fobj2 = open("square_detector_output.txt", "w")
def containsAny(str, set):
    """Check whether 'str' contains ANY of the chars in 'set'"""
    return 1 in [c in str for c in set]
def is_number(strg):
    """ Check if not any '.' or '*' in str -> it is a number"""
    return not(containsAny(".", strg) or containsAny("#", strg))
for line in fobj:
    i_file_line_ct += 1
    is_nmbr = is_number(line)
    if i_file_line_ct == 1:
        T=line    # line 1 of input file helds count of test cases
        T_c=1
    if i_file_line_ct>1 and is_nmbr:
        field_size_ct=int(line)
        test_case_pattern=""
        match_line_ct=0
    elif i_file_line_ct <> 1 and (line < 1 or line > 20) and is_nmbr:
        print ("invalid count of fieldsize "+str(line)+" in line "+str(i_file_line_ct)+" of inputfile")
        size_out_of_range=1
    if not is_nmbr:
        match=re.search("#+",line,flags=0)
        if match:
            group=match.group(0)
#            print group
#            print match.groups()
            length=int(len(group))
            if square_size == 0:
                square_size=length
            if len(last_line)>0:
                if not (last_line == line) and square_size>1:
                    fehler=1
        else:
            group=""
            length=0
        if (length==square_size)and square_size>0:
            match_line_ct += 1
        last_line=line
        test_case_pattern=test_case_pattern+line
        field_size_ct = field_size_ct -1
        if field_size_ct == 0:
            # now testcasepattern of testcase is complete - check it for valid square
            print "Testcasepattern:\n"+test_case_pattern
            print match_line_ct
            print square_size
            if match_line_ct == square_size and not fehler:
                print >> fobj2,"Case #"+str(T_c)+": YES"
                print "Case #"+str(T_c)+": YES"
            else:
                print >> fobj2,"Case #"+str(T_c)+": NO"
                print "Case #"+str(T_c)+": NO"
            T_c += 1
            square_size=0
            fehler=0
            last_line=""
fobj.close()
fobj2.close()
print
print ("count of testcases: "+T)
