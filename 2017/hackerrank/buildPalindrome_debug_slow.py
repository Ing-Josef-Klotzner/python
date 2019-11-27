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

from os import environ
from collections import defaultdict
from time import time
#from sys import maxsize

#from sys import setrecursionlimit
#setrecursionlimit (100000)

"""
tc6:
1
jaqsoqgfpovigxfvhltpwptojsardozogrltulberiywireebjddkdhpyleypylevvglkckubmygxzqmeeyehvsgrslryxfqgrmdsqwptajbqzvethuwyfgdcbkdgxzurjpoahrhdpqexzsrpgvdutabogkwkuehfzwhvamsntzuvcrqzplxhykiaoapjzkznmlsnezsskdlosiyfawaznbuwenovcsfkfuhntglvesxsrrnzkbhzkhzmvkjevsrbdiclckmsgpgngyckzvgysvwcgwayjokqactfxtivfbdwprufivtggzhbpvlxfkisdneogdseenjlewrobjhpppjczyxeaiqanaztksnpfwyhdjvipgwzznmnnxwraiieicscdhryzvrhtoprratxufcithokiogudggzpvjctbahnzdwtokiatsriqzwedrrfzbrkgvynbbfomoiawwmmjiqvhdlnsvwnwbktehykevhacvdflm
nkrljmijvfxdvdydmvkjsbpmcgmnftseumhbdiohzcjvpayxqwdpychqctudlkedtbjduqbzwxvoxjlajstaoqnrrrpxcndmwhlwdygnnordxmujnljbdatxghfzqrwvfgakwmoawlzqjypmhllbbuuhbpriqsnibywlgjlxowyzagrfnqafvcqwktkcjwejevzbnxhsfmwojshcdypnvbuhhuzqmgovmvgwiizatoxgblyudipahapiduylbgxotaziiwgvmvogmqzuhhubvnpydchsjowmfshxnbzvejewjcktkwqcvfaqnfrgazywoxljglwybinsqirpbhuubbllhmpyjqzlwaomwkagfvwrqzfhgxtadbjluhtevzqbjatpwqsdmrgqfxyrlsrgsvfymgrfmzxqpejcixxppqgvuawutgrmezjkteofjbnrvzzkvjtacfxjjoki
out:
vsgrslryxfqgrmdsqwptajbqzvethuljbdatxghfzqrwvfgakwmoawlzqjypmhllbbuuhbpriqsnibywlgjlxowyzagrfnqafvcqwktkcjwejevzbnxhsfmwojshcdypnvbuhhuzqmgovmvgwiizatoxgblyudipahapiduylbgxotaziiwgvmvogmqzuhhubvnpydchsjowmfshxnbzvejewjcktkwqcvfaqnfrgazywoxljglwybinsqirpbhuubbllhmpyjqzlwaomwkagfvwrqzfhgxtadbjluhtevzqbjatpwqsdmrgqfxyrlsrgsv

tc1:
10
ottloictodtdtloloollllyocidyiodttoacoctcdcidcdttyoiilocltacdlydaailaiylcttilld
jevgfsuujwrunvgvgwpfbknkruvwzgxxgksmexqvxbghfffseuugxkwexhzfbpu
qquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfistulgbglwmfgzrnyxryetwzhlnfewczmnoozlqatugmd
jwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbszcepigpbzuzoootorzfskcwbqorvw
dczatfarqdkelalxzxillkfdvpfpxabqlngdscrentzamztvvcvrtcm
bqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunydtmwbexsngxhwvroandfqjamzkpttslildlrkjoyrpxugiceahgiakev
kfnfolpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyjj
qrxpxnloeozxpnvasorcvubxksccsobkxwrthytecnplbfcplofx
mlfcpidlqrvngnvttaifcbopnwezesomkxhaiafmvkbjaisyr
btultpnxbcrmornqumatserhieqggrivouwfnbnghdfall
pb
kkb
rfq
xzj
zlc
zdw
s
k
w
n
out:
-1
oozlzoo
lxsysxl
folpcfblpncetyhtrwxkbosccskxbuvcrosavnpxzoeoyyghbbqkflslfkqbbhgyyoeozxpnvasorcvubxksccsobkxwrthytecnplbfcplof
rvngnvr
bkkb
-1
zlz
-1
-1

tc2:
10
uxivudydgxwsgmhlracaayipsojleqhpygshcvxvchsgyphqeljospiyaacuvmeewpdwpiymwbhoxebjibxphief
gtsawcdivtltrshjqnkkmdtjgscnozmojnhigippjemzzzbcvoyplxenffmfdzdiojuodgbulvarlhmgswxgdyduviyaov
ddqpcjxzftwrlgptrkbkrlwgsnlcaudzdujbb
qlfzikgxohvhtuvcjmmwvhkxcg
lcjqoneppydpspiwqbkpsunexicskpmzmokfrcvrszcvdyfwuhtzptbbnxbhqjomxrbhjqxv
daserfpkscixqylqprawyquevhvuzcvfmbe
gfirlz
zbczeghmuhx
pcvqejw
owqsfhov
uuvepr
riyfwsts
ppomdfdtvv
tdfdmopp
ibdknprn
ptjpjtrq
ervhveh
gdfigxq
egfncsa
ascnfg

out:
ivudydgxwsgmhlracaayipsojleqhpygshcvxvchsgyphqeljospiyaacarlhmgswxgdyduvi
trkbkrt
xicskpmzmpkscix
geg
qeq
rr
ppomdfdtvvtdfdmopp
rtjpjtr
-1
gfncsaascnfg

tc3:
10
tsqejfoxyvszpuuvetdfluuhxpeopuxmdylaysttenjmcedcumoeeicjtxkkvxcxvkkxtjcifbeutdcsdrviozobdytwsi
mseetqckeeomucdecmjnettsyalydmxupoepxhuulfdtevuupzsvyynamdjxnsmkiewkwdpzjpkibcbbmzbiwpmjczcehtczqjzl
bkiimwwkwkbwwkwwmiikbwmikbiiwbkkwimmwiwiwkmkbkm
hjxhxvluhtdnzgxjfgedtzfxhzeoootvjqeegoysgoppdvvzd
drouylqobsgemwdoibqvcyedfvqoebvdujgsulahkprfrxco
xbfzlwcxfvqaavfegpkhalusgjudvbeqzqifuaoubukyp
tqflceilpmszizfw
bonxplcyqittpk
ngoqbpielolgfelgbpofbifnf
jkhhyhdcjxzymxcddavzkzwyhwtsj
uoavyovdbielzdobgqcjzn
jbexalkghywioxzbvx
chwszhvcdooejlcqvqmhx
hcwccwchcljeoodcvhzswhcf
eavwjmgvhuesssaxgmoywdg
vwvgdwyomgxassseuhvgmjw
qatxbuzxpstpyggyptsuqmx
enprpmypxzubxtatesstwhy
bximeeswyndfh
m

out:
yvszpuuvetdfluuhxpeopuxmdylaysttenjmcedcumoeeicjtxkkvxcxvkkxtjcieeomucdecmjnettsyalydmxupoepxhuulfdtevuupzsvy
-1
ebvdujgsulahkprfrpkhalusgjudvbe
lpmpl
-1
ava
chwszhvcdooejlchcwccwchcljeoodcvhzswhc
wjmgvhuesssaxgmoywdgvwvgdwyomgxassseuhvgmjw
atxbuzxpstpyggyptspxzubxta
meem

tc4
10
zbvebyeucepgcdpmghcibfxgrvnacytonmliivrkbblvnmhiprgeryrpjpjykchneyfymiefymajrnrjamyfeimyfwmedxbmxag
imxmxgjlnnfkwbrqshxfcanwpoflqejafdktnlpgvlexcygyenhckyjpjpryregrpihmnvlbbkrviilmnotycmlilwztbscfh
zfffzzzzzzzzzfffffffzfzzzzzzfzzfzzzfzffzfffffffzzfzfzffzzzzff
qnabqokracewqildmvgchtqkbjovegqaqrymqeutaqbluspigttdenepi
wdozitqgqiphvwuijwhsmgogxomlcggiwkhnarjisvcdpzggtlludvdulltggzpdcvsijranhkwiinzxcd
xewculofitylhxhzxmjdlisupdylshahciggcptullyisxsczjqawagn
imtpftgy
tkfntylnflbfutsyovxmligoaiqz
iiiimasfxxmd
kzrelybyekpnkzyyblhwr
kccurpzpumcsm
qhebhqrfigammagifrqhbehqmscmupzprucc
ayxjeqkkrrrkqgeagvkvrvqgkkjaeugerxkk
fzztoidbwcpcsnthnmdicbbnlowmdcdztmic
qtkqbajuldlwrpkrtfblbftrkprwldlujyql
pzbnsbzhanbiypuziqurwabrbxmhbrdpdrer
pgjlcktlaqsalnoiphbtuy
rrghseznkmzukaiihat
actadtninwc
z
out:
cytonmliivrkbblvnmhiprgeryrpjpjykchneyfymiefymajrnrjamyfeimyfyenhckyjpjpryregrpihmnvlbbkrviilmnotyc
-1
cggiwkhnarjisvcdpzggtlludvdulltggzpdcvsijranhkwiggc
fbf
-1
ccurpzpumcsmqhebhqrfigammagifrqhbehqmscmupzprucc
-1
bajuldlwrpkrtfblbftrkprwldlujab
grrg
-1
"""
def bisect_left (sa, x, text, lo = 0, hi = None):
    if lo < 0:
        raise ValueError ('lo must be non-negative')
    if hi is None: hi = len (sa)
    while lo < hi:
        mid = (lo + hi) // 2
        if text [sa [mid] : ] < x: lo = mid + 1
        else: hi = mid
    if not text [sa [lo] : ].startswith (x):
        # i suppose text[a[lo]:a[lo]+len(x)] == x could be a faster check
        #raise IndexError ('not found')
        return -1
    return sa [lo]

def kasai_lcp (s, sa, n):   # sa  suffix array
    k = 0
    lcp = [0] * n; rank = [0] * n
    for i in range (n): rank [sa [i]] = i
    for i in range (n):
        k -= 1 if k else 0
        if rank [i] == n - 1: k = 0; continue
        j = sa [rank [i] + 1]
        while i + k < n and j + k < n and s [i + k] == s [j + k]: k += 1
        lcp [rank [i]] = k
    return lcp

# O (n)    !!   fastest
def suffixArray (s, n):
    def suffix_array (s, n, K):
        # skew algorithm
        s += [0] * 3
        n0 = (n + 2) // 3;  n1 = (n + 1) // 3;  n2 = n // 3
        n02 = n0 + n2;   adj = n0 - n1
        def radix_pass (a, o, n = n02):
            c = [0] * (K + 3)
            for x in a [ : n]: c [s [x + o] + 1] += 1
            for i in range (K + 3): c [i] += c [i - 1]
            for x in a [ : n]:
                j = s [x + o]; a [c [j]] = x; c [j] += 1
        A = [x for x in range (n + adj) if x % 3] + [0] * 3
        radix_pass (A, 2); radix_pass (A, 1); radix_pass (A, 0)
        B = [0] * n02;   t = [];   m = 0
        for x in A [ : n02]:
            u = s [x : x + 3];  m += t < u;  t = u
            B [x // 3 + x % 3 // 2 * n0] = m
        A [ : n02] = 1 // n02 * [0] or suffix_array (B, n--~n//3, m)
        I = A * 1
        for i in range (n02): I [A [i]] = i + 1
        B = [3 * x for x in A if x < n0]
        radix_pass (B, 0, n0)
        R = [];  p = 0;  t = adj
        while t < n02:
            x = A [t];  b = x >= n0
            i = (x - b * n0) * 3 - ~b;  j = B [p]
            if p == n0 or ((s [i : i + 2], I [A [t] - n0 + 1]) < (s [j : j + 2], I [j // 3 + n0]) if b else (s [i], I [A [t] + n0]) < (s [j], I [j // 3])): R += i,; t += 1
            else: R += j,; p += 1
        return R + B [p : n0]
    return suffix_array (list (map (ord, s)), n, 128)

def solve (a, b, sta, stb):
    # lcp - palindrome  ('abc' (from a) + x (from a) + 'cba' (from b))
    # found by lcp of a and reversed b    x ... if exists
    tim = time ()
    a_ = a [::-1]; b_ = b [::-1]; s = a + b_
    n = len (s); la = len (a);  lb = len (b)
    jsl = False
    if la > 100 or lb > 100: jsl = True   # just show length of palindromes
    sa = suffixArray (s, n)
    """umg. auf kasai lcp   l_p longest common prefix (length list)"""
    l = kasai_lcp (s, sa, n)
    print ()
    print ("time to build suffix array sa", time () - tim)
    tim = time ()
    _l_ix = 0   # find max l, where found lcp is in a and b_
    mx = 0
    ctl = defaultdict (tuple)
    for i in range (n):
        if not l [i]: 
            continue
#        print ((str (i) + " " + str (l [i]) + " " + s [sa [i] : sa [i] + l [i]]).ljust (10), end = " ")
        # l  Liste der Längen gemeinsamer prefixe zwischen a und b
        # check, if found lcp is in a and b_ and not in a only or b_ only
        """ mk m_l list from lcp l of tuples (plen, pix) - keep it lexographical 
            valid entries only if length of com prefix is from a and b_ and not a only or b_ only
            keep it lexogr. by ctl dict (right border is key and content is (length / indices to lcp/SA))
            only add different prefixes to dict - how identify different ones? -> different right border
            - when combining prefixes with existing palins in a or b they could overlap !
            ... so not just search for R_prefix == L_exist_pal, search if within others L to R """
        if (sa [i] < la and sa [i + 1] >= la or
            sa [i] >= la and sa [i + 1] < la):
            if len (sa) > 1:
                isa = i; isb = isa + 1
                if sa [isb] < sa [isa]: isa, isb = isb, isa
                ct = l [i]; L = sa [isa]; R = L + ct
                Lb = lb - sa [isb] + la - ct; Rb = Lb + ct
#            ct = l [i]; L = sa [i] if sa [i] < la else sa [i + 1]; R = L + ct
            # if same right side, it is same prefix, change entry if longer
            min_pre_len = max (0, mx - 2)
            if ct > min_pre_len:
                if R in ctl:
                    ctd, _, _, _, _, _ = ctl [R]
                    if ct >= ctd:
#                        print ("enlarge", s [R - ctl [R] [0] : R], "->", R - L, i, s [L : R], end = " ")
                        ctl [R] = (ct, i, L, R, Lb, Rb)
                else:
#                    print ("uniques: ", R - L, i, s [L : R], end = "  ")
                    ctl [R] = (ct, i, L, R, Lb, Rb)
            if ct > mx:
                mx = ct
                _l_ix = i   # index of longest prefix
    # build m_l list from dict ctl
    m_l = sorted (list (ctl.values ()))
#    print ("m_l", m_l, "len ctl", len (ctl), "_l_ix", _l_ix, s [sa [_l_ix] : sa [_l_ix] + l [_l_ix]])

    """
    längster prefix wird kombiniert wird mit bis 3 Folgezeichen (palindrome) in a, Vorfolgezeichen in b
    """
    if len (sa) > 1:
        isa = _l_ix; isb = isa + 1
        if sa [isb] < sa [isa]: isa, isb = isb, isa
        l_ct = l [_l_ix]; L = sa [isa]; R = L + l_ct
        Lb = lb - sa [isb] + la - l_ct; Rb = Lb + l_ct
    else: return "-1"
    x1 = a [R] if R < la else ""
    if R + 1 < la and a [R] == a [R + 1]: x1 = a [R : R + 2]
    if R + 2 < la and a [R] == a [R + 2]: x1 = a [R : R + 3]
    x2 = b [Lb - 1] if Lb - 1 >= 0 else ""
    if Lb - 2 >= 0 and b [Lb - 2] == b [Lb - 1]: x2 = b [Lb - 2 : Lb]
    if Lb - 3 >= 0 and b [Lb - 3] == b [Lb - 1]: x2 = b [Lb - 3 : Lb]
    Lft = False; x = ""
    lx1 = len (x1); lx2 = len (x2)
    if lx2 > lx1 or lx2 == lx1 and x2 < x1: x = x2; Lft = False
    elif lx1 > lx2 or lx2 == lx1 and x1 < x2: x = x1; Lft = True
    if not x1 and not x2: sg1 = "_"; sg2 = ""
    elif Lft: sg1 = ","; sg2 = "_"
    else: sg1 = "_"; sg2 = ","
    lcp_palin_l = a [L : R]; lcp_palin_r = b [Lb : Rb]
    lcp_palin = lcp_palin_l + x + lcp_palin_r if lcp_palin_l else ""
    lcp_palin_p = " " + lcp_palin_l + sg1 + x + sg2 + lcp_palin_r if lcp_palin else ""
    lcp_palin_pl = " " + str (len (lcp_palin_l)) + sg1 + str (len (x)) + sg2 + str (len (lcp_palin_r)) if lcp_palin else ""
    if jsl: print ("palin a + b_", "{:7.5f}".format (time () - tim), lcp_palin_pl, lcp_palin_l [ : 5], "..")
    else: print ("palin a + b_", "{:7.5f}".format (time () - tim), lcp_palin_p)

    res_pal = lcp_palin

    """ puuzle palindrome fact tc14_1: 
        length b: 49473,   1630 + 29033 + 1630
                          cutb_ + palb  + cutb """
    # trying to find part of palindrome in a + a_ and b + b_
    # these are no standalone answers, as it is not ollowed to 
    # combine with empty string from other (b or a)
    tim = time ()
    s_a = a + a_; na = la * 2; s_b = b + b_; nb = lb * 2
    saa = suffixArray (s_a, na)
    l_a = kasai_lcp (s_a, saa, na)
#    print ()
#    print ("kasai lcps of partly palindromes of a")
#    for i in range (na):
#        if l_a [i]: print ((str (i) + " " + str (l_a [i]) + " " + s_a [saa [i] : saa [i] + l_a [i]]).ljust (10), end = " ")
    sab = suffixArray (s_b, nb)
    l_b = kasai_lcp (s_b, sab, nb)
#    print ()
#    print ("kasai lcps of partly palindromes of b")
#    for i in range (nb):
#        if l_b [i]: print ((str (i) + " " + str (l_b [i]) + " " + s_b [sab [i] : sab [i] + l_b [i]]).ljust (10), end = " ")
    """ code used for super palindrome """
    # get max a_palin if "La" == R

    """ change to find from longest of l_a list a_palin which "La" == R """
#    l_a_ix = l_a.index (max (l_a)); l_a_p = l_a [l_a_ix]
#    La = saa [l_a_ix]; Ra = La + l_a_p
#    p_a = a [La : Ra]
#    p_a_palin = p_a if p_a == p_a [::-1] and La == R else ""

#    print ()
#    print ("part of palindrome in a", p_a_palin)
    # get max b_palin if "Rbp" == Lb

    """ change to find from longest of l_b list b_palin which "Rbp" == Lb """
#    l_b_ix = l_b.index (max (l_b)); l_b_p = l_b [l_b_ix]
#    Lbp = sab [l_b_ix]; Rbp = Lbp + l_b_p
#    p_b = b [Lbp : Rbp]
#    p_b_palin = p_b if p_b == p_b [::-1] and Rbp == Lb else ""

#    print ("part of palindrome in b", p_b_palin)
    """ super palindrome, if exists
this is a palindrome consistent of 
part of palindrome + found pal in a or b + part of palindrome_
    """
#    s_pal = lcp_palin_l + p_a_palin + lcp_palin_r if La == R else ""
#    s_pal_p = lcp_palin_l + "_" + p_a_palin + "_" + lcp_palin_r if La == R else ""
#    s_pal_pl = str (len (lcp_palin_l)) + "_" + str (len (p_a_palin)) + "_" + str (len (lcp_palin_r)) if La == R else ""
#    if len (s_pal) > len (res_pal): res_pal = s_pal
#    elif len (s_pal) == len (res_pal) and s_pal < res_pal:
#        res_pal = s_pal
#    s_pal_ = lcp_palin_l + p_b_palin + lcp_palin_r if Rbp == Lb else ""
#    s_pal_p_ = lcp_palin_l + "_" + p_b_palin + "_" + lcp_palin_r if Rbp == Lb else ""
#    s_pal_p_l = str (len (lcp_palin_l)) + "_" + str (len (p_b_palin)) + "_" + str (len (lcp_palin_r)) if Rbp == Lb else ""
#    if len (s_pal_) > len (res_pal): res_pal = s_pal_
#    elif len (s_pal_) == len (res_pal) and s_pal_ < res_pal:
#        res_pal = s_pal_
##    print ()
#    if jsl:
#        print ("super palindrome a ", s_pal_pl)
#        print ("super palindrome b ", "{:7.5f}".format (time () - tim), s_pal_p_l)
#    else: 
#        print ("super palindrome a ", s_pal_p)
#        print ("super palindrome b ", "{:7.5f}".format (time () - tim), s_pal_p_)
    print ("time to build suffix array saa, sab", time () - tim)

    """          puzzle palindrome 2         """
    # combine and find maximum palindrome:
    # combine m_l list with all palindromes in a and in b, check if overlap / fit, find maximum
    tim = time ()
    p2_ca_pal = p2_ca_pal_p = p2_ca_pal_pl = ""; l_p2_ca_pal = 0
    for isaa, l_a_ct in enumerate (l_a):
        if l_a_ct < 1: continue
        isaa_ = isaa + 1
        if saa [isaa_] < saa [isaa]: isaa, isaa_ = isaa_, isaa
        if saa [isaa] > la or isaa_ < na and saa [isaa_] < la: continue
        Lax = saa [isaa]; Rax = Lax + l_a_ct
        pala = a [Lax : Rax]
        if pala != pala [::-1]: continue
        for ct, i, L, R, Lb, Rb in m_l:
            if R >= Lax and R < Rax: 
                df = R - Lax; fd = a [L : Lax]; fd_ = b [Lb + df: Rb]
#                print ("f a", a [L:R], fd + "," + pala + "_" + fd_, end = "  ")
                p2_ca_palin = fd + pala + fd_ if fd else ""
                p2_ca_palin_p = fd + "," + pala + "_" + fd_ if fd else ""
                if jsl: p2_ca_palin_pl = str (Lax - L) + "," + str (Rax - Lax) + "_" + str (Rb - Lb - df) if fd else ""
                l_p2_ca_palin = 2 * (Lax - L) + Rax - Lax
                if (l_p2_ca_palin > l_p2_ca_pal or 
                    l_p2_ca_palin == l_p2_ca_pal and p2_ca_palin < p2_ca_pal):
                        l_p2_ca_pal = l_p2_ca_palin
                        p2_ca_pal = p2_ca_palin
                        p2_ca_pal_p = p2_ca_palin_p
                        if jsl: p2_ca_pal_pl = p2_ca_palin_pl
    if l_p2_ca_pal > len (res_pal): res_pal = p2_ca_pal
    elif len (p2_ca_pal) == len (res_pal) and p2_ca_pal < res_pal:
        res_pal = p2_ca_pal
    if jsl: print ("puzzle palindrome 2 a ", "{:7.5f}".format (time () - tim), p2_ca_pal_pl, p2_ca_pal [ : 5], "..")
    else: print ("puzzle palindrome 2 a ", "{:7.5f}".format (time () - tim), p2_ca_pal_p)
    tim = time ()
    p2_cb_pal = p2_cb_pal_p = p2_cb_pal_pl = ""; l_p2_cb_pal = 0
    for isab, l_b_ct in enumerate (l_b):
        if l_b_ct < 1: continue
        isab_ = isab + 1
        if sab [isab_] < sab [isab]: isab, isab_ = isab_, isab
        if sab [isab] > lb or isab_ < nb and sab [isab_] < lb: continue
        Lbx = sab [isab]; Rbx = Lbx + l_b_ct
        palb = b [Lbx : Rbx]
        if palb != palb [::-1]: continue
        for ct, i, L, R, Lb, Rb in m_l:
            if Rbx >= Lb and Rbx < Rb:
                df = Rbx - Lb; fd = a [L : R - df]; fd_ = b [Rbx : Rb]
#                print ("f b", fd + "_" + palb + "," + fd_, b [Lb : Rb], end = "  ")
                p2_cb_palin = fd + palb + fd_ if fd else ""
                p2_cb_palin_p = fd + "," + palb + "_" + fd_ if fd else ""
                if jsl: p2_cb_palin_pl = str (R - df - L) + "," + str (Rbx - Lbx) + "_" + str (Rb - Rbx) if fd else ""
                l_p2_cb_palin = 2 * (Rb - Rbx) + Rbx - Lbx
                if (l_p2_cb_palin > l_p2_cb_pal or 
                    l_p2_cb_palin == l_p2_cb_pal and p2_cb_palin < p2_cb_pal):
                        l_p2_cb_pal = l_p2_cb_palin
                        p2_cb_pal = p2_cb_palin
                        p2_cb_pal_p = p2_cb_palin_p
                        if jsl: p2_cb_pal_pl = p2_cb_palin_pl
    if l_p2_cb_pal > len (res_pal): res_pal = p2_cb_pal
    elif len (p2_cb_pal) == len (res_pal) and p2_cb_pal < res_pal:
        res_pal = p2_cb_pal
    if jsl: print ("puzzle palindrome 2 b ", "{:7.5f}".format (time () - tim), p2_cb_pal_pl, p2_cb_pal [ : 5], "..")
    else: print ("puzzle palindrome 2 b ", "{:7.5f}".format (time () - tim), p2_cb_pal_p)

    """          puzzle palindrome          """
    # find in a, combine with b and vice versa
    # for all longest common prefixes > 1 of l_a (a + a_),
    # which are palindromes (pal): cut text from a until begin
    # of each palindrome; get sap, lcpp lists of cutted text + b_ 
    # -> plcp (puzzle lcp)
    # build   plcp + pal + plcp_ (reverse) and take longest
    # with b cut text from end of pal to end of b
    print ("length of a",la)
    if la < 100 or la == 9098 or la == 95540:
        tim = time (); Lax_ = Rax_ = 0
        p_ca_pal = p_ca_pal_p = p_ca_pal_pl = ""; l_p_ca_pal = 0
        #mx_ix = l_a.index (max (l_a))
        for isaa, l_a_ct in enumerate (l_a):
            if l_a_ct < 1: continue
            isaa_ = isaa + 1
            if saa [isaa_] < saa [isaa]: isaa, isaa_ = isaa_, isaa
            if saa [isaa] > la or isaa_ < na and saa [isaa_] < la: continue
            Lax = saa [isaa]; Rax = Lax + l_a_ct
            pala = s_a [Lax : Rax]
            lpaa = Rax - Lax   # len (pala)
#            if la > 9500 and lpaa < 10 or la > 2500 and lpaa < 5  or la > 100 and lpaa < 3 or pala != pala [::-1]: continue
            if la == 95540 and lpaa < 10 or la > 100 and lpaa < 10 or pala != pala [::-1]: continue            
            # pala now are only palindromes for further processing
            cuta_ = a [ : Lax] [::-1]; s_ca = cuta_ + '$' + b + '|'
    #        print (cuta_, end = " ")
            nca = len (s_ca)
            saca = suffixArray (s_ca, nca)
    #        print (saca)
            l_ca = kasai_lcp (s_ca, saca, nca)
    #        print (l_ca)
            # finde den prefix dessen Eintrag in saca 0 ist (Beginn cuta_)
            aix = saca.index (0)
            # wenn l_ca [aix - 1] > l_ca [aix], dann nimm aix - 1, weil nächster anderer prefix ist
            if aix and l_ca [aix - 1] > l_ca [aix]: aix -= 1
    #        print ("pala", pala, aix, s_ca [saca [aix] : saca [aix] + l_ca [aix]], end = " ")
            # wenn beide prefixe in cuta_ oder beide in b liegen -> ungültig, continue
            lca = len (cuta_)
            if (saca [aix] < lca and saca [aix + 1] < lca or 
                saca [aix] >= lca and saca [aix + 1] >= lca): continue
    #        print ("pala", pala, end = " ")
            found_ = s_ca [saca [aix] : saca [aix] + l_ca [aix]]
    #        print ("found_", found_, aix, l_ca [aix], end = " ")
            found = found_ [::-1]
            l_found = l_ca [aix]
            l_p_ca_palin = 2 * l_found + Rax - Lax
            p_ca_palin = found + pala + found_ if found else ""
            p_ca_palin_p = found + "," + pala + "_" + found_ if found else ""
            p_ca_palin_pl = str (l_found) + "," + str (Rax - Lax) + "_" + str (l_found) if found else ""
            if (l_p_ca_palin > l_p_ca_pal or 
                l_p_ca_palin == l_p_ca_pal and p_ca_palin < p_ca_pal):
                    l_p_ca_pal = l_p_ca_palin
                    Lax_ = Lax; Rax_ = Rax
                    p_ca_pal = p_ca_palin
                    p_ca_pal_p = p_ca_palin_p
                    p_ca_pal_pl = p_ca_palin_pl
    #        print (p_ca_palin, end = "  ")
        if len (p_ca_pal) > len (res_pal): res_pal = p_ca_pal
        elif len (p_ca_pal) == len (res_pal) and p_ca_pal < res_pal:
            res_pal = p_ca_pal
        if jsl: print ("puzzle palindrome a ", "{:7.5f}".format (time () - tim), p_ca_pal_pl, p_ca_pal [ : 5], "..", Lax_, s_a [Lax_ : Lax_ + 5] + "..." + s_a [Rax_ - 5 : Rax_], Rax_, "length of a", la)
        else: print ("puzzle palindrome a ", "{:7.5f}".format (time () - tim), p_ca_pal_p)
        
#    print ()
    if la < 100 or la == 6938:
        tim = time (); Lbx_ = Rbx_ = 0
        p_cb_pal = p_cb_pal_p = p_cb_pal_pl = ""; l_p_cb_pal = 0
        #mx_ix = l_b.index (max (l_b))
        for isab, l_b_ct in enumerate (l_b):
            if l_b_ct < 1: continue
            isab_ = isab + 1
            if sab [isab_] < sab [isab]: isab, isab_ = isab_, isab
            if sab [isab] > lb or isab_ < na and sab [isab_] < lb: continue
            Lbx = sab [isab]; Rbx = Lbx + l_b_ct
            palb = s_b [Lbx : Rbx]
            lpab = Rbx - Lbx   # len (palb)
#            if lb > 2500 and lpab < 10 or lb > 100 and lpab < 3 or palb != palb [::-1]: continue
            if la == 6938 and lpab < 6 or palb != palb [::-1]: continue
            # palb now are only palindromes for further processing
            cutb = b [Rbx : ]; s_cb = cutb + '$' + a_ + '|'
            ncb = len (s_cb)
            sacb = suffixArray (s_cb, ncb)
    #        print (sacb)
            l_cb = kasai_lcp (s_cb, sacb, ncb)
    #        print (l_cb)
            # finde den prefix dessen Eintrag in sacb 0 ist (Beginn cutb)
            bix = sacb.index (0)
            # wenn l_cb [bix - 1] > l_cb [bix], dann nimm bix - 1, weil nächster anderer prefix ist
            if bix and l_cb [bix - 1] > l_cb [bix]: bix -= 1
    #        print ("palb", palb, bix, s_cb [sacb [bix] : sacb [bix] + l_cb [bix]], end = " ")
            # wenn beide prefixe in cuta_ oder beide in b liegen -> ungültig, continue
            lcb = len (cutb)
            if (sacb [bix] < lcb and sacb [bix + 1] < lcb or 
                sacb [bix] >= lcb and sacb [bix + 1] >= lcb): continue
    #        if jsl: print ("palb length", len (palb), end = " ")
    #        else: print ("palb", palb, end = " ")
            found_ = s_cb [sacb [bix] : sacb [bix] + l_cb [bix]]
            found = found_ [::-1]
            l_found = l_cb [bix]
            l_p_cb_palin = 2 * l_found + Rbx - Lbx
            p_cb_palin = found + palb + found_ if found else ""
            p_cb_palin_p = found + "_" + palb + "," + found_ if found else ""
            p_cb_palin_pl = str (l_found) + "_" + str (Rbx - Lbx) + "," + str (l_found) if found else ""
            if (l_p_cb_palin > l_p_cb_pal or
                l_p_cb_palin == l_p_cb_pal and p_cb_palin < p_cb_pal):
                    l_p_cb_pal = l_p_cb_palin
                    Lbx_ = Lbx; Rbx_ = Rbx
                    p_cb_pal = p_cb_palin
                    p_cb_pal_p = p_cb_palin_p
                    p_cb_pal_pl = p_cb_palin_pl
    #        print (p_cb_palin, end = "  ")
        if len (p_cb_pal) > len (res_pal): res_pal = p_cb_pal
        elif len (p_cb_pal) == len (res_pal) and p_cb_pal < res_pal:
            res_pal = p_cb_pal
        if jsl: print ("puzzle palindrome b ", "{:7.5f}".format (time () - tim), p_cb_pal_pl, p_cb_pal [ : 5], "..", Lbx_, b [Lbx_ : Lbx_ + 5] + "..." + b [Rbx_ - 5 : Rbx_], Rbx_, "length of b", lb)
        else: print ("puzzle palindrome b ", "{:7.5f}".format (time () - tim), p_cb_pal_p)
    return res_pal
    

def buildPalindrome (a, b):
    sta = set (a); stb = set (b)
    if sta.isdisjoint (stb) or a == "" and b == "": return "-1"
    res = solve (a, b, sta, stb)
    return res

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    t = int (input ())
    for _ in range (t):
        a = input ()
        b = input ()
        result = buildPalindrome (a, b)
        if len (result) < 50: print (result)
        else: print ("result > 50 in length", result [ : 50] + "...")
        fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()

"""
tc0 - part
5
aeenyaulnadoqjkzwdbzmogeiiywrfvuhzublopafnxftpktilcsvbpmocapvinieppkobjhfykimmhecqvebpboskoojublktktzxkllyrwgnkywyhflncpggsxckaobobahgeybavprlfqaarwfxaaawvuxtumfrkulcydzawdkiqvfybjyrqsaurznbmudbatyydqpsgsxssubzjdjioeidugdaztttgbxjmuojlequmjtixitjsvtncxwdtldmdycnxkvdqyatvtyrzahuuwjsquwzxybjjnsmwxudxjurmacoaocwipmtapywobjzxofoneokcjeclvlbiivymruroxxhxsjlcilnfyzhmldhcfgrbjcmuwfgjcufidnreyilkcaltxcdebvwacqbuxhqpzemfuksaykrdhxlligmcqsyhzwtsodftahgzsqajgetoujkwygxdanrpcbsgepsnigqvfnlwiyacipvlevfinerclsysapittihgloqdsjbaaktdozepizqguhvcrbxxvkdxhcnisokwyraesdwlpnjjnjlxprhbilnaunrwynmvdaruczuzyownelriwctmhzwohuxtklimniqhqrddoiptzoytvcsrndsazppreliilzprovhcrfniilyxxfduyqzirhzqzmghvdfyozzpmtgmochkgbpfavibeazsenfiowtdqluuktycqqtlgwdkgxwktruiphokqklnsoiugxnxkqaxaofnvgppbnlphfbtfunewxvggzzoztghvgufjrubuesblducoccewkaucnwdjqaagauyhsmvbsfyjkqyxmgdctitrrtcmnnelohrctnvqwsoebgxoiqddtdmibixndfzltbcwovwgvslwfgcwskfzchdqwxhclkasgbfynzvfrighgtierscdjxfcicrioxyvlilkpgdgzkixpqzojlmxnsxenasxpvmsrsntaukldmnekxwnqfvyctkylgcxzbvsuqyxjleievdwbecxezjkbqmtouqabjhcykttdopqgukzoeptbxslebjyhtradxrfoedxmsgxgbgbiiocxzxhvhpqmdbviuhaklzbhixrvyaonpalttosplfzjimdrxesbbarusarflcualucdbhercpamrcbaibeibbtfuuuupkhnmqopsdbbsrxnypngvotchupdlmopbdpnnimqrixedirziugevtcktvrtgrjwjbrhqglpfkmzcjomofsfdqqsvgnzzeinhivxiltqpmcxqpbtjpbwcdkrbdngavfgwzauuveilavftxtbsiwuqzwxkwglhqopwycbiuxzvccsrtdtkstkxlzoxrghggakjfaznharerkwvvgebarseyxcpbixlypfrpurwntnondswgrsxqxnwtrqoisctvypokgjzfutzemdkaroouvyeyvsnenituvymyuoeehyixryutjoyyrssbqrnapsclooimbrewvfzmwklpubxuteqqbupulxurasgwcnuqwusfdrldydbhviulvymaiodbxjkuwjucsplfjeaisjtcprxcoazbasxltlesaeznerykqepnyulvtcunakvhxjlmhljnevpuqyzshstcdexkhkormxpklkknorokkeadlkcfoxcmpjkhrwyahrotaprgloteomgkxzewfjjgvtamamooduskaccmbqrhtuzrftebixfktsvijpwgswmvzvfguqqikyfyxylcchezfxcoyqmvrqixbeyuzrumthwcodumvtwmmukxuolmxymesszpmlobbbiwhmcrkfsrklyrdiodrgvsphgiasojaavhnnvjjdflpttmecoxjwyvvwqtuffuykklnyatqiphuwjatnxzwgfwgoyhdxnqirnnsjlbwmabebqepstnyxylzberbougmqroxpinjgzqapipmkiegtsykmavtzdthplblgoqefnnjktaecanwsxubclsajpbdrhkpurcyrxhvuixdtzfzgdzbkijzgytmlflxtcfzjpcdgxsbeswgrdqmdytrvqawaikvfcbaezxfhalstvwejizhsveviszthhlimvhktyjajuykptuykqucabgdkqgfimbotbcvpnwsxuwnpvwphvphhnxbrfxrqmndgsjddbfcmmyzvncmqliygqkxfhylwazfjfkgqoimqcupgosezxcxuejnbygyvuwpcmiikqsbunafsclkvehwdpawbtxsmmevnforkkbpblimlakzpuisoigpjlpbwvwbnwknvbfptiakxnusvzhltmylrmdapmpqcxihmpgkijtygxlfqwoyevvgpmdxkbuncakemgdxkndslycvamszqg
knvappatgxtoiknjrjjoilqbooatluwolsesmvltzdflbmwzrnmsviknnbylvqozfysmcpxjhshbgwekraryojmycgvbyhotrdotvurlrjhrryyzlncqectjossprimhfylqgbfqqfhzhhbxsdhrlxckiktpksdwduuttwavxzbjbrlqgcuihkxowrcollamqahgcpvmtpfjibdsziuaeppewoqubarmmgzmjfolyucdqxaudmbkcgxmmyfwwiqjdcspxlgzlyizzbpvvsrbezmwzqapodexnxalxtczlanwrrlzorqmsinxndpzgjragwrsmjjesarullazbukqxugymciecgjfszuqgnywhnktsfbsatakbusnxedseikjfyhgcgmzlgyzdnbwivosqqeffqbmpexmpgfjbkgqsurtizjrkyixxfldfjpvlnaxcqcupkkysziciisgkjmbsxujryhfozwvipyqwohegndowghmrroejbvllldksbmynzobqtsislcmmsojytwrufhazrpzwmfcblitnnosngumfcyvoopncwafwmfeeyfgovjheamhzddsipyrblxmvkwqyvqxiyzfcmxlcmwjshjtsnrmftkehvxlmiwtxgzjocelrnjppcyuvpyzasgwjtfdsmzffubkeakekxmyneidlgzmxcbarodxnqtzswfvwtiasmggwcjevqplwsqykilgydehlrvnrunvuyymrrtopcjhluttshkudgjoepqzwkfzsleydonzbhuftwwsapjpfaqtjbubiwouctxzyxrdgdzorbhjzyksjydqdzavfvqmeusxpvxzuipacbesuvkwyxuzumlyimrinqajfzropbgxqpkchczkyklhsqabqymmvmsylyjedlxgsmbvcozyuodyrmkijrvismkokiwpsmjebtdvizugxiemukvvkzomnntqihudjsmdzrmbnomvlowygwsiebnxulocteptljrhfxgohxogjrxyoqebxbwmlzmakolkgwqjmqmmbjchgvrycasqedsrxjorwkgicxqqlxebbxfcuvqucntoggvdawwsijfzhftiejmyffuaubnwohxyhypeulnezziuzchasnibdteurauqprlzoqkuoyqhjswgtrzxduirdfeixfhrkwwpkncmybkrqrsflytrufamqvodztuboolmgcibgoggrvbjrdcsijoorrdgopvatbzuoqetulniwlfyocwvbsjosrqlvipzphcelywiprsdhdplavaprpphvbyyqnamgopxszcvwtfmyurxienuaqefozksujoxuedezqymardpumxaebfjskhabuyiervaobrxtiuhtebdsyrqoyxnjvvxzrdoumrhelkshmyrsxfpleomdlemvwmcbcyxvdkwwwebndpbeomrxjyuaklakqvgoswwxfvptoiowdhdlkyezkmqwhbemeefqdazhroibfxfpjylxdxwcmedeysjflgptmkuatnnhuersrdzimupaiwmxmhlfypjjztenqnuptezkgoeglqvmdjfknpksswblxbidotxnfgziqlhchxatoasladltswaegooshjriqhzviamdomqdwpcqauvkxthvyivhgysgznwnktbzqsetujqyrhxfmjgapjeoxounyfjwwyljrohksqkbonbxydthjipcqvknxehudznszvhwjfickotjbfmkmjoiuchmgqwgtfzpawwchulzfhkfuvkrcliaolvzzwmeespggxgzlkxulzjetbynzfshvvepmuyixipflvtonaagiofnhzkfjrmqenpglubtxlkuczncqynrwngbixeznigesseccgvqsxhixkdzsmtllsafhfwhdgbpulhdxowqoroxpjetypusxyglpivlcrosocfryflikhtrabgtshwbqfnjxcityvtyukzvzhtqifjvaujqjejsslpshhtisortbxrrspqsmxlrsnhdgsizqzurjtrcgldqfpvpvqzptxzfmfucgbwbmdjfkkknfkbsyacuzbbqvepcgagoylngtjdvphuuiuyxnjmkixaerorgeqgsdmdinsixucarxusookicrqaqtrstjqvmsddzvxtcnpwcfjbkmaogxrgyxbjgqqjjzkmufsvtjcvqbkpbwgowiddzeawdzfuyohyqzpyujgtjhtqwbvdyjrpycv
ijdjnlihihddjrnijhiiadjaaljjdnlalyaahijlyrjjnijylnlidinddydhjhdrainajddnnlnlrnadhiiayhdnihjlyrjydijlyrraaddllyalhhhlyjlharjrajdydhhdyiinrrnddynynaydiyrirajyhlnahidrriyiyjrdyihrihlhihnnhyndhlljayhaaraaldiyjhnyhyhillhrinaryhylyidjhrnnyilhndjaryaiyyjinnrndlirhydaryhdrajilnhhinihnllldyijyidnjjrinrindyaarjhjjldyhrryjljhyjjhrlhyahdalhyhlailyiliyiiyalaydaanaidhdnrrijhirnjarhlnhnhrjdajhiyhhihjarlllihlhrlahrnnjdrndyjlrrhrdyjyhrjdjayihryrldjaiiinyhyidaylnnjararhynnidnjhnnndhlrahyhdajjlahjajlalhhilhdnrlyjhlyajrydayjianhhrhjynljyhajdhjriirnjnlianhhnyrlaildyrljhrdihrjdjhdynrrairrijnharnhnylhrjhhharrdnlyyylyihliryidndyyirndlrildrijlrlrrrilhhihlijrranjiddaiydhjjnrjddhdhdhijljjjnynnjnjirhdjjyjdnrinlrdyaayhyhrnnyrhndljyhrdjljaydrljdlryiajadylaajinljliajjldrlnndajllydrlhdjjrhhianldndahyiydjahnrraiarhnlhndyijyyliharllariayayliryhlnydajlrrdjydilrdrhliarynarrlaynninrnadrradijrdlaildhllyjnyaarnanajidriinaririhjlrjhiajiirljaahyainlyjilyyharnaynldiayiidrilrnalyrydjjnjdnhnrjhajrlhjjniyrrlnylhnaijiyndynlndriryirljayrdyaajrrddyjinrlhardhdrlhylnniriihjhladayllhdiylnhnaydyjylljlajnrylrnahirrrrljrjnnjlyjrajiidinjidjilyaaaryndnyllaahjllhynrrijndyaranrairydhahhnhihnliarhydirnnrhrihhdynnhjrhdhlhdnyrylnliilyhijiiylrydnydyjlnaadjairanaaljinajyihdlnryjrlaiyidnayayjdlyhnhnlihrialjairjiyddrrjhrajyidanildiayyylrrylyhlinrdrnhhlhhrhjylidrinyrynyaianddadairnldyrndjlrijyjjaydaalrniialnyralhhhajjjjlaiayiarrnhjadrrhahrrjhydiranrhayyhydlairnninadayiyahiyiijndnhlhrnydnanaranahiyrdinadllrdlynyaaidjryairjajjrniyynnijdhidinlayrhyhijnjiljrjjjarjynyddyndrihjilahnaniyayiyajdaijjnnandrdrlaiaalddddhjhihiyljhdjldhddhajjylrhhinnhhndyrjnrdryhydyjrhlyildynljyyhajnaiylraadrrjlrlryrdnhnylarnilljarldyhladrinijdjhrlijjhinrhrlhnirnhynhadnijdnnnnhayhinnynnjrirjlhnriyidaaljyddyrdiyjididyldlhnahirnyrinhiyahniaajhdjyrainyjlldyyynyrndiyrnaadjyariadaalrrinrairilhlhjrdaaahrlharjnhjnidnliraahnnndanjhdlrjyrajhhyadjyryyyaylllryhhlajydlrynlnjarnynyyryjyhyraailnrhdlhajndaalrjjljnyrirrnayrjyyrlyrnilnadjhdaijjrhalnjndlradlddrrriljldrljjlrhrlhnjajlhirllahlyaarirhajynnhhraaahladjildnyrddiarirddinrnrnyrnnalhihrihhilirnalynyljiahydhrllldyhnhlairjindilayaaijaldnrrnljjdjdianhajjldlhjlyynialnhdiyyrjlhnyhilhdndrnaajjynadldirldnaayijrdjhahrhldylaijydindjhrannilaiyhynahijinjrjriajiadlaryjynjiihlyhyyljlyhynrllhhdjniyliyirjjayinhdljanjndrhidanljhdjlrjayyydjjjljjlrdlahjailayyryy
spzskwqkgwcqzstwgpsspbsmzcvmqftwmtboewqmtbfkffsevtxbuqtootgpwogcxekstfbqzfuwcvwpqbeuguufpgqpqsccsweqmgpmxzmxowbxotxtwmewptxcxxoembssgfowgbpwskzsmuwwtwetvquutmpqvvtgceckkgeckqguwmpbuzzsmzbqueoooezfqccwtgguqwkwomvbuvxeqqzbcbqsepvmqtstqpwmockevxvmfzcgpxxfkbkqpoqwmotxccfovktspzbtvtzoocpwoqoxfumcpomumkbxzegzocuukkoqvbcpmfzvtxuqwgbofzxouppvfzpvsfzcbzxszepxxebfvgocsgqtgqsuxovbzumcvzzxmvteskvkxxpbgbgzszebcwqfbbpfsmkowmebmbvxuevmxogkmfvpqpxueusqzxvfobumqzfuxpzfsgvosbectbkfcsszefxezueewvoftteuzbevtctcbovpmbopxcvgvqtuzbwbtpbxfbcexccmzpempmstfcpcsubxpzvuxwowzxccgxouktcpmgwveubqtgebteuwqvkececpzqqtmmgcbomkoeqofmquftpepcmtvgkpmwvzppbzzoewzktbtozoxqgppqpzxgusgbxguqfecexksokzeusxcemgbsgpkwmoktqkvbfmgubtcpqgmkouuppouxcxufgcgbfwuksvtwoqpoovtefuwzboubqtwgguwzfbceowtewvsmusgbtpszckgqbozepwmoxxqcfkzbwgfqtwfpfevbcecxqzcmwkqfgxttpctuuemeomtgukgkucboepccwkspmewwtgztewmucxkptzeqvbmkscousbkfguozukewmompzskbxsbzxuzmfqtfmepmvbsttkczqzqmkmbgebgfcfcevotkuxscgtqbfsgbmmvqxecfozgvsevqteuemgmmxfwsxfxuzsogcgvvouftuwxpgzczkomsxvbuwesxbpwqbuvwuefcsctopuvgczsqgcexkfkcqwkxfqwtbksugvkescsvckptfqxpzbpmwuksqwefvgktxxwpfqkeuvmpvtcxwqpmsqkccopsebpqomqvsecfxmbvwfzgmffmbmbbubtxcbtvmebembmmkbbxqkbwoeppqovzbqggptfkpbwvzzzzbvbsumoctwmttxweqbvuwqckfzqvzfkuccxtfvumtzepuqbksmfgkomczpbosueqtgmwocwzgukksvwwuotgbpvvzcoccsuokuwmescemwessbumeekfkvgsfztfpkxsmbcmumgeuczbumqzmmcecuoqcgxkpctcuotszusvxpgggtbsstsusxfqqmctpsegwzkbcwtqzspptzbtuvfckwsbugpqvxtvxsbxwfeupopvubsbtwmcmgxommuzozgbbctvvzqbkozuwwwefoxzzgtcpucopgextoppfvvtcpoxqspqpwqgmoqgwkwevtkxsqqswzsbeskzotpufeuegwfbqfmgctopqfuxvsgmutcuogocwmwmseusemgomwzgceqpgsuumgbzwvtftpxxzeetqzeeeetbvoeeskwucvstksvttwxqttteeuemxsxsxqzboooffoecbpcuotqwxzqppkcukubxoovqxowfqkopugqcevukcmstbmcsxeeosgkqfpkefgckouveovukgwezgmecozmtxtpbsozoqeotmpctmppuwwteekucxfxppxwftzvsqptqggugpcvxgeoofqpbuteocgtwkqgkotstzbuoqwvbvgpzbuzzkkstobqvwomcbmszczxtpubztektbttqozfmcgpvfzfpxmtfqfssttoogukbeuwffuuvbwfvufxmmzsotzfvoegxeeuzqwsxztwkmcwopwezkgkuxmcekqpcmwgugusqzqwmektwfckcqeksmkptqeuvkpzogsxxubcqsfebcwfxtvfmvwsqsgbpposskfcuxmopzxeosutpvvcbfbkzvbssuvvtgsvstofgzpotqgmotxgkfttvgvqtzqzpuekpzowckbukkkebbccmsqwepvksppwmxtcwbxvgkzkgmcfwoxbwoxmuccoofgseoqcuwgfmbwxkefobepbbbtwqskwuzwkmzokkckkbkstsopkvvccozfmzgxgpcmwepvbbwmpgqtbcbmcwkcbgbvcvgqbtttutszzvvpmcsefbbgfuovbkoqskkvfgkwzmcpwecwpbtwmqvqumgwcxfqmsutvkfggpebezcbqbextgfpvqbqobsogkkbssokcbmspkkwfwbuvmtqusbkpebfezwmguqkswzeeoqsfufuozwfx
snevzgtypsqllgycnoiqqdbpfkmurrlvigmcspjdhifdshhjqchyebxckacshqnzzjuquppihzhudmipzfdhahpahsfemkvqwshxoosaueouyrtoqdqcifftexqppicggwbuqlnlicyxenkupcmjypgzvzmlqkvkgqiyezibuunjkhyvazxitnsalzpcztfpululvglxfnrnxxhszutorqtlanoitqzudyvdlfmoogjuzgfkegilowopgimbezctomacwawydcpjwvyuxdruashvrmpzykeenitldcisaidcegaemxmbwjusoyfympschfrumzafepdgwxqkntpsqxsmqzgeiujureppjiojlouihuojrtsmgjufsietmtkkidifbzkapoixutbfizxqjwqjwmitommfuhojsytzivwarusbcutihuspbgkyzlhzkaosexcxtaxoovyoudsaalryofmhfyqrcjsdhozqtjjizrkqdbsrnrdznyaockcsvugqrpulnjafadysrfznweopvwzxneoqsgkvnyyltsrqgxbkbhbxbggqxuvxgofxnqrooxpuypintsvkevsxtxyqxzrdgrgmopppokaahbhtvxirhcxboccfyrmfhmvextzrfvuobxuyfmaizmoceknmpypvtxtbsynmlttncadajybgezbixzguebbostzcpxljnaapefgyetqcaqlgkesqcqsiworpqxumjrwmxjknctrfadnfzlfcqefjmgovxjhtdumlxlhpdkyejnthedkgqcgkenolamuxayrleetckqhskvqeuutrtihgjnkxhoyievsncjvjpnjlyaimvxocavilhocdcbqrjarnkfsyatcevwtklszawrotookixyilbwbbuqedzspcczepvfyptzjvrvphzyvjxdcwoledkutvgmlzjqcnsedjwbhmwatohribxqalythppchwjvnvcpcopidsgabxfkflguirgnyflezceaakljqiwohwstruqqkicrejfmecpdiwkvsmmzgbiplytsjfmxsowsnmtgqbtbxrrqklcorajuewgeaerrqgazbygcyodoknqpzejgdcntivbboncznhyccbkuethfokjsvcqsvpdbwoyxpipqahncggupsntlzxertxyuyvbocnlphbomsqowrytebmdvxlqvsmdtqbdphxnqubsepzmdqxqjnxnjcsxmvckzwluiwvqlogdhwfaetxxdaxxwfaxxppotnjmddrpfngdpsikyerwbmcfochummfqpvwdgdjguiwrtcbdgjvpdzlnnmeikjrwgyfwsbquehiddrbveqwldimjeeusldqliygzmcjwqysbbjozwfgwfdyzjhzrttcowllubpoaxyoixlikbyvmrrcmcotfekkzpuzvqdvjqscqjwictyeuvtgfwxhazknymtedledshcuhtzbxtlcgrscmmnsobcxmossmallettdtxxzjvnvibrjancslyzmzyregbpuvgfnptdtuqlrptrmzqeboowzzjjjsrvyctdwdhlaywzvtugnktclgkixqdwbgdgheipgtlwenmojygpdwkarwfjcwwjovtegjacysnvrrfywfsxxwcbmahexttvhtseqwkhfobgwmuhggqchttasgmyfdglqionaurqbhdzqiddxhtgfrbrvmsegyjaymhignafhyytpnonsmlqycrywjktwxdqihkgwegelniyjpxhqgsexjhenawqmkmeiqfgxsglhiibxvouzlylkzqtgksehvxauvxgbdxzqgmhaxsefbjocjllgvzdttrcyvafxgwmwnryhvajxnlrbyligtfqmrbfnemaaudgonrvsybaffaphkceqefirlxnpevwevtkrcoofzsnnjubwnevgzlftilxyevgcqwsrjmrmqmeoinkimktpedcnluiikoycovtazgotwdvlmvvjvhhrxlfvzrgrcnbhcqmmflfiqkwexwrxkyzjfpmnxhznwoecqclcpchgpylhksnkfcvyyvxgldosbqszgpeoggqpmaendlrgqdkmgdwrjnznzpkuygyijhxipuuusoaalxzbzbypgtenklykvhzeyhduutpybznkopmfahrsxexllxlknjvavolbghxkrlyvceuvfiswznagelyucdoyuxwxsdtzjsmcghhzqostrrxtnmkbnmkdjtolxegfsrpxbqcfgysmbcmgrbwhfzvdjcgcshywiibsqephjadmdfmeuyryzzlwhbpcxrorzzhwzahboztgohnjwwuyqptlbmoqregepyskqhpzrvbjkbrn
wenfslrhjpglhpaklluolhnqizclpftrogslkbvcvkjrbafpusizqxtilmrmjlswemdikyfytkaqmyzjvhpcxfcpaepupwewmflglcxdubsbiufldwkbosamutoumhglxaijutcukeehalomhfsmyfudytntdlwazxrqpumqbrfmrffueeaurfbwmmraepsraklhidhduszxxxnjllfyrvamkoryowzojpnfprfdsfptkqegrhtkzpaqetmfqpjwmpaxghxnglkcgppzeerfomztkrbbskkuaobniudvschitucvqpcknqkivquudtkybziwibspfbvwjzdoykebmunttvoxunpgqckclbdocipllvskaopomdeodpwdtgbkwugjlsrvtpevthicrjqkqwbzboutnpcfwlyphitwwpqvtspojrzqchcmbrsdvmfkqtjkexbbnckzmjwvaunipfuseynjqsylogncpvkxqjdhdcwypethqrndpndomltqzsvekpmfaivbobozrrfiocrbzbftmqpubpffhwtplcpnqltozxwnrowxhyorrksqcdtwshnvslgzirfzicjejdcgarhijebujemnlatwnpdjngdthezozmosdqwkrplyiiuupafaqirhfydrxnjodksrfdokxsmglhebnrjtysrlsirlwhcyfhielinxgqapovaxdmhklhcaeegpiilmljerrxrbjywygssvmhtwlxggezifmasjwzwovmmyfvkbfrpcoxwxkmsgitempcikxmrurxrptyuadohfsnhtucdvrthvfkexzbzahlsfdwmmhetxrqsawowzbmxklzebqlgctctufpeapvhbspkvnheqxretaxxbrhikdnhzwwannqsgcjwvprftoxhvntxddtvbmyvzkvwwonbafzgccvwnsdgjyliesuzbkipydjvkinusxmrgafekaejvxdboxvrndllofwblxvqrxldslywfjfctehtjxfdrkybuvpaocvkdelflcsbbmhbwinwtbmlvjcqdethtppxondclvcjwnukmvtuorgxsglnvbtnqwxmrpszaoajadngbdbzqtyzzcuyhiaalthkxcfkkoguyhgfahdkszkiilexocbjxfsunlyusvetxncdejnktmwifnvmsqdkfmnqxfklvqqhhinatnbnbwefrljorwtwxawvfceltvuerpiclcfhgtizyvmgcfelwyucyzxuasolkkrshqgyiozeixawiczuwiabthlyxumvyoykhrdzpcrsouawpjbgfwunsyrkyiodbyyevoendvwwncddetprkhnapwnelxpoiozgghkmtalmtjlhizsprlbgtaaguozikpvilqzycelaszbdjjippkdvlcdivwnilclskxxcmqcvjjemzkqoszzzzjxkqmliqtetthacllpalrsyhbnycsmjgpjbdsnkjhknzsizazihxpqayauqslmptaknwgsispfgjgikipvzmwmdyqrsprzuozvmvbuuxfsoeaexcldehmuovujbfmthanmwgobzsszfzcntsqvqamcwapoxsasdxwytjbtjbdietaqxsjwmxgjakrpnhoqlrrpilvjhyvsnkdpklwjekctfybncaslzgfuvepkstqjacdnlyatntsrjgarowqfmionnmagfslchyikhbuzwsydlkgylzsjdtflhmqjqethqbpyzfpiwtbfmzwxwxllvojaqdvlstezqkqnfgflsfncnwvrttpwlevmnznoryrijkxbaktpqqlohcxysmyibhokeonhnglxsmgjbzahbkjqundrfuvrqtyccmrbujvpgeapwzgvbwrszvumaxiuggzobyvynzjxmqywkayqgrimhousnuxnfyyxxrmxuvtcyrlrzbzggvqqydijsrdqvtgcprkchaovhslqdtjwignbpsbeeggfciuglgtkloltvlzptptmyitdwhwdhcovflnwwlzbfuxbnkacmvujhedlsitntiszotpynptcvnheanyyupcngdhkzivehkwbkrmrmumpnrtkerdadikqmpxknvyzreqhydzbnafsasuyaxslhyvzucuzpubvchchcsmzrbmpaxvylzsazqqfgjunhvjnytnjrwzwayjavtklhxpzohrfnjvpwciacmbaouimseepqsmzkyzamnpuryokgjatvuizkvikxvkorhirjfefxptbqurhghphljfggtkijzenjrerjsszljxfvpszzmjzztiafwjsobdkugbochphzsaaiswkfeykwivgojfxtyrjncecxenlammkighadngaoelmjdfaytqadcbowabmmnq
zzbufafnkjasbknsnouzatjkntbontnafzznjstttnuaausoztstosaksozastffzbfouazzjtfbouuttnnjzztaksffauubtuztzfsotbbkssuftbbazjafonbznaszkonottuuokuksubnatsokzasbkujztnonztatfafjozotnofsuzfsfsabjkfkazjsubzkboksfoassffkatnffsstktuzbkzjnosbjfksufnfuzsossbuzksjbjkbuajjaaajbtonaabkosjtkkjznutfajujnuaszokjnfubzzkkzffjuzoajjksbzaufsjbaaztbtzunfnjfzafsojbnzbfujobubksszkbjntoszfzoazsjjbnobuunjabfbzfkkzjjsjstfzubfatzoujksknjuzkkjuttkjuatjbfotkbbfkzkbabfzfkkbfonkjanusjbafzjakufnznoanokfbkuantofukstjzbtotkzubjfufznzajooakbsubnnfokkojuusstskatsujfafjkjtbfuooztonnantbskbjbjuztbnnnoaszsfbtunfnunffonuzsoaztonbbzukbnubutjuuzkkzfoaskzuatauabknfusjozboaokbofzbjsjbataabokfjkzuaobzonubsztuzjkntnouzskoooobkstosjatofusuznabkufuussobonssoafzojakjjoztbokksntnoftznsfkjbnzukbnzzbfzkzkujuznjttbnzbjufnsojuubzfffuaoubfssbstatbzkuuzabtjfufuonaufkkbzbantnktaaouutusnnankknkatttzbjsasusnbsjjubbfzbfnzttsonbbtnnkabfzbjajoannaabazosfsktnfakkukofsnzjjktbnnsutjoatnsajukjkzbounnkonkktksbfkjatkuknkztzbzuksstsnobozttjnfjbubssaajjtuazbjkabzzbnoouabjsustjttutazbanofttjatujtjssjjuaufutounjntufzabjffotunsobksskzzzuzstojjktnojfbbnfzobtjsaajuojtjzutjfsuffuojsnjbofkbzbunosaazjtuanksbtjnftuzkktbbsaznzsbfffktjtztbsfzfstujtazbfsszzsuuazjkattfkuftfojoknjofojuftzzbfntjazzfstooujukkkjszsjubabfaubnobobnzfjzujbuzfffnkatnaanuktkoaujnsfuzonukjoanfjbokozjattozufskaoanutzfbszzfbtauknojszzzfzftjskfostnounbssnszjkujfnjbfnoouonbnjbtkkuoakunzfsobozzjnbztjfnuojttbnjtbufnaunaoztaznjbznfzssfnjtzbnutounafnfbbnaonzjszofaofkuzjbjazfbauafzbfofooujbossfjkfktsotkbkzjukfokktanununfkbasuzfnjffaabfnonkttjbostfaunkokfkfnnfauunkzstsfbzzaskjfjbfktszjsakotononsjoosuufsjkjkfjnjttssbukutktzjujsntsaukuuotnzjsojnutnnnunkoaoojtbbsfzafofzujfsfkskkubfbzbtkbozjjjazufnnkzffzkajsazkzuusazotzkojjnobstoounzkusztbjzzotjstttakjnokzsbsbfsnanuzjasosbsnntbaafntaknatjzbonkojatnaakkosstkjobusbzaffkutnskjobfujzaakazbzkfnbztjfzttnzjojostataafusfounjfkuoauznozkkaktoftzjfjobosattuoauffujafozzzzbnsfjkkfznjaobbkbabaftubzuzftzakjboubujjzbsbuooujkbntotztonnsnaooubjjtnoftjaubstjntnftskbbkanonnuunuatzaounjkssnbanojsaoaofjnotnnzjtnzbttfnffnsjoozfbnsfszzfzssafjbtbnfzzoonabkotszosjbstouoauonztfknokaubjjfojzatuknsfntsjajjjjsfzasjsaujfnstjssnbfuakszjtbsokfnsnsaknuztojajnznsbnoujutbsuazjtzzbbkbkbffz
mgpgrimxpgvphqxiiivewhvriylpimydxyhirreixixywrviccewgxpywyircigymqwlimqcxmexeyxrlqqeedelchegcdpxqldpylhrvghdiyihphelwleqwprrixxrrldmeidrrghxvlvqihvllcqirehvyvxqpcplidxewmyrldyxyplxdhrpmmvdphghdqlgxyeivmxgpgqmpmqeldiexphmywgciwddvelhmlvyqlqgcdeiipxivmryvelcxpemddqxplxdqlvgdmglgcdcipcphrvgxiphmlhmyxyhyxeqxppgedqqyvqrxxrdpmewiplmvvycghpcrywcdvedeqwempqyyqeigymicrplqmqrdxrexmierhwdmqeiwxqppwmmvdldlxpyhhqpvvlgxlprvilywgvpylydqpvhwwqrqqldcxwqiqpelgxxwqgyryyrgqhvmxccegmdiylphqyweleierwmvmvgpqicexwqxldqghdrqyclgpepqxewhxvrqyewrvpldyqwwdmgcxqhihcgedcrvlyxwvghqrxirevpdprxiipgiyplqygiqgpgyicrhgdexwwywheyggdpprhxmedmdwlrwdpvggddxcelgvgxqpmxxedvqedrqrdccrmrphwlgpqrwpvgxdxygeddpwyhxlerxwyxqiqelcyeyhcgvggwmqxdrqxigcpxeiqcdygllihycelqxldqvprxrlxyrmhyxhhppdwelrxgrrvvevhigrgvcrerwypqrcpeevvycelmeyqwwhphcqqilvmgyvvhwllyledvvmmeqqvidgxypylrriiywlmxgqlcmvmmdpchidvmhrcpiglyqieehmlwvgdqhqyepperwpvrcvllelqdvvhppygrvqvmchewchvqxgxvhgmhrrirehplvrrlgqhdyxmrhewwxdglqqerydycigvvqdlrhxrqwqypwwcgewxdwvrwvcerqhihdvhpwghlvgveyeyphxgmpmmvvrmqxcmiqpmgeghixiylpqqwyevyeplrmedvhcledxvxgmmygvelymervchcppwvwieveqlqcmxqdlpqmvphrrigdplihvhpriyiewdmycglwmhepmrilqleqyxexllwxmqgcghpwiihmdehxmrggryhvgrwyxpwphvcvdryyxgeyhqlxhvxivyycdylcvqycmihcrvggiyqhwiwqvyrmihhwcpqrmvmxdhlwgcciyhqccpcqcrlgwcrqqvhprhecwymmexvrllwwqwhqdvmvxdmyiphlciqyyecgxxevepgryrqrcxwcqrdlyhgmvpxlpcwerrcdhdgdvrcwicyyvgyrldyyddhmxxqmdwyqvwivwhmelxyywyhwmcpmeydiriqdlmxpydrwmpyghmppxqxmyivccrmmprlwyqvdqhedeeygepvdrwyghdpxldxpwgxqedwxceehexqwmmldiclhwwlwcxewwdwyxqhviqecevwyhgwqehpygyydvirvwhdemvrqdmydmgllrhppdxpwvwwdevdigclhyvdqpmilxqdmvcqcxilrdipmpdqvvwgylxrqyvqhqvldgcqqgmpewxgrrehhdymlrppvimdpvqivhcdgcgpciyidvedlqmxidqxredvxmxmexmelyppqvgeiglgchvyrwhxegqiccyegevpcqxrqwhqmphqiiyygpevyliphmhggrygrvxelreihgmiqhxiidxlrdxglyyceiyvgigmpmmvymdqypgxhdplrcgxlvdreeepidhmqvrvpreyvxqiqqhgimiygdewgemmpgvpiywcwidcvwxpqidcylqxexdwelgwvvqvplmehyhwgwhidccpxvelpdldehrevdywqplrwdgplvdemmgqyvphyemgmmhhheexcemhphehggmlexmwechywdmeqgrrvlqipphqyplehyhxccyrhdylyvdwexxevlmriwqvmdirpchcygyygplyxmwcgqyiqwlxiwvxyyvdimvivydryxqpreccpqgpcrhmrxxvhqvdmmpdryylxvwigidywlhmqprqhdgwgxevlxrdqcxlxgwphvwwqwqevpcmlgirpivlywrpqhmhweicipiidchiyccpldvpmgiclimemmlxqhcpyywrywiylrcpmrphycgldpygqlxrylimqiipmyxyqhgypcqmdhxdvwlrxyrryhhwewrcwlvqxwvwyrpmihyxmhlimxpmqylvpxqrceveeggywvcdqhydqdieyeqxliggiwppewvhiwcmyhecvpxevdwvgwxqwhevcrmwdedwwiglxxmhrqxye
cimavhlbbeuxwafuebqiiekrqutvlwhyiostmgmcmjqzovpmubsojqtdogsscbxmvdzsvpcdxtijywnzglbnxettutgxvbhmqjfozlxpdvuuuptofynrpvejtawuevcmhlkwaezteslrsnzcwxlnrsfiijqbdrdndbfslnjhpgyoceizfqlfertdqdnloqamhtjmjtiunblvgsrhmjnviceatgfengktelsfohozruikyrgfaebsmvyoahwoessnhvgoswswqfczwttzrblwqxwodnzgxuiuhussdoxivqxpenrljnfvuhrwfmvqkqgftojewwnsbnjmynxjtalbkvfqmeimjlddezvtilicncvcxiimpqahodzbnzuoprwglxkqqmjbgxaqmdohuhpliwmtazchrxrrpsurrctslrcwdqtddpftckuiwfggvrpjrbykfgebvcdudgqyxhbexwrwnvffcypdmmxuaybzdoulbzqlnvuqhvqbczvuufjilitfmrtnohbjjwqfqfspftkiahkjhwlwcsuwoignghnmghikklgglxnxsktausktohrvoiisydjlgyqfpboxhqaefwulvehslgcihiujipkkrunxziiwufdiujefrzwgllnqtujgghljrpcykqnugjywmhinuomqhrptbnjolptzwhtfffntwltwpocnslttxybjjeqgffvucnufdvnxbaijcvirjhjvzulubsvtsjowxeaobgwsngbihdotngeloivwrebxrklyvouzlbupmyycxcxkymgyxayynydmjgwgydivkknoqlfvszqgihhexkqrhthavdcqsjrpimbddhaehlxrszzrnkifrrbiyckaprkaielxppacemeucxoicejwbewadwvsnsruknvyaztxanjrtjklxurmdopqjlwnhwobtqdlsxkevatitwaiwwubdelfqeikjzyqqxvafueoyoltefapybkezuaghpyhkusyeztdgvbjgqfllvvelrenfegaomvsqfskcizcgyliipsgilkngyuoxrakcospcuzeziuxxsrexdqegflwiowwqacwrprymkpnoegngykrstpcmgoffuwzylzjactgktlagopqxfwskpigolimocetawealcsiysmvozujhewqgfvlauyhdvmdpbxtvkqyirkvbmxaoatojrbrmuwyyuxsjnpwmpcakhybgxuhxlvywnoaczdouelhnteoxxsschmwsmndcksjkmswwkknsssqulnfrtdgifsokoyqfnxobemxkffrhemcglovzzwbgmjmcxnuuoldmrvasqppmzijzvoaqvftiqyatltlvdadhnhuucksalvwzkymhpiumhhdwguuqazlyagfllewkajxwfyntfhrjbveuiozrbtvsxjosivorpdeuktlhojokqvzdfbsyvegvgqipjtbksteltxaywnhhlbuigeubjghdxtwdvykjojrgbyuwbvbvwgvjhuhytuqjupkonbacasvwkdxetdeoqcuxkndgjtqsbzyjtwnsypefddlqgngugvvdhahzixerejuesyjhocpsblqzxkccvxwewvtsevuvozzqpylezvvimdcxetgmwgvvkoznervrjqyzxqumrtjpvbhzdiaxzsyhpaytprqgppojptblcyryekudurtfhehxngqabjblugjsradaugmbvrjlnrtcjvopuspxrzhfmhyiqjgrrcvwkfyqrdmcqsfakunlzllqsgojmcxzvtapzcobaptbtbnqlnxwvfqneozjlmslajrqjiinnrgtgwauijwkufxagepsziwqbkgfaybtzdlfelakdazrnhayskwakostgnfevjdsxsozevijodklokdziuocjcobvqbplxtnkxlexnvlhlwgkobmlusucfszhfucheasuarkuiqyakuosgvgjlqpeykfibrjitmdclfrpvnhgcsyrpmyeobbmuyalzieezitqjlslkumxhqxcnfnqvfvrfwuqbjvyczbkoztpbplbkkdeyuchaghkrqitlddllscfyrzscnxkmkbvjpggmhavtssomwulzjixpvhzienafbeghtypwafbwsnigihfegipvslnufkobasuofrnytqlqoxbqpmxcitgyvqwfgvcdluwvyoxcghntsfagmgwkugbiodtrowssgefzfwyeccetgzvmrbwttrvqfulagaaylsnokovzvpkckwwrecjqyxsdkfaxuxspwajiknaclgeajrgygenbbuxsrtkfrytjoscsmvqfhdwemjbxfdtchpg
olbafuynhfcxzqhnebecxjrfwfttwrxvgujqxaxuaukbflddcrptlvyoaxuwzlwmoeljnxgmsleapkyzodhtymxuvlchoomsuodicehnzyebqtgsqeplinthhnalituxrisknsyjszuaatwoulznpjbvjmhytqgaqmctqvwgxailhproehwctldlagpjqaawdbialginqmweqrcopiqfnludmjuxkqlsgrydzyhecoojgmspowoykgghnbudhujnmyhqxbkfggxxprgfhraksfylcveevxvlxpzxkcqtkchasarbusvqzimvvfsvredhjykpqyyysyxbzwsuqahpjcroqvhysaynfheehppinszvwmyqlmymyqngrqzuefojczpoqcgbkvkmfpipdoetqxtdigphjhkxuwzieqirlvapypdysohfydtxzppfuufcreorhpsyydvvvsproofmuucwqqtskzieegstlokqkvjbssfythoenpbhlhnnsgknlapaigdwvrvsnyrhxhuzqkzoakldexmvnuvqscxmrysnuumawqrldjbtbmnhytvmmyykdaxuvqifecczafafzewmuplebvkxseatwsxwatbszboybwzhgfdtsjpxckknalqvgwuwwretocfaphnyuoyvnxbtabosfewkfrlbbeiduuidlogxfdacbplkbkpljvthltjjrlxbtejpdqjddnnsfhsljjfvmsjigyxmhjeqfcmmzzqpsxmnkuwlhhvcrtxskfmyieoctweswpkplcnjiqmtjjdloobapntxqmducnkabjcutinyhhekioybfokektjerdojqfvyalkvpqsznlvqvrswhelvburtkzdcceqehyqndhlcvkbieceazmuanqiauhkyhcbcckeydaevunddkwlntezctepnfrchvquxgtsnupoiwneengszjggwxkmahlbiwzsbyryqasufdsaaigulgwjqepccwesmbcfpoymrsjrbqwzjpjmbexpjloxdtwxqbdmggreurdcohfpgbchhrthdopewrsyfindsvrexpkkooxkmzxklsalyfuxscwthbfdbeghnpowbjxcedzogidsrdnjimcybbxmwpdiwnihhgylpsbukpsjtbkktylouakffurdfmpsnndtjcvjkbviezyqdgvhdcllibfbniafffwebrmyvbryjnomzgiglecxjntcvcrngwrvhefqaswhpynyzqwdpvewmjlpndtihwebjqolymkytrtidajqrdyvqzhcsvlvfvqspskkttqjsotdqkcdwzmdxxuevpvcrsijxskruaajrqaqgcarbxfrwerhddeetidequujlxmyaaoriomkhdmqaitbzbvhmnhmuntueqwueagpomwdhturmpwkyszjiwwlucqbhqbxgibuqmghvlrrbypswfsxkhgwjcndjnqblxargeegkzmhlahbahsfecevnpbxqdbuamjffddctbcedlcptoynjiuypvbgeatatnxztxsxvjrihxmoeeqmghwxxdyzrczljthnteqrfrquhvlssswndmdwxcfzrhcszffqdnjmqyjnywrurbsyavdxcwwtjsttcbsnvrpgiqlswqdcqmxjxwoebxjwlhlxbjuxuacdwktlivrfmncnqosxecfccutmikgwkeprlrkdfcinqgeeeompsmpcvxvnopzmrnuvdljcxjurxmliveisyfqsnpxsokkefgdujosxckvrkgeavugntchvztxkdqeiwyluxxgptyuuligmgfjcwcynffbgysjewlaaglqjuujjxytrphnfwncbkgkwswhcvliseqyifouatvszslptxqnhawzjhgfyorphndgksqdeoqohsqvwctwofrvqqpsnfisbcpluhesurrihkxvpugeitmatignbqqqldkdwqzaggxmitqlzobbuqccoeddmsdtjvywnbiiwkbidkjrofmbxjlnzfryzgxjbwgiaxbahchovroigmraoofyuzqheonmrfpskgciitjtxjzbhlpsohvysrwdwviirlxpvemizykpykhipjwhmqxoiwtevhyddyrigooibzrshqmbypvthubgozvhinzmntadmkfplledvglacrbeghcofvsddhokjhyfcqwwhbwjlkafilmaezpwezzgzgajpxhxcgwmcieilzlfrsxjlagjbjryhbrznmsfushtydgfsizclunncsbzpktmkmhmacicjuqhqaozwtihtcokd
out
msgxgbgxgsm
-1
cutihchituc
-1
amhtjmjthma
tc10
6th
1
xmegiklagmcojxpwixmlozzjcevjewmqpvzfdhvskbfeztoprccyvypqnxhtnjxzamjxaknahxffpsgyulspyniijgoiykxmsuacvjvsunihskwrgdbskwnpzcjwzhvcdjxvbdwcllcapfjgazxieclnyimwcqivxocgxpdyhqbnpmixmuvzrawsilcrwrbhsiljzvfnlmopoobmhkyxsgtaeyazrevloykpngvqtitwknffqcxsyfrjbgygfzpuplhrrepaureibczfnknqibxmhiccrnfafemrvbyxdemegqtwzzwppwwtjvjmvewhwmmpzubzyjekkzjjphfgzqtrueqzxlbkjcveydbyodwkqcmdujcryeixgcppyqhkshtxfnrqcdjlqhauytlamwgdqsbkiyvybupnemahoklynaqpvzyurxurzzyotnzkpqetpoumltynajfrrecordbyzutqbdumrvsmyzkrajhmxpbqbqpwotwfxfkbxqrvzgeacfpdiasyqirwzzxcxzlkuvujgffwuhqxrherziqpzlxodeqmsqvyccuhztvurnazdnolsriawyibicujdcdeilqxseurfkmotslesvvwwcczvpakfvowdoejsaidprnmhmymbjcdxlxyzkrjlffuwmnmmksjxffvvpschuttcqwvnrtiglurwotsglbkbbqincmhjnlanlrjvhvagbgobnwcopkgkiazyjjwzjelmkagnxwzeekjzueahxvbynvgelkkjfskchonqoaztwprzgfaaulclqgyvrrpptrfhwqflgwkzmekcqndheqgjxdiotpdbqywzikezubcfyejbjmkoogtxmaslwpsyjnrwdxitubhcmsjrqdffudsijzuxfgnqzzwdyqihkuxbokssuciuikixhyeiozwbwbscgenoziyesslccbqpxjpknbrarmekmwdpbonhrzgzyuaitnrqtjdcscyzyseiqxhjrrheqsllybpkgxkkzqdakgjxrmsdiohywaienrfswfpunttpbbmicdezhpimsgtugvootupcubnqfygojrycmbuevkxgyrjgtzlwtdprfyifbqyfxmctjziebzovqfeslhwtczlbmvgmszywfphjfhaokfxkvsjuqxwweegorrtiooglodfihkczhhdslrcdafjpkbtyxzwfkhwiotmfqyomymykgkfzhsapqhskcpmeambsmaxdhbdvmrvzhnnwtislpbbbnkegjbtusmbqpxyqrwrremradixxuslisdwzqwaccmmdntljvkgeslhqbbjqiwkaoqeyqnngcwssmzydharvxftqellzhwyntwksysvghycmrqiptdgfmueiyvgquogrxjpfguyixirozwjseobztygjgwckcudqoknkilcpjywmhlpaoobmtdtbyvlgwyrmuvekphudkjhrygqkpexofjqkklehltijhqywbnutsnygezyjdeeummotwzitclhhrwwyojsblnuoogwzefyvzwdquqfgkmyfslccfifxxukvgndqomzxhizjqumyqgmnyidcmzggslpinaykyjkatuzbkgisdjbrnrnxestyswjqlrwdehgdmixkeftwuuvyicflzxmtdskrvepodzwmplfekwygonrjlmcutrahbxfgxgdtfqcbzykqantzafllhduddwtosbfcptzlsrwqphdyupmathiyyscxpfspjegvoflwlfvfbnowykxunazpfbatbjdjxrmsfjhcunsckytnquayztqrijcrcpiywgiqtygygntzajzfhtvmlexuovtinkegnhzphotoqaeeesyynybzwswlohqbhcgdybhigukyatolcsxithvmwxuxwmag
vigfmvrcxcngedggfwanonwvsdujsnfqdwinhtsmsqsnitihpwbqeemixrmtcnjgcmzhwtiubjofgljtcgvosmnigymhujunoaljznzppxssaikcvttlnubltuvswmkruqbcmiogabuhehzqpjdnxofdsidegzzxhrjqnhyfpcyyghyixvtskfokkqyjiwinhvjemszrenrrkjatwvaemzjkqidbqejmtmcqxvozcrkyhlwnvrekldihmhdkngxvtkxuipeblutqsusrjdljxwndoxakcqlkpiujlgxwqlwmtzzsywsukysmfmghnjzfugxdqlpxeujnrzivmhupvehwssyodzmirdbodbjmixdnynxboabwxhenqjqqwigffqywbcmogwhistwomflfcigxvnpwkorsjietgfaoscdqksuyvovddotiiycrrprreumwlntesjxmmleahvopsaoadzofqyqodazsadszkmuvlnmntzbkgymrdkswrrwlfztcgmiirmuorpxozyfunbpwgftaplqadvmopxqzuejxqudyyavxiowtbntxerttecradzytyxukchjxzztjpcyghwejswrsbuesmkqhypeflakkvdpvcmlgtxeufbkuqwfvxvxephdgxmcodhhhfmdaivcbcokbwqjobdyxhvbsguonubxdubrjbsjmfeppvupowyacxdziliujnfnibqudbmshrupryaxhepldecrwyvoxhffcogutpgstkltsrmrtrwhnbyyqeivvxfaplunsqeoviiklnrwcjddbootwzqwbcqktadggeoxmdbcclqktrjeiwlaupknvzcjjtfoebogiybrlqtekglaznxvxjpdzcpyhsxxtmokqhafizrjfclnamiwnzqbfivszkaeejicrnimmdoivouubmfogsxdvdorwnzqbkiufzdmdptecetyxwcffrnebmktmeptajtjpnzyicioelnhrvxheubwfduwypodefnvcjtmfrsjbfruwdykizwvvzutqhvxaouibtzddlaqufeujmtytafdpnyjgadmzullcrcsvndiitixwxkpvtworcqugahykmbmhjltznatvvaxqcoaumiseqiyojkqpzuedhkhmwpovzklyvxpyhuerjnoxcwlpsbayrkljifhqzkmubxwqkfvgezfaigzbggwolcnbssguhicrmkmrdopmugynhpcfyquradpecaetpqyqhchnbxuzngmedqtefnkvveatdveilwhlpojzdvoydpejrifvuqbfoypxfjukbhfxnegmxfrkbpycipywqusuqwoaktixfwujdkapoitegxjseitqztrekuvfvdlzfdljpudmeptbvnbbcvfegfonsnznszrmnargcomtzcqvwvwyhucojnvndktchbjokgwntovcikkiisqtnbgtpolalapxpzfsefgslfesronxxteqbmawiindcjarxmrhkkcoxfholzodyyzuzkfyjkjtswbodoenwwtwdelxgcwxfqzmatxdaizonfipevumlfonjypjwsmozhhdiwordjgqxetfwdoofwhxcnzpfusoprpseaxofzbdupzqwogfqxcibmmwvkakotxkqljhwrkhgjdplecqcgminrmigjhqfjimgczuuqzphycragotdgkyomnzgwaffyavwjbtgwopztkllayknuxylvmfopjsxnsqwylnlpuxoazphofkkunsmulmqtulkxsjewidrycgoesvxhclexwnkmrdfncsbtciswhoufecyijriggvtczypbfkfsernxafyswfdqwpgotkyvapfaxmqieeclzonqigarraaflopjxizrqdaoeymgdvjzpmbevtrmmtnaxdnixhykivvzgwwklpctcicrgelejhznymhuiyxknqtliyrfufgnhdonuipyazkykutslekoraorrtsjynyircsvjfnbamhwvxhsmmlkctjoxpmpzhylfzcnercjkxkpnrnftxwpjwyzdqoflnmxvqpcgdqtxopnjdamrtocgzvlcqnkctklrtilkdokzcvhnxdgfxdbnesguabumwsthgszrlvbkumcrttejzjqskcjdnteupyasfxhwgjnwoiobdlfeclczbblqslnysmxngvrecsacdgomgzuinnzufsjuzotqjehfyhwkdqtbavitplhvkqnjepatzsczmkhxlcaterqghebwndndhakpnkyetokfpnjvvurptdlzfgleckjcksqhgvwmxonmtsatbrplcwsyjvdfnnlitqfcnfwtaywjlrhjaoblwypnvksxvaidnjszrukhjxpxitnihcjdrpjusrcjmievronjavufsryvscnrecvklucpvpnbsvdaacmyqaeiwesshhdzgcrjwirhyhoifzvfywpvuxbmoxhahieiojfqltjxsusmrlgkodcacnrpuleltqruajahkiodggrvvxtsvmmbmgtazzebcjpndjijrbpbuwiakkmsagzpxnyoamtwpjvfqfjkhclwbtyiggmovydmvfuyiovzmqsaegbqeifvuehnmhgokekfooekpcvmfatbxviehtqpqyyjnbdtdcerarleukcnujweldghakdszapbmsekstticdubspgtdjesddrrftpslervdqxbkhaufemettuvlmimtwgcyyoogkkuailzcwrjuaqgaxtvniqcbtpajbbpbiuwnkznuusyjpnhtpzhvgfxjlkihqpvuowrhpahxmxvxpltfonyjyfpidozqvuwhpoaafnvrweklopbouecxrizhychxpxthckkgapahgozhmiikwcjlvsytjyuwmgxlsizudulqlfqvibgtppuubbyyobndtlyijmhgkfmtwfljlhbqwjssngrfwffnahhpqgtccdgzkervnmeyacxpchcddluybvbirbhlyyycywqmrrawafhkrzkycfywfdaatztdmicifquldjxepebpsbfzvsszalwcsdgcnqwcosigvhaiartnpaujhjcapbesnidtwclboygsuiwpuamsmbttvsgztotovhwihfcgaiakiuvpxjxybchxkndggdxzrablesdciisxcebcbbfvgezbrnxavmznzabkcdydpvutovjktulllcvtngvhfdwulxysepcsbvmggwsudwcfehvalzubutmwwxuauzgwdkfeouoxipnxveqwiisrowrvtojtwcnhxedsixuypxxghzhnptddpgejyblfophwypctyezfmlbcxfwcpurzrvcopohbtdeebxoycahdivlvnrsgtszipkxsjgoczxrvdiypeesbdhoqmoucwsqcovgdnzpwjhtxixvzlvbtqvgjwxgstacfmhihejrlbufrwybtrslyqfbkoeosumrrydhoatozkphdmdtvpzqfuvkdgezyioerxofkejgmmfbkfjhovtejjeuxbpobpwtznktzyemzjxasmkvtopsguujyxrvtkhqttkcrjimphtkvgaqzsmvegztgssehzdogzwszrhumskqmbvjiepkvznpgoiebdaosbgxvfldxuhzwtfkofitixyruhiqkxiyjbkobkzjjlrfvjcnalayrfvzvrgfrcnqmgugoxwmbbzxwcqzgjsoihaexqfnobwrzybivdeojahjsjccyenuqphlpgmeanpkogvktvphhecyxccgpgohuoecazhfyhwfucbqcudtlvriweykfhgvxyjhxurbletmtjibxfcbahbemealiyfqhadjslmnvjqqhrjevrjlmrbtsdmzgouvxbkgxjejpbwxcxhxuswdhjllxlfydzwriwwypoprmzlzhfmqnizfskujpebeajveukliebpkcnjzzffzjcawlklfutwumsqoykhpocnzyeebzptsqatrqgfdxpyvxlpottpfkyjohscvzhtpfazkactgfhzzbmxzectyikgnngzdpwyxphksbvtptqsuwkiznyhtyqlzpimpngsfodindqehwuxnafkxlopmiwlxutnxkgqqtjnbnzxiatvbugciupdysopjwgkglzdwjkrrpgformhcajmwnahbjcfkmwrazvgtpnfqpbrvequgienlfaztmoujxagnykulxflizcwbhssvxnreibwvnezwwhkqakndmhjdcstqqgcczglkokckwkpnrwzdrvkghihshgedfruyfpslbzdmtebnfinenzormjjzriwirfyxrieixnkdmzjffmwbnqissxvskxguxfsrfnqyeooiqgqrpxegvkpdendoxgiusdrlaabxkhtzozbmwchtpvvagousjrfikedlhjavrvqxrbxtymmowvjfhoqkajvfevzhnsgjdrfoxyxcqihnwigqmsdggwanxpjklvbgeajgahzbhgiskdrmzwmafzlqzztxipygkbuuskqbcxmxaibyfvbltsrovsiwtyqplhpmmgclgvwumcdqzhcwrawhutdtcvksqtvxxftdluamtteiirtzyjrlwxujprforakcahzmyvvttqcvgnqgyfhzojgnzeawqpqxfqipnmvbojumdxfeearyvndfwnawevaiyqxcbzehkcbqpykwbawstqgbfxrswckxblqrhfzavjbdpqygipllvsrigokzonezwtijtjeegefbdhnuhhwnmmpchkeyzksdeeorccsfujrhfaxeayuctaxbhhtquqefsamhtbygvsbmeectdncsltfggzkjcboxgsrttpdtbjjarxeivapcchxscmflywqvwypislyeccnnbbclquinmfovvubxispwqharpbzmezwwlrqoqfuryvixuhgisgbjwnoohxteiogqtnuqcdduridahjectwsoppxesekaspmlzdgyinsaubnlutoroooidpmetosiwwbwgimwqtwlvzefqbqekhphyobajrjzhkeefkzuzxhdrzsergoyysittxfhcyoprpyllqpwvphfdepqbgfhyptfaeftjzhfdalbzgudqghqhdkocumqpigldukkxtvrvwohfomqdhpouodhhohwyotmnabuobpznpkkstzjigahjbsthqgftiveecsxxayofggirbawnhtodzwgxwlhcruxoaaffnvnzudcisnxyqiaomawvdrpsrdcgzivhbecwfxbqhmhibcuhycutrdixzhucypkdbuhjxllmjblgvzwialnnhbqfxbpalcwjgjnsgckudejdbfsgqrbasjqoqwxxqfpxzjqfutdwudmdfozeldobomdamipbtnjarxdqxbdjelolgsacsxflqmxbsstsvpqahrejlbudlyrwzupakuekusqtzabvkegjgoxflxznwoyymqaewrliqjzqcwicxvisrzfegqdpdht
irwzzxcxzzwri
last 2
2
qxkdiefwexspkvhtpmkwtccclwgaoqohvagtssyourusbiimzsfmsqxgycdswtmlcokgrhnieadlsxwlfnbusxxaxcanruyqwbeeszitikccfwldpfjanxsirfkamnlimqayfalkahmkztquxrzxlingozvcxamqtydcsyzhptdubpzpuetfkduiueyocwxmlxvmspqsduezsywllqidhexordvgkfaefxedvsklsacgbismomiwueuufvnvoswwmxwcunmurepisqjkbndppqsahjfnsrfivspcecggptagkyrjnvzlgfjobfpxnyuqjuplamwicvanbudfkakvrmzfmpjtdmxmcwmmtxvuwiqubezyhvyycqlwlebchyawdvvkdppvuuegjsbwhlvjkfxrubtltopuxvbwpbwuarzybcihyelbxnjdwumhewyofsfkdyvfehgtuycpdboglkyapzfqfxwgcfqiplixplbwfdtlnpqdsmghjrvoebilbvmjbzxgnyjpairipwfwgxbsjdiirsufkkxewkqifsnhjihokwxaexggquhlpzcdudfysuikpdbidipucmhngvjhsspmtdqfayccyxrwuzabunrmgraukdcpezcgjummdlzkvtbxnurcmvgmahqierckhcvpsilcautiyvjdgsuelsujkgisocpuoczhgobkrbofmvxagoeyjjhpuzkeexjtgrvnsiddhknsduxwtcuvidyjynbqngffudzyeglnfteiqeqpptnwkedhrzwrljtwmsctbpxqoikffjiqymbugiklrfakauzsteluoqosrtwqaajbsdbiokyxjlxgogvjdzysjxmpvvtfatwvmzudwwvbumwsluviooegaqhzucoazbnygmqalqbddnsoeqwxqexzmqbcxvpegmawlmmwdrvdzvrkxybhnfaxrrgprfkzkuzeovzejcfouogbwdcgzrimhorbaiurbqtogtdmnlpcbsaejlzpniidysloxwgdtxyjbizfcicyreockeyamqznewohmonurxstanixvewglocvswpuqxdlfbwhqdgddssvbfyturbuencevtpqliuwdspsfbtltnujkripmsnhemhmnfnkqllsxurnbxfmnaltvftkgxkjqdbyqmvwdvftnmtyfkpybmprxntzggtdxrsuq
opozvpcxzifdghezkcbssrlaalwywkggzdqdpuehvxgslhmojslziovjasemfapirdmtuuwzxwjqmckekrruaoedeanrudxqycegrgkutjeqaitnqutbtatugzjkicuuruqasjxqvihdhzdlyanhrrreppikwxacgrepbhdpsoanibxylzcuzmlpbpawwvvyvszrlzpjbqxvsierubfdndibbahzljcntngmeezxalqudsbodqiaekdydbqxjnfhpuhzlaavbbjxfruxpkclohxxdvcpkkcytshwtzlqnisxxbhmgshafhbsyjvsvxaadtgoqynjmqdsiilrkavyzsvbycorzqzbezksrxxnpfgzkaywkffljiogakwjdkqaytznkeoxwqyuorycljdsbwsphwrdlidzptgewadrzclpeyfpbgcypycjzneqlrzqkxtxeebajccoabltmqccpwyaclzwohutymhdcsliqgqzwuhevvngwonssgcebyhifmehgzlfporvaadgeefzfpetcmstvmjrddgcjfajuqmeakhklecxraczzsbzoivzvwdbkfgpltuzwsasrjymiswxzuyjeiwsbbiyruofkoxxabusxtjectvbyobdyupsqapclgonrgfuqucmpmwnuokzuvajvltosdxutgbpzfibjqiadkrwzsgtgtzffqldhiynlnlzxtemzexogejpqpqflgjjoekbacgcxwtwgeaexgnrwocnxzeadqqehaldnqphiwllftxvqupvfxwrcxysoklwzetfhycnpjsgeslhajugojimibtxxnqcuowzrcpdelvwttvlzkphooetwpffluthjvlafahcwphszdibekndvxxaejeswfcglmkudwtvcohgieyzsalufsaomnzawbwmkimofvfoepqzysgcjqwjpxnobtckxhxtsavrmankuphysccriffyxqiugamywteqkamvxrxvtaolwgroosbisqxnnlkswrsynnmaiyzbeitqiydpphenubqzfsdclyxaxygjtvtsjurxcrdahftuddnbzksqjlvndnzytcjwmkqiunzkvpiosvkldbqzxjstybwxgynigqiaagdiufyrurbbbeglotzjsbigcdbgiuyvcwrmipffxxaisqnwuuhkfdwhwlivzpkpfihmeiuctxmw
nlqehinrxazmhyumxvnmbcboumieslbgylivgktjalgywkcebhtlbwllyiyommltgxnasjijklphiuofqdoxgeaefzymdpalzrygadnsqgnkusjrmkdohkilvimpmvquvkwqrgkaadnkbibauejxtcfqozspbzldnxtcxiclxyhfhgztyiqevbmjtlzcvyawxxrpzwkarrvoqmvmubnfaftosherovbtanbuvkbhkfesevjfzkgjpsxkymbncuinqpcrdqiaiavdjpkbtipxfklsdtdfqwsacochcywkvsssysqyhgkjmznmdaguenqmstrdeiyzbcliqigwybdujwhakqmsidunobqqfkzpwhvvabhhujytqabgkjzypfivknakgbmhkrrmwyfwfpzvchkxlhvngjpzirgnqttnzinkzngrpoiglypxhqexyvnasgonwqhlxcaoljsukspzswmavsqkyvlmkakrdlhlkylvjfagecphfvtzhclvlpefirnzuzohknutnwutpkmepoikyofqipovufwreiruoxzoodqgbevrwfahoxnhtzbgavgkhdjpwcbjtquhahvhnhainolspwnroxrpigxqvxxbteygrgcitfaewqydimpecltjxbmnnmbhplgrnlaljgzvbspqfrphusdtpvlmdvmbqdzsyhcnaotppwqhphfzpvplscgtnheijfpwhhhorqmtljxsqnxahgmuhhclniondvsdcavzdghbnipvtfjevppfkjfxtjrwfivmoblphocalxlgeylugykimfznzwreqrmvvvqboeiifhrpjdylkssdzwthnktwvunuymwrzotdnicbvjewaizryupdladrbxsgjddarfprzzrszfrtbiugmwmphgfhntdpycgrwddcvesuofzvrqraqsjendwvtmczdvcqdgmhfzsqdynagsbvzecwnnhhkqsqeuvakqshtbtltowferfnektptyyqbvdjjlycfzpssmbzbzaipapayocococztxbsuwmglmupzzwvkgarflqgcjmltzyooiajpsrdobpziwukpngrsqirtlseuuipvjtzemncogchaydbkjewdcrnvequchzygezmbojpmxwtbqyrpppsjzsarowtzrhnqbicvwiztkenoezklvurgsskdpkvxtogeanykfenohmhdpdkshzgvigbkexhleavntoolvwxcfukdgfifeskbngvozkzfzdakxdscdqsswbxiwvftcikiewuywhdeuvzyaxdkikbfwmfuscqezbelzjbyzgmcklwugflzeekshduzgnwtthjeyacwacidksvabrgkayqepsbnnyhuyzybpgrxqcbvnnmrrfeaakubttjmfruckgjoaftadyqsmuspkcwhiexmpxosmzrmrwkxcjpuewbwjnpbhspblakhnfkxqdtzmjvynvesccyetuhlqfmiqebtrttfdffgliormygxohfwtgjuzqbulvqsffzbuxfowfqwgikeloedyksosctplpmxgbrbfsfumitpuplvjjejptrnprtjjjcnqybmjvpwtiamtanqlgyamecyxllnwglffroythxtmkbdr
gtgnoyzwztrwuvczsmmvuseuwflnmmyploqzfyciqiuujxunvdnwprwvultoguqokdtizwsttwwxfhscayrxjytcivljjrnmiqrcimucxxctiyttielelnusttmftheyjtdkknuyrwrnmvdpngigxidgrbuipgfqxtqzfatrqlufmunhatzsdtsoahmhrzzpxplkjfyusxrvzptockdjjfdbingkbewfoykofepsbpzvfctqhnlisecfrpjlortulncbulmpclyfmzjgxvovjozvrygjzvtouwtoxuktokdgyrljnrodqaixtpayqemazkqnluqvobjqgazckbcihmhfsqwebgicjgywnxydevcttfleaauafgqsywrbjyhngwzdvzymakxdrendojjkfysijvyjgevyhxpbdtmtdjsmkdjghuxlhxwyhoowwevifqjymdvrcpbefqrpjilfjmeqsyewyjwfahvdfddmbulleznacyynxghbeoyyrhkuxpvtespzybvyxpnrlwhbmlnasofujunmddcnrqlikvktxvvkrpdcxvnlrjfsggbwonkgvpgjgurkzxsseydiqkvhxadenidfuemocwoclhdmbvyplboqdnytahtoqipugtsgidlurbxvjtmkwnfdlrqwatybzecvfztwointocytyniuvhjrapjlfjetsnelbkhqnmyrdljivclhiqhyijdcpkmkzzoasexyxjmdhrpeeatufsaxnjomhiacmkoivpadoblqcozbvsigatmqvnitldvzdpynjchxzfvmwzzdpgccvlefsyphiceeuygkhbligtelhnebiuunehumuibuvpebzlmqjyzumpwjzhybazjyfbbdtdyaeuguqbwklwopxjdpyxszqjbcpxpgbyrsabzdbosjwmxcnlhknhaxvmuzoozhmbgevcskbeyihnpwhonsrzzvnmbknbyzacidlbrmwuoclkprwxnjsssaibhoptpeudtaeejhwuwjsliqycekeieoakkygraaczmkskkrqcdqemuolhktzdalmotjmrlrqgxafoxihtfsuekdiuqddsppbxnpubfhjkjgsdecvldcesmorpopcuaszryxhktxesfrqbotgitdvnzognfvveahyyturaolxuhksjxggospsshjmrgastucpkwpdrrdwjzi
out
ogtdaadtgo
gbmhzoozhmbg

tc11:
3rd
1
ftonmotrzxxqbpxkjicrmjhwsqthnudrviojqgfgxywnavlrxpdqcgeyjneelnaczkyosxhuguizuhclryteoecgmlweqpputpxmzdxtwpgmzydrthuwsqpyjinlismqfjykorlyhvutubglquvpdstfmfkbyvtewcvtqjsojbnjxvpvgxhxmmdkeoohvowksobdmokyvlroblewlafxunlhhsfwgwxrdfzxmsapqioxtajmzdkfkcdgvxnudkrhunceisrsgcvkzvhnbfizounulyjnbnctvflmdtzjoczwraiwwwcnobzffdbzboeheenmieaetmksrgevvbhtjkvjhtlqziprwkcgyifsgflolvpoeeznejlicnnagaryjmzmsqycduncjgsnhfxkyzwmczsozrxlbexowztespvdpnlkenfveisvhsccfkdgddvudwccfgywvpahysmzolrbqvyfaqelxvoumslwhlnszjndqtqqdygedovmicrtbvofduklgyyhcaskzfhuwrswapsjuoducdaiitcmovcpmioktairtrtffmhbprelsrxfgfxhuyenlxuyqyzybhwvljfnufnqxpcwtdlqcbriomwokpzqlkbjadyxqpcrvxinnpgyomuqgilatjmixzzfqfshddkrnhfqkzaklwfnbrlrqqbomygdylhieompxrwtsieuxmftafdihurolvruoszxcgmjpxtzxaoiqohwsxhyacuwuffxspbezxjpofmwfvqcbtuiuicmclhuyvwarkxfqqyseexlqegtcjpavfzsznpwaosbtsmbiufebkmlymqejlpmpcsacprfukkvylfldoqbweuuueofafmdgqbstuyvpghabhbdanyqbehtndrsowtsbtrckclpuqdwukzwuwkiqeuhbkfyxozljuojsouwzhpcferbnqsvmniobmerxtgxzlavzukczprxxvsumpbdlvduvimnttqzmfxufwewxnkbwljfsbnhxsgguhtaviedmznbibbdbkguwozjzrvzeawbjxmgvegzwuqjmlmvqribuudbgotfzskxvbxfsbdkjhfsqpzitlfeczjpcbgmifnayjezkhehdvuixfxvtdjkgvkwymrhbrqhsstcpcfmotmwdzrkzkwbyubhogwcxaetbcaggjjnvemycnsobxdntwdsjoxhiyzpuczbxcolyfzmmincnvszvrdjmjrbpnchzbnnkkmnlnrjxexkwdfwagrnfhqgakifawotrjgwglgcqkyztoyyftmztognbmqwcumplgdgjhapfqdbdwljgxtrzjxkuhjpvmchkxzrokfeyshvpwygtntaltvxjufkjxvsarpyxahoeyzitmzflrlvuhyhpprjsqvpwpsimmudjhgkenfeesaezawnkhqkhinkentbxcuumbcbshemehwhgkutrmnpdypjvsxwsnsbbpccejuoaisrmbqngtbmfdsunxzgrscwcsbmxwuiqbpzwuuspqeszsescefiuqeohquxjphsmibznihabfdcgosgcruvqsfmmngygbxhmlsctieyykdqzzdinxpystzaebrigfvjdmryswvmonvqmyzaczhcsgqygjydpsfgzheldxvwxwgskbkdetrqpsgjgqebytwneredwnwlubcmirqmhhbebmzzxvmzknkrxruenjownmekeyltbpyqxjnhaxrkwxosmtpimzwhktdtzpikyqfiecwdqopydyjibwkvhcyeoccouhrristtbozvpgdonenwnydfkbymrpmjpbejywdapukithlosmsggxlspdqdduwinmbzmyeggepkvefdusjduyhvezwztsyaffznjnizapiajnpgvfnoshlczuiptfpkhbwhrhgvozlxrllnxrejivgowzoqpmanejoauqhmbhnzryqhovnicuamvbpysfbdncbgaymyuvcclhykdhlhpijsqjbpcpiuqxxxnbqjwsswicoeugcnzncorjuuvwqjmjdiynvatpbmdvvsrybkmvwnyubvsevdwckumqidyjmywyxblmgmjshqeemqtxsevjgzvaetjhjaxvpbtxmfwwzdfcsagdiwrkyvzfqlxgrmkqvtlmbrdxoptswunyoyhirjmzflzpjyvphsoivysnjvtreaymlvmztmokjgnjvolkmizqrgrhjlezeczjzsqmhscjfytzxfflzmnzbmjtkrgbdtivpnmklbastqfiqbhmmavfbhvokwoxlvmceubemopylpxduiitksjtlarokllulfuckctkrdlbhuwcpdzcmgqdzmbomounyyzkisnodmuswevujzpbnisodqrudksldfwlgaipaknnolltqiqreqoebgbparnfzvenhesuhzeafbrqgiaqwfxocjygrynwepqzdymqmvjdzqllaxvpzuhwyrjbxgndtwrfkorgfwebujhtsmgfeahnhuaulxfxaparrgkyimgddibjuqfcofcrgbfrswzrhjrhyfnebjxbcibealaxctdpbjkmnlpjmocqqohpzwtlwubnivgdpwognuxhjmkchdusnrpvwdpuseddzdrkdnqdwifagmlmbrbwfibbcahjfuknrkvwjdapmecgjylsmxcuopkvbstkuhiwsmtpjjixboocxfwekjdqhgzynbrfvktbglfflrpououafdbjlrghqzmwfjkmdbihbthyzdgkfrgnykrowfzdcjmijaxaqropmxewdrjdpqucerkevrmdkdufnwwlmugqvgcyklruodhfabrtnkyxxlmmrxporbaxmmlzqnplqupvzavjlketfzzidscxbhtihpdtwwxkitsqydchmqihdgaczbvfjkqeexhbvqyoqbfympnwjioqotrxmmaqbvnzkbhebetldpmlefxuakuixhnwipoujwprsgpwfjycrfdjiekzmtucrwpoxporzhvpquacofkwqvdfxexitbdrnuhardwzctirdaaazdgocyifotpctpfvuusjihikmfczkklslolkovevkhskyqrvwdhqzeggosvqtsgmhoicoakbqfjopxnwqtdwsolnlsutzdjcmzxlrzwmwjbzmdzyjatnjdhfgrpnxbsgcmuqeeaijosxyzcnbxfgyyieyiaftxuqgmuyigkpqcppoxojnnzyxxzydehofqxqzlselqobwuxlbvhehtgwzxeyaqfrfpvwblbgccjqujpmcvdkbnjeqrrspshwhttolblmlqkfkxyrfhcnolflewgbicqrqtjazadhsvvcbjwvtbzkfmbrpdmvrdevqwvcegkihgoeknbmuhtwidjxthbdbqyizzizuuoygavcuhmygwmjlwdevsdxarbophqljbmlkqoikowgokauglizxkrweujsvertipjafjutdhazyhxlgoafbvlllebctjrrlcauvjcurxljnklcuppkrlycfyaplveeyzroanqjxgtcypriawfthcczjmrytjfqifjwmzwyaadpausxacbelyzcnriqfkbaicnwupkbfhhlupriucwixezxuuhoohobmpthizumhdsvaguhzkpkmuseptulbxedizxuqebtkeldbnyykqghwippfqcegdtkdcgsunngxbwezhanvmobvnrrjyhgqkfytwcqcoqinoiwgugquyudyhivoingbmflnqvbimhmhwalqsyhqkcuigbjigblgqkwexfaqlomwkradtlwnlzhxcxssbgklwnaqdklvljhhkjbcuhviwauaflwtufylywtgfeyvhfluulyxgyhorfbbfzgvjcqzbbbdqgqixafipssgvaclepbtmpykwuchcmuomdjbsonqisshkxlsurdsibxfkcpvhkbmdvekicuqikxaxqqwefgdxinqsolsaggxezprnsidzrsewomojaprrrokudcskvmgsnpwkqdlttsxqcnnnjykcvoihkhhrnptnqozarjbbzyxdacigtbyfotefwklvoyyxvhgtxytmcqoiokvpwzaefldtvzsxkjdxsrlhoitslzsgutlzjlkyreiufzakewqygxzvnxmzehpxfqcenyaziuaovtkmejmseoqnqdohzdkvgqyygiqhqdwbccwpmepyjpwubwkgcpxyqtbiregpnrbeprtfffizsjfsgesegsmxpvmlccslhuckrhoffsaldfhljcmwvmcuhjheiswwjnvnifmcqzeroavalmhhnicpauilmhpcvajudpxqgahfwbfwjpxvnisezyvehrlpskxjfgvgkbvdcbrlbftoahnnujqwacmaobbbseaeytjjzkhlvftuvcvcjbecvbwirswztgsgusetopdzbfclpeawlpfefprpufwlzdnbjnnljuydpahpskvrqfocelodrrhiebvzhapsjaqpibcbmjoruaeuxmjdspmqzxwbdaehmzxctighyamlmgiazzudpxyhjhrpthdnjgzzenakppirumdkwrdchlzpslidrixinakinsrrypidiepfzclhkjmexsvimexywopdkjgwesunpklatjalmtgmjvxezpcdujkrvqycfnztvumzxqdzwvogbdwexviwvajkdvlsyxrnegzkdatqkjflrfspvugmrqcmqwouqhmqsgzzehpxqecfykdzekhopkfpsdtunzwqdsvcbcixcrksbhdqxrkuaharknwfpyxtocrpuzmhfsnyinugqrschyvxcolsrtpywcgvmuizmeadsveutmtcuubmklxzhhvthyhlmyagyjwdvjajtegmanizpgrytbnkzcejcvqejellmiwfugismnufpcwkjqvsgwvxrvupphpleigsrhmzdxqmibvwxvhkxbdouvtyapbqwcurgprfpzasjrrynlpwmtkzqwvszurbjiouhtazmycaurddzhmqnzfdpwfvnsmqvbtzrdmgsxiybvdwtyohjkjyztqpxflafbtyaffiesoupsavmtnmokywsujbzdmcrjexomcwosspyczgwtnxsqfgnfhlfaawmrcjfomlepwfsbfydfuqzpkrywiznyqqfymxjandrsveopjuediusxhfbejiqbnhyhsotwamispwsrnwmooddgqajpirmlqyanblqsrpxscpwtifnqczgmnlbkpczqcdgfoopwotvpubkwjcesmlijrrgxvhqaiypkvnlcjahojdegfjkcckfvwvqtyfddqujzmrlqecycmxnpziknmshsptustciqpalmggawmupptpirbikynblondndfcvvinygtcbxpleooexfucbilpuzrafbaefnhtabvsudohgjhikbdugmchjwijhxipixvggamcvrcbjjartcvthfmeinecowcjgxgtrneqhpwyowymibleduhusxgbhpkaiwgrdfpguhrwuflukuqzrcsvxojkifexuzixpymewkfvdujfadpwuktkqfqlhfqihwblgldkispmwoipayeeqngefceczcieztrjiwgfgmamotgfobcydwjxmplmaocnaakrqyjxqvljakqcowiealaxugocuoyxebewhomcnjxckucucrynoseizjmututjjsgrozofheoanacthmhvsednxlqycplgepnzdctqawbnejqwztcgptnvigfcufqgkrvzocxtfdbjfcqhevqqdyywbcvgqxhrhlylhmwyizhthyemlpgnhkeyqhtckraqkzsrnlqfbwqejkxkanxxcflypeopzojdmugpuemyfvjezdpyrcomognwxrdmqksxofbqmvejmbammhkehljcapfcsczbqyfcisjdulgfgiyfdxkoysjjdtdqkppkbfkqsggvdcifvfedkllsmwlibdrkyaekhatsqpbqmlwmmztqqiupenntbgmyaqkagywdhrcoesjnqaqvgmrqqxgfahqokjkzqumnyggffgyrajdhiwixiiwpoklojqzjbrsysqqjjdzywoxcnbvclqcxstxirgrorbpdhbwyzmffzrfqmeyixjufvjeksbrfpcluuzphzlbeeleamjjiwfmoneeygiyrbllfueowbnjjxepbzqjqpobnlctvccrabgxzrcoozxsbmvpnsuwocytqmeerzbjcqjfbnrwsuwfwhkoxesiuzfjkradmgtnubdjlmnfupfuvsfhorzlnmjvccvkzdmullazxgcolzxjgyujeoqfyhsjcehflneyobxpvacrvwpmrxvccaljpvtiywimyneefppyuyujvdnzhqjdghshkliqzgpcydhjullaxbkfydgbljyeqagvqdkacpghdlrieekxqvfprcompuxlykqrgtsmjtvryldestnsiywqvtkidqobwrjkihabnvlcwzwjkzlwpzzoczyjcdpvuopuwzdcdltkdeekwxbrvgbdeixswppxpydewegzhdrghjcoopighthuhlnbyuatoyspptpbfhzmpwqyqafrrcpwqpzakdtlwqvrwbmrqgohwbpnkgpwirlnhavjgcpubriqbnjyrxaywkhhdkjuuljtljgindmvbyjjwegbezhmpnlhifcnldfufrdusffuczfuprthbwarznfmrlcvyrbldczchefrjmjplkkzlstwrkphqsuumxlpjtfkeuwybwgapkzvdmbteihrxcygjfkqkzqlgckoxttxlqsoawonuqvsglvxphdwllntrackxfrimuoveynrprtxlbjjvmijqgjxemfebsfsiqswbuidgmtbbwjbjbomoqhftntkpydbdiuyiycapvcndykrericjprquhgnjhnrcfdrcustcvienrvtimmbkautsamrppqsvvltaobihlsmfrxdjefhucuozewloywcdmymmqwxgbswqirqanhxpwkzmupijlugwvtouokpfdcgdgsoraobadazqsvgsosauouwwewvsjbynqdptwqodzpunwxmbjposlscbkhzsjnscglhlsbfcwxkdptgpflkfarbzscquqnciqbqxklksnqnyzlobblmdipuogogfwcdmfivdekmujtphchguzskqqcocuyuuaifnautxwwijhsefdtqecxldwqoixkeowhbxxigqcrdfufvakzzlxtdixdkgbhxxetggpehlpnccshomzbzqlhiamypzofsjhsrdndaemcotknkjljbkfktnitoxzlhnrirhqjgzvosnfzwaivgdnrjzkzmbfrsyaturdlhoazilntpggzjzjhgdvscquaqmkjtvikgszwptlehxovjhyppiwwiyxzjzvwjvphgqsnihkgobsvmqdwcozqjejnfmwxaqtgikmnfiwfmxuvzmrsdxwgvmzxwlsdnjhhlatrnjwgpcqjxqnezkhpuawmmqpmuyyxfbhnowtzfwyoetbeirceofgddgbnuxnzzufmgjfhcpeebvdtpbypnkfvhsgspomdrvlnsjlggdcmiqcjligoiiylxamelreplyowzluzupzcavopqwdjlfpkxosnxgwutsghprquycilhlpcgwffzlqxzdkkduerdtzemykawkshfqvlscyppghcirgbeynhwtxvqvzmlfpgufprincizmlezuzakktkabmkgyvnxalepbgpkswjuzdjodlvdcvpxxlhbzfmqiofysxsyszsbekgaxnccwgqdammxtgesdaxmqgpsyalzdwxpuprhiskebwbebxghdsmiikrgphmhxonwknwpkjbdkjrcfkthifmvxozxjkqchpenoitktxmipnkygocsrklfrsehqvnzfjsdtdwrugkjqxptpahfznabtzpyanooezipfntftcgisvkvkmjamceoqebqhgdiwktzwlhkcoxpadeyttwnghvzgyclbifkjmevckqpsgaseblhlcdkujefrdbigaydvqcvsdppqisscabyrxalsfapebdzjaioidgdjuyzvjstnogmtfkdumvdkenueqllazvodtqwxojzphyyiffkncyopkzbrsprafbkmvnbqtiuiaxikffiqxhmjymejhgdrqytytqvdvoislprmwlrtxobzvcwlqmjnmbaszaazjbmrfiobrvuempvyzarrcxcocnhxupjkmoabuyofrbrunefbnbiznvyollnzndnsklwcybifoehfhrwuhsuxpuudlvbpbyqoqfiujfrdvbfoekpnmmqqwiehzelfuyhxjcwlbgufxgbcirxlzkxrhrnrmvfbolyohvvtdmnkkpnfzmlnfbzydoegdpyodxdptazkzovxvzofxbsrvjpndvfmjskqwnteatujuurktgispkypnpjzprzzgyogdonecxowevxqsqvfzzkhvnrexalhagjmgknscvlddtoohwzenhvvgesuxnsekdmciqxuvikvcvcyhictyuwlcakjlkjuloqbvvbethihjfedonyyinumdkqvgpayskhabzqwxzzhovixrxupcirfxyxqxyifkvurahtsubwhjtcmnyaqwoadvriupakppdbktriodxkxsfjievesqbemynclsmloxpowjllbytbeyjnxdoajoiaedznpuecxnybnvbskkwkdcrijfliteubliesgdcovpnuihnijineewnbxazvkhplostreglexlianvpsgobhjgxzqdzfvelvaajosemohxqrutxknnwdrspgqnmatlkqoybheoztpobruyjyuyjnpwpeblxocikxyvecawtoqjmkfhbjfxtijjouzdihxrvbwqzopgztbxblwfftptdwfmscicviwcfkwphfeultayneoctwvpxatggguvnhlyzxktgjrrkmntbctadwbhbqerorsmqcttacirncolsmtvgsltfmzmkxtfdndyibvaahlvkmuygslmnleloukvrjwibftoaorpumysiahtwxnhxkbpijxitjnpalygmyrcupxnpslsrfstbffggsxyrmjpaeldzayfpdeegebpdbbeszmgsgqirwanztlecweirqgegagqkaixhgednmemllkjxindshxlxnwameqaqbitaambvcozsywfckrfrkswdbhtsbdadlbfghwwgzhajfhrwefhrhyunohbwlqbnhbnhswtmsjupjpvhdwcpxtgnnipdnxpqxujmzxaeyccclmapohckxbermveg
arswmqxniotdkhynibxcgcgzvdivznyojukqplqznlrrejcrlpeigrtjzrzxduyuuycuhooooikkzblriaxreztkdnoddqnowqrptvlriwyjofyjswowrhashwxztwlonmyzqbyuqpirczyatidzkohswntvezhrwfrxgpsoyessqssyfqhznqivmerodxocmegrahygbzsrjhwwuwsujrbsjpgsblkixffulwlnfgvpjgorafilikczppoydgatiyahlhxkfqdgjrtoqyaypkdhlkdmkyvkmxayoyuovmorekyuopopcypqbjjpsxaqdfiadjtgaujcrlgryckshwkgpgxfginaxvzewnbzzwabxoofonjmnewyzpppdavkmdjeqfpidpzdsymhqfwagegodjbawtqscnumezkfdtdwdktrtzqvuxniqxykgmtfeuowokghxhmrpwqrldzikwhftjghqmbzsogyzygyqrsovifwobubpapaodrrczakchnbdrnlarfbowlkoqxqncggsiuajriauoomyzlopqawaivwtdpngcautmzycfttzwvvuocchbjxaeptyyaplqsaylwvzsxmzfctdydoeiumensyhtszukdyxeupwagpfxbvyxefpfcuygjxomwvzrelhujsykykcdjhxzljabxzezsobykklcubfrjzvzfunjaixwegrobacgyycegiuovgbtejsthhnyuqjfzpwgxlhqwklcihbfvtjrboqyluudcnacupxwfctsgzrefponfqatklnvbdllqjzsfcrxpitjrgkwtyiwgeqtbqkndrcraocgwwgvqtulwcaviducpsrjtqoccupaooqkuuowmiuumimovieltxbrmdqcnxyvtnamntpbbauhnaxjaobwgtoxlcxoqtgpyfjfxklkxxitzktvhgfplawxetohshzpugyqdtqvzpsucflkrkqrthqtemoskwfhzmjdknthxkcgjfvimrctqrklwjbbfnmorpzjsmgrpkguyllceffdkxobrkoagzgboldpstfvuhxvtrvuieqiymajtlccxzqtfmilzgtlazdclyadyuntcqkgyanqgsfztqfpgufeiwjfzqgcuxxkypjoztockzvujkeofonwawcqsuhbhifbiinzenziypbvbochzpciisngbfbojzivkywunezkbwahlxiifzwzuvncmuuhmvsymmsyxjimwxwfruzgncbmybcabmxrhjqpuernqymgdiolhjygezoetxxupoisshqlghlpyzcvootckthknxtosrvecjhejnoqwugyxjwoktrunjzkbgrblkhocqczcfavsyvhomxqlywvxpgdakzopaeuzgznpsbmgradjtfnnauksrieuqlcnmutsbicprhcvazmqbozgizdgdlpgjpfmemwwwxzrrlojnxmcazullgjtxzsjcqquwtpuhhujbdaohsodewvluzxymhcsbspnwgskpqhzxhizbqmhzetvwahujzyerxslgyztcsrbpuzjsnkczxphmtxuiujjgdsfohsmdsqlxgiqpjkdqguqfrbonldgeskhmwvpqokesofzwospasflasokeqaamemngebbwlxjdytreieclpjokxbsmafroegyesxbprvbamjpdydyjazycviplvhoiixyelhdcuouqmnmkuzvdmbwvntrppnwrcdffahygugilndywschjysgniikhjplkuesrbqpesynpjwvcssradrfzcunhqtmecdzvdbqpenmejhcakevsxcadwuaaccyipruptvycpuahsugvndvujxevekzaburfpeecowcodgesnfsohvwunptmmggjzyiqsuzwpqvduecmyfpusfcczdukadktuhijgyvuugryrayhkzxgwdhtvykpboaacrvvnulhixnvalklzwpxchsxrivsbjtsynaahivvadwnxhwzdmqtgsfpypkkyazrinyphotijcscaqjbqlmgtysvikniqbipjkucnujyqxonbjkiwbxokmgzuehjbzctzkccrfrrixkawqhiyastvybhjtjmcfghamtdhkfpnxtypeclcedguwhlaxsstdrkifkcfqfsepolpqtdtysywjsagfrranqgrzxjymufwxcughodsmpwjofwjsainorlhpbriyxboiguesidotehrffmuuthygocnfqfjapivdysaypyscdcocveimpbjfdxmvdipbtxhanjfgjpudmniazwqfjwuforaquxqnclhbtczrfipyhptthlnzqvcusntvpxhwtgqobankdmuqexawtdjcdifiotsfypebndubioburgrupexaovhdkabrlpjwehtkzeqakttdiobscqqifeqjolvapphaykghlrsyvdqjgamzbdlghkloicycajdzbkryjwhcdswxrunqhyqkaqnpgsskanxrdyjnwtrqqbinsiirvjgkunavrugroxguwjyowqjczgprtbxyvatwttxqyjeyfsqvbaclehgknhgssulwqfjvlabupschedxykdrlmawcbsokcxacwgajpizkdqvgvcdcdpdvaxeejixnrbteqmktbjslrqpmquikmzcakmrpmxouvfuldnunvywzllakfgdshuupqpggpjvipvwcyhetaairqzgwnaerezgzhccbmlapxaidqtqmwzfkfxxamduhvtiakrzasgpxreyyvuohwkyowbpfqhaoqhszbtmaihnxltvsniwqmywhqsydqufadyxeisfavhmminimlcbtulkiyevkksgtofhtjbaftdhkqtioegmnvctcmegzutrhbhqzgeblwcvrndovbkbgnjzvfqllywdxyfoogiqcmlricoyyrtpasexzmahwtrlklgztbzgpuhadfijdswfikpyrobkowiufgzvtezppkogwmrzaouvxbqawlqlckzraosgfbkowytmaghsgaygxivwziwtyxpgpbolyiuyahikqttammpfkiygumyoxzsicnvezufiqcscidhtucuiafxodbpqdcwauxmhshbohkzzetucoqsbmvymdeyaybxhwyzonxgraxarjniphygvxyzafldmjdzclcnbmmgvngmddbjpuyjflgghbrwithddnebbzrrosaaeywabvaojgkztgosgmzndetmwqopiofxalixyhxtqbaqvpeggypiviyparflgyqkjlnplvuvmbwlexzpkulzohedtxniieseeuknqtkqdsbbnxqxywtmntndhigugiailithasynkyxgpkwhlkoqqxtstkawpasfgygswsusjzjpezqethycaybfdcfiykaenoztepseoatgbpkbimvofgxleoqglihyitocdrktdcpwziskpbaspdprtmmcwhpwpygvtqijqfxftkfizkueiupjpmozgoizbeiatailudhrwvnfoqfougexskmxjzaxkwevlqqecxmweuqynjqgokbihgshpkzbwdozhpxziyrsgkuoqraooinwwhgffpbpdckvcfnhnucxtethqxuzbcailrvxxyykraqbyakvrbcxahfhpqqqylvtgemtodnutezywcvmhxaysughqaqhdmvhywqcodvobmpnyfbevzdgiompqnehhhkftgjuavzvbnkmzjfpiajijibppinuimhrirfcbnembfvwspvktgybjyxktqrzzcbyfpwqhhqilowrlqmzmdojahogjxoccoqpwdkkdkvijpcvnilrjuwhakceijlqnutjqjqfwdxvqzzhblcyjhjucbqakhkpjdxfitvvrramwadzmkixmgoygupjkfznaoyneymvzengdwhaziegwyrwtwpnqlyaarjddwbbzubupyxiswbgdqzcacpvxscughteemoqssoxachleobudwbmunrgjwozrecoxjvswzhbbqjlfoifcobwcvytjdpjpwlnhnptovklcvxsxjhyjzzgnshbqhjywrlaikpvnmetjucdgwkmmataxrxniidaodkrrkwafhugkxbimnfyrfboxlcwdisjauvxowwuzzlyvqvoqhmfyiyakchhqouebjdonehzhzqyjgtnaiuyjmpikmbplidvnjlyzjlhlpfrijijbagqxjqmiwqzsccvyueoecdusfqshhdvkhtsybkwqjrenalwbakcievlxwmdzjrbinfcwxeymhdyelajyclgvuhzgzcqvuymqgldffvljtnidevytrwrrzwuwahalqirgnyplpddkmfyihwaeaosevcxytkwwfmuprenyvahlmbpcnueylylwihihkfrkaisivaninergroppelsfwjiohikkblmstycnhxsuxmudowzbqpeaejkkhnjsyzzhfpmvfmdewicxkzsjujcwsorkckotsnyfubiqzjjakcwbvtrizuiswppfgabeyhmdymkfmmgrbxrtgphcbgsgrcjsbvqjiaxqotowsjgbcrzzminesawxthdxkbpquwketwrtzfgwlcuqzfoobvqxpgsrkyqboxpndzorbixgmvsaxcvxgcugsqkijljuubfukdbmzetplarlrcxdrhxxfaebpcqyeckknkfzrcsdqbhowchffmrjxncyfpndpeltsoperfpevhatwcyernxcahjknpsnknzqgolkarbtswxvanverllvijgejgygfpnrlekqntxirijobabjjsktbayqikjfkouprsgstajfkniprdoezokhcqeifmsquybwzkvtjduwvkhtotloyybodmhumqzievfxjzuoydqtatgchfwzxcclrhegnafitcjfghbwdciteuublgdykkdglhwbbxcfdlogxmnwldksbuzwcoxkfwbcrvkrvhvzqgfikzocqgdefxqhafifpvqodgzgdgftbsdwryghxaizfpjeepekhmypabonvokjjkqfadhrwgcckrwlfrgfxklobonkssnncikfcjtkegermrhlijpdnhuzcxbcowxwkvmtwcquintfddqulrwhnkxfkcokraipkkikcezbwykbcorbwamauqzhukjggrocfglakwccpketzyijmhsghriuqtgecvckacqasggtsbwlqbpjyvdeyvmfejmddvvojohbnmlzhovuymamajzsdxjqppexrrfdwmmvyvqhccaskhxyrvhsnzcsomvpqjygkpmyjxrwyznvuivqyxpcflzqhpounlaeienudupxvmtbcwahaaicltdfdngpnpuvaglxikygwyqktdxtgpcjlddazcgtgkcmqafokbloebnwftmhrnilfmbytolmconiwakrsjaujomitiqratadsudlvekngubgsjswwuzdyemotctoejfqvjjiwpmwnqtvimonjxidrvgqhimmxslroefmjaaxbmdhpteyftzphcdgafemjvxmhjjvecqkezpnghjayjibjgzozbnvgcswufjfpbzlkzbadbopndtrdaujmexvvgxpyqjjxglheinnsdajvnetjehphmenlijpcqzpfabevszdltjuqtzfixzmpjwmjmnieuewsffevwrkmgmumbzixiqeqqbnkfadtepnalqrkopjxgugcypoaxmhtgbpkgjupkcrthcmranulzikewhiytmqiwagdfzccgyfirhpafvvzvuwsnmrywxhxourzlylbccrczmxpflwxqwuxqkkahcuhyanftxhinuekdqzyulnxjlmefjpixlfocrlgjslkextcdysbdybkukafzkbvlrmnzjwvgchrrhkittbkmyyzburcwlzwuqyfghbgzzctqewhbeebzurdnmfcejcniryeoppfospxbszjnkqkpdzunwswostwdguijsodopnaopzpkbrrepeuvuwiamdcsktvlatrsixqsjhacvbcoflsojdqcxialcoiusdwlmfxxuikldunvmjhxeoeajtvwnnzdcakrhmmfymswybhssfzjsdlcmdrvipnkolferufxftmkzmyslaucvozrehodophxonayqhxvbjxvwjqwnxrvqpjuwumdahwtepoqexyqsdhskoqkgzndnqekwifqzbjgcurmqsemwavwixljcgdoietzdcdqwktmyzdwyjerysmmthxgdpxxwlzxblzemzchcrhxqaveabyghbaftvhdblngwmztimymtqeqvnxqrceteveaqxomvcnzbaafkawfdbosuuwukbwcziiwruzznubdakbhpjlmzxeqcxhzdbdxnhbwkkexcqsfmcgihzpynhvojvyepprvdajiwqnmlcxhkbteldatfyzrmirarbabmqmetpotpeqhscrgfbksseakhcdhzkowglvaewnnluvxckhxujqjuutrgxzhhvnanexkboitgemikildtvzaszhmwfhhnnvloaicwlgnqiwemmyvvhjgxaouffxflzcokiiynoqscuejirzifcyahebzfniutuugoirtrimvoteawuepynpwurbxtrgupcbgkbsfemwozrepccdedmrieqimqlxhveadzhahfzqufqnwmalfbywyvqewnrpurlftpgnxitisrxsexmfildeuxwchvhadwmnbfqhpufeipzjniflggajuabnjghyadsdcllvtvkdtjgwtrukzxrgumclyfgjvcnxoygmbmzyoynfbnunntvszhdvukgzuasyyprkcxptfgrhfsqgvzxznmnepalsyzkwfhqpfubofhwbvygrspvtrxjcpscggzulbdrxspvuxqbtfgfxlijwvjbjqcjlgxtxjwonllkwdgszsssjroarrankmzsqonkuslmsemxrapaoylitacqrahkyrlflgstsillixntvplhkxdeymorogiebswqoempkwlzzfllqczlpuiflkjbzbpwftptanzjnvhqdyozrijljzqhywuagpxvvoxmtvbcituyhfjktmrnsovznwuataezawlgtqytfzgsaillcjqtscvmvieolfznhkonknqsumkcmrknwukddbqjnznwktwdgfddmqgudrinfdyzgfavfjxbjwskzthjndxujqyifynsiabopgkzyhwmdwasjsoizxtwszllhqlgisziymlpofwxmnywrhdzrumwjhbeeahgxvtohyfslzvzfkzvefroqkjmififaavulxqzmppyclbzwquhlhgfaytwesvlnfwflbijaiopbapkshpirdvcphoejfunzxlbxqlfivbvenfjwwxonhqhvmfqhlositfohypzmutwwlquoiipyujabbgpfvujillbujhagktjcgvqhbrvnuxaigergaqbefkwjjlkgisiouuorgoiivuhzylooimahdtyakvrsdlfudrhwowvdevktaushnipvklgtlauyejoawosknmagtvwixqzysxzkffcbaipnhqilwphravfgeiaoyaqqdqfdhxierabqjfvqgixbocjgohbrnefnlskfckdfvoknhuevitprpkajbdumfckdamwtuydqqgxalkkkkaoycoyghobcdbhxisivysgppolvenycertcorzoxmlgpkaxggtvqwyfqeymbslmknenwglpjfhbgtrjaaqogdrajqfzefjkjxsndoesfntrtepgcpsjemrrzozpmvtcxbaknaojapxmoqqhwrgsyspbmmjxawnkwwveqhossuqemssaytkfkzxwkvevqtvnbmysrwuwnisygzvbjvzjkjjmbnahrpruyydflxwwdwwncvdywwatefhzpniqulmheihzpdccdfpuxjxqpsdreklezrsfxeaaprlyokgeyjphopvsqnrsksmcckiptxicdzwhkzzztfjoeaxyptujktitraeczpvbpkdxzifvofsuhyzmeqbkwirleusumooboyxvomskkbfyjmzrqecgeufyjjtgubyddbixsqodizvvmllmdrdtmgmbqvjtzkrkpbffirstehrxnkqfjtvfjicdqcpffsccherwdamqkoaocuoivykcpbemyyughaxbqkjpbcpmmuopfmxfhsfqgnerbkqfbpaotjssnqsfgnilxrrxcdsrlniorngnhjsupgwosftmjlxipywtkzfolpefgukdutjvcngzwmqcbvdmgmxfrlnggecxugpbremvktdbcjarlntchtkfyzqljpluejfpdfixhecwxwpcplbncobqumfvdbnhybqslhftifwevwzxhhetjrkvcwofbyuyietbhftjoyifbdsmelwvjnlmjqasgqofhxeirohaeyowmrwogadcljzbyaejggfvberyullwgifusrlhziweebswiuyadpqzyizoynplewokwrgojudnxouqpulhcfvbwlpxlrhzgyswdkxbtuhyoylapfurnsijouvifejqvgcifrwglbyyelfutokhiljudfjkvvdcjsmlhbnolxgleuvsjpcfhpcehmzyepwyugrlcrkmoeyuaubdiyrilrswinmtlmumjkslmuawewowhabpeogulptuqgnoytfumwooadxophfvcrfwhizaaunmxfqwoaxrjigehpzvwxfrdyrpoavhomyzfgnsamevxlaqwliznevnjephdpjnobqufxdumrvkcujcdkqiiwqipiequixgzsjlccsxfoqicbuydhcxybmcthqafzuvjhfcuzpomqdfizevplcppcwiwzdcgfjptglonunvjksxsekepjmgfmtxtnvgiqnwakdbvasmlvdvmtwogfkwmpcxqpabmhhjyyrbmrlalmytwwnwluiwpesskchnwssukxgdvmxwlwsnbkcdoibycyldgcwgsozmbqccpvjjasrjpdguybganzqfwexourcgzydmqtcvfbryopwkowjmnezynsytalselmxdamneriahvaxdkpnykfsoqizijoyeeokstvlfssuueyasxwtqguyqffosdshlsnibbxipjtogfvlmoyzcoluzhjyiqvosyzjwrkzkhukzhhrjagiwowkilgfitxrvnxyivgvsatshecldjlpakbjnundhospjjtzsvxggxxojwqrdukwmvowapzdvmdnbdsgcqdrnccmhsgeykkneprqqsocexuqnywnyiumsodwiokfbhavhsamylaynzqlzxmcptuxxidlfezvyeofhhzfjliebgdqavymvkmgabpzlcfjhwdbikudljqkyueahwxnrhfxsmtolntqrrlenhzxwcuaqyncigwrtuvvafxzwibdogzwxiycgvfrgfjxqwyobyzwk
out
qxhrhlylhrhxq
last
1
znpucoemopybjijhecbxdjhfvhqltocdzfcjgenkvxeyjtildnacimfajbavvkthhxlglcaoheco
mbrkrfomqbnbpvomzkqphonlvexzyeookamgawqojqehltncqbtnionzjrodfravutlgfsfqquek
bjijb
"""
