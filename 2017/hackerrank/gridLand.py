#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from sys import version_info
if version_info.major == 3:
    pass
elif version_info.major == 2:
    input = raw_input
else:
    print ("Unknown python version - input function not safe")

import os
from collections import deque
#from itertools import islice

def rotate (t):
    return t [1: ] + t [0]

def gridlandProvinces(n, s1, s2):
    s = set ()
    # überzählige blanks etc aus strings entfernen
    s1 = s1 [ : n]
    s2 = s2 [ : n]
    # in Uhrzeigersinn und gegen Uhrzeigersinn von allen 2 * n Startpositionen
    s_c = s1 + s2 [ : : -1]
    s_cw = s1 [ : : -1] + s2
    for i in range (2 * n):
        s.add (hash (s_c))
        s.add (hash (s_cw))
        s_c = rotate (s_c)
        s_cw = rotate (s_cw)

    s1r = s1 [::-1]
    s2r = s2 [::-1]
    
    # folgendes wiederholen mit getauschten Texten und alles nochmal mit invertierten Texten
    # Wechsel: von Position x des s1 zu x, dann x + 1 des s2 oder umgekehrt
    # Erstmägliche Wechselposition (wp): Index 1; letztmögliche wp : Index n - 2
    # Für wp von 0 bis 2:  (später 2 bis n - 2)
    #   Für aw von 0  bis  (n - wp - 2) * 2, step 2 
    #       Verbinde alle Buchstaben am Weg zu Text t:
    #       Gehe in s1 reversed von n - wp -1  bis n
    #       Gehe in s2 von 0 bis wp + 2 (exclusive wegen range) (bis hier: init text)
    #       curr = s1; other = s2
    #       Für w von 1 bis aw:
    #         Gehe von wp + w - 1 nach wp + w + 1 in curr
    #         curr, other = other, curr
    #       Gehe in curr von wp + w nach n - 1
    #       Gehe in other reverse von n - 1 bis wp + w + 1
    #       wenn t nicht in set s, add
    #       speichere ident text für odd/even wp ab t pos wp * 2 -/+ 1
    # für wp von 2 bis n - 2: 
    #   Für aw von 0  bis  (n - wp - 2) * 2, step 2
    #       Verbinde init text den ident text

    def mkzigzagDq (offset, s1, s2):
        s1 = deque (s1); s2 = deque (s2)
        result = deque ()
        s2.popleft ()
        for i in range (offset):
            s1.popleft (); s2.popleft ()
        for i in range (0, n - 3, 2):
            if len (s1) > 1:
                result.append (s1.popleft ()); result.append (s1.popleft ())
            if len (s2) > 1:
                result.append (s2.popleft ()); result.append (s2.popleft ())
        return "".join (result)

    def mkzigzag (offset, s1, s2):
        result = ""
        for i in range (offset, n - 3 + offset, 2):
            result += s1 [i: i + 2] + s2 [i + 1: i + 3]
        return result
    
    for s1_, s2_ in ((s1, s2), (s2, s1), (s1r, s2r), (s2r, s1r)):
        # zig zag Text ist gleich je string, alle 2 wp - nur unterschiedlich weit
        # es gibt 2 Muster (zigzag1 und zigzag2)
        zigzag1 = mkzigzag (1, s1_, s2_)
        zigzag2 = mkzigzag (2, s1_, s2_)
        s1r_ = s1_ [::-1]; s2r_ = s2_ [::-1]
        if n > 2: init = 2 
        else: init = 0
        ident0 = deque (); ident1 = deque ()
        for wp in range (init):
            # init text ist gleich je Wechselposition
            t_init = s1r_ [ n - wp - 1: n]
            t_init += s2_ [ : wp + 2]
            curr = s2_; other = s1_; curr_r = s2r_; other_r = s1r_
            for aw in range (0, (n - wp - 2) * 2, 2):
                t = t_init
                if aw:
                    if not wp % 2: t += zigzag1 [: aw]
                    else: t += zigzag2 [ : aw]
                curr, other = other, curr
                curr_r, other_r = other_r, curr_r
                wp_ = wp + aw // 2 + 2
                t += curr [wp_ - 1: n]
                t += other_r [ : n - wp_]
                if wp % 2: ident1.append (t [wp * 2 - 1 : ])
                else: ident0.append (t [wp * 2 + 1 : ])
                #print (wp, aw, t)
                s.add (hash (t))
            if not wp % 2: zigzag1 = zigzag1 [4: ]
            else: zigzag2 = zigzag2 [4: ]
        ident0.append (""); ident1.append("")
        offset = 2
        for wp in range (2, n - 2):
            # init text ist gleich je Wechselposition
            t_init = s1r_ [ n - wp - 1: n]
            t_init += s2_ [ : wp]
            for aw in range (0, (n - wp - 2) * 2, 2):
                t = t_init
                ix = aw // 2 + offset
                if wp % 2: t += ident1 [ix] [wp * 2: ]
                else: t += ident0 [ix] [wp * 2: ]
                #print (wp, aw, ix, t)
                s.add (hash (t))
            if wp % 2:
                offset += 2
    return len (s)

def main ():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p = int(input())
    for p_itr in range(p):
        n = int(input())
        s1 = input()
        s2 = input()
        result = gridlandProvinces(n, s1, s2)
        fptr.write(str(result) + '\n')
        print (result)
    fptr.close()

if __name__ == '__main__':
    main ()
