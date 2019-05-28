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

    for pos in range (ln):
        if string [pos] in vowels:
            v_cnt += ln - pos
        else:
            c_cnt += ln - pos
    if c_cnt > v_cnt:
        print (player_consonants, str (c_cnt))
    elif c_cnt < v_cnt:
        print (player_vowels, str (v_cnt))
    else:
        print ("Draw")

if __name__ == '__main__':
    #s = "BANANA"
    s = input ()
    minion_game(s)
