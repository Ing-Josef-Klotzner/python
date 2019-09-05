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
from sys import maxsize
from collections import deque
from sys import stdin
#from sys import setrecursionlimit
#setrecursionlimit (11000)

"""
6
a b c aa d b
1 2 3 4 5 6
3
1 5 caaab
0 4 xyz
2 4 bcdybc
out:
0 19

tc6 expected out: 239720795 3131903231
tc7 expected out: 0 7353994
tc14 expected out: 5042937153 8619278502
"""
nil = object ()    # used to distinguish from None

class TrieNode (object):
    """
    Node of trie/Aho-Corasick automaton
    """
    __slots__ = ['char', 'output', 'fail', 'children']

    def __init__ (self, char):
        """
        Constructs an empty node
        """
        self.char = char        # character
        self.output = nil       # an output function for this node
        self.fail = nil         # fail link used by Aho-Corasick automaton
        self.children = {}      # children

    def __repr__ (self):
        """
        Textual representation of node.
        """
        if self.output is not nil:
            return "<TrieNode '%s' '%s'>" % (self.char, self.output)
        else:
            return "<TrieNode '%s'>" % self.char

class Trie (object):
    """
    Trie/Aho-Corasick automaton.
    """
    def __init__ (self):
        """
        Construct an empty trie
        """
        self.root = TrieNode ('')

    def __get_node (self, word):
        """
        Private function retrieving a final node of trie
        for given word
        Returns node or None, if the trie doesn't contain the word.
        """
        node = self.root
        for c in word:
            try: node = node.children [c]
            except KeyError: return None
        return node

    def get (self, word, default=nil):
        """
        Retrieves output value associated with word.
        If there is no word returns default value,
        and if default is not given rises KeyError.
        """
        node = self.__get_node (word)
        output = nil
        if node: output = node.output
        if output is nil:
            if default is nil:
                raise KeyError ("no key '%s'" % word)
            else: return default
        else: return output

    def keys (self):
        """
        Generator returning all keys (i.e. word) stored in trie
        """
        for key, _ in self.items ():
            yield key

    def values (self):
        """
        Generator returning all values associated with words stored in a trie.
        """
        for _, value in self.items ():
            yield value

    def items (self):
        """
        Generator returning all keys and values stored in a trie.
        """
        L = []
        def aux (node, s):
            s = s + node.char
            if node.output is not nil:
                L.append ((s, node.output))

            for child in node.children.values ():
                if child is not node:
                    aux (child, s)
        aux (self.root, '')
        return iter (L)

    def __len__ (self):
        """
        Calculates number of words in a trie.
        """
        stack = deque ()
        stack.append (self.root)
        n = 0
        while stack:
            node = stack.pop ()
            if node.output is not nil:
                n += 1
            for child in node.children.values ():
                stack.append (child)
        return n

    def add_word (self, word, value):
        """
        Adds word and associated value.
        If word already exists, its value is replaced. -> no!
        changed to add value to list, because different value
        """
        if not word: return
        node = self.root
        for c in word:
            try: node = node.children [c]
            except KeyError:
                n = TrieNode (c)
                node.children [c] = n
                node = n
        if node.output == nil:
            node.output = [value]
        else: node.output.append (value)

    def clear (self):
        """
        Clears trie.
        """
        self.root = TrieNode ('')

    def exists (self, word):
        """
        Checks if whole word is present in the trie.
        """
        node = self.__get_node (word)
        if node: return bool (node.output != nil)
        else: return False

    def match (self, word):
        """
        Checks if word is a prefix of any existing word in the trie.
        """
        return (self.__get_node (word) is not None)


    def make_automation (self):
        """
        Converts trie to Aho-Corasick automaton.
        """
        queue = deque ()
        # 1.
        for i in range (256):
            c = chr (i)
            if c in self.root.children:
                node = self.root.children [c]
                node.fail = self.root
                queue.append (node)
            else:
                self.root.children [c] = self.root
        # 2.
        while queue:
            r = queue.popleft ()
            for node in r.children.values ():
                queue.append (node)
                state = r.fail
                while node.char not in state.children:
                        state = state.fail
                node.fail = state.children.get (node.char, self.root)

    def iter (self, string):
        """
        Generator performs Aho-Corasick search string algorithm, yielding
        tuples containing two values:
        - position in string
        - outputs associated with matched strings
        """
        state = self.root
        for index, c in enumerate (string):
            while c not in state.children:
                state = state.fail
            state = state.children.get (c, self.root)
            tmp = state
            output = []
            while tmp is not nil:
                if tmp.output is not nil:
                    output.append (tmp.output)
                tmp = tmp.fail
            if output: yield (index, output)

    def iter_long (self, string):
        """
        Generator performs a modified Aho-Corasick search string algorithm,
        which maches only the longest word.
        """
        state = self.root
        last  = None
        index = 0
        while index < len (string):
            c = string [index]
            if c in state.children:
                state = state.children [c]
                if state.output is not nil:
                    # save the last node on the path
                    last = (state.output, index)
                index += 1
            else:
                # return the saved match
                if last:
                    yield last
                    # and start over, as we don't want overlapped results
                    # Note: this leads to quadratic complexity in the worst case
                    index = last [1] + 1
                    state = self.root
                    last  = None
                else:
                    # if no output, perform classic Aho-Corasick algorithm
                    while c not in state.children:
                        state = state.fail
        # corner case
        if last:
            yield last

    def find_all (self, string, callback):
        """
        Wrapper on iter method, callback gets an iterator result
        """
        for index, output in self.iter (string):
            callback (index, output)

"""
Demonstration of work
#####################
words = ['a', 'ab', 'abc', 'bc', 'c', 'cba']
t = Trie ()
for w in words:
    t.add_word (w, w)
s = "caaab"
t.make_automation ()
for res in t.iter (s):
    print
    print ('%s' % s)
    pos, matches = res
    for fragment in matches:
        print ('%s%s' % ((pos - len (fragment) + 1) * ' ', fragment))
"""

def determiningDNAhealth (n, g, h, fldL):
    mn = maxsize; mx = 0
    t = Trie ()
    for i in range (n):
        gen = g [i]
        t.add_word (gen, (gen, i, h [i]))
    t.make_automation ()
    print ("root created")

    for f, l, d in fldL:
        ln = len (d)
        sm = 0
        for pos, matches in t.iter (d):
            for match in matches:
#                print ("match", match)
                for gen, ix, h in match:
#                    print (gen, ' ' * (4 - len (gen)), pos, ix, h)
                    if ix >= f and ix <= l: sm += h
#        print (t.get ("b"))
#        t.find_all (d, print)
        mn = min (sm, mn)
        mx = max (sm, mx)
    return str (mn) + " " + str (mx)

def main ():
    fptr = open (environ ['OUTPUT_PATH'], 'w')
    n = int (input ())
    genes = stdin.readline ().rstrip ().split ()
    health = list (map (int, stdin.readline ().rstrip ().split ()))
    s = int (input ())
    fldL = []
    for _ in range (s):
        [first, last, d] = stdin.readline ().split ()
        fldL.append ((int (first), int (last), d))
    result = determiningDNAhealth (n, genes, health, fldL)
    print (result)
    fptr.write (result + '\n')
    fptr.close ()

if __name__ == '__main__':
    main ()
