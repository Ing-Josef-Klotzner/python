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
        if s_c not in s:
            s.add (s_c)
        if s_cw not in s:
            s.add (s_cw)
        s_c = rotate (s_c)
        s_cw = rotate (s_cw)

    if n > 2: mxaw = n - 2
    else: mxaw = 0
    s1r = s1 [ : : -1]
    s2r = s2 [ : : -1]

    # folgendes wiederholen mit getauschten Texten und alles nochmal mit invertierten Texten
    # Wechsel: von Position x des s1 zu x, dann x + 1 des s2 oder umgekehrt
    # max Anzahl Wechsel (mxaw): n - 2 (0 für n <= 2)
    # Erstmägliche Wechselposition (wp): Index 1; letztmögliche wp (=mxaw): Index n - 2
    # Erstpositionen: wp - 1
    # Endposition: last wp + 1 (= wp + w + 1)
    # Für aw von 1  bis  mxaw + 1
    #     Für wp von 1 bis n - aw:
    #       Verbinde alle Buchstaben am Weg zu Text t:
    #       Gehe in s1 reverse von Erstposition nach 0 (wenn 0 dann 1 character)
    #       Gehe in s2 von 0 bis wp + 1 (exclusive wegen range)
    #       curr = s1; other = s2
    #       Für w von 1 bis aw:
    #         Gehe von wp + w - 1 nach wp + w + 1 in curr
    #         curr, other = other, curr
    #       Gehe in curr von wp + w nach n - 1
    #       Gehe in other reverse von n - 1 bis wp + w + 1
    #       wenn t nicht in set s, add

#    #funktioniert richtig, aber zu langsam    
#    for curr, other in ((s1, s2), (s2, s1), (s1r, s2r), (s2r, s1r)):
##        print (s1_, s2_)
##    s1_ = s1; s2_ = s2
#        for aw in range (1, mxaw + 1):
#    #        print ("Anzahl Wechsel:", aw)
#            for wp in range (1, n - aw):
#                t = curr [ : wp] [ : : -1]
#                t += other [ : wp + 1]
#                w = 0
#                for w in range (1, aw):
#                    wp_ = wp + w - 1
#                    t += curr [wp_: wp_ + 2]
#                    curr, other = other, curr
#                wp_ = wp + w
#                t += curr [wp_: n]
#                t += other [wp_ + 1 : n] [ : : -1]
#                if t not in s:
#    #                print (t)
#                    s.add (t)
#    return len (s)
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
        ident = dict ()
        for wp in range (init):
            # init text ist gleich je Wechselposition
            t_init = s1r_ [ n - wp - 1: n]
            t_init += s2_ [ : wp + 2]
            curr = s2_; other = s1_; curr_r = s2r_; other_r = s1r_
            ixbs = wp * 2 + wp % 2
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
                ix = ixbs + aw
                if ix > 3:
                    ident [ix] = (t [wp * 2 + 1 : ])
                #print (wp, aw, ix, t)
                if t not in s:
                    s.add (t)
            if not wp % 2: zigzag1 = zigzag1 [4: ]
            else: zigzag2 = zigzag2 [4: ]
        for wp in range (2, n - 2):
            # init text ist gleich je Wechselposition
            t_init = s1r_ [ n - wp - 1: n]
            t_init += s2_ [ : wp]
            ixbs = wp * 2 + wp % 2
            for aw in range (0, (n - wp - 2) * 2, 2):
                t = t_init
                ix = ixbs + aw
                ident [ix] = ident [ix] [4: ]
                t += ident [ix]
                #print (wp, aw, ix, t)
                if t not in s:
                    s.add (t)
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
#        zigzag1_1 = [s1_ [zi: zi + 2] for zi in range (1, n - 2, 2)]
#        zigzag1_2 = [s2_ [zi: zi + 2] for zi in range (2, n - 1, 2)]
#        zigzag1 = "".join ([x + y for (x,y) in zip (zigzag1_1, zigzag1_2)])
#        zigzag2_1 = [s1_ [zi: zi + 2] for zi in range (2, n - 2, 2)]
#        zigzag2_2 = [s2_ [zi: zi + 2] for zi in range (3, n - 1, 2)]
#        zigzag2 = "".join ([x + y for (x,y) in zip (zigzag2_1, zigzag2_2)])

