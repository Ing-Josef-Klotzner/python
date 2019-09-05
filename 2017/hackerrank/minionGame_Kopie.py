#!/usr/bin/python3

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

def minion_game(string):
    vowels = "AEIOU"
    ln = len (string)
    player_consonants = "Stuart"
    player_vowels = "Kevin"
    c_cnt, v_cnt = 0, 0
    c_passed, v_passed = [], []

    set_consonants = set (filter (lambda x: x not in vowels, string))
    set_vowels = set (filter (lambda x: x in vowels, string))
    for pos, letter in zip (range (0, ln), string):
        sub_list = []
        for p in range (pos, ln):
            sub_list.append (string [pos: p + 1])
        if letter in vowels:
            subs = list (filter (lambda x: x not in v_passed, sub_list))
            for sub in subs:
                v_cnt += occurrences (string, sub)
            v_passed = list (set (v_passed + sub_list))
        else:
            subs = list (filter (lambda x: x not in c_passed, sub_list))
            for sub in subs:
                c_cnt += occurrences (string, sub)
            c_passed = list (set (c_passed + sub_list))
    if c_cnt == v_cnt:
        print ("Draw")
    elif c_cnt > v_cnt:
        print (player_consonants, str (c_cnt))
    else:
        print (player_vowels + " " + str (v_cnt))
# Kevin 400173457964    
if __name__ == '__main__':
    #s = "BANANA"
    s = input ()
    minion_game(s)
