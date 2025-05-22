#!/bin/python3

'''
From string 's' find 3 most common letters. Output each of them on a new line, the character followed by the count. Sort this output from most to least, with tiebreakers going IN alphabetical order.
3 <= s <= 100000
'''

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter

def count(s):
    i_am_counting = defaultdict(list)
    cc = [0]
    for ss in set(s):
        i_am_counting[s.count(ss)].append(ss)
        cc.append(s.count(ss))
        i_am_counting[s.count(ss)].sort()
    cc.sort(reverse=True)
    first = i_am_counting[cc[0]]
    second = i_am_counting[cc[1]]
    third = i_am_counting[cc[2]]
    f = i_am_counting[cc[0]][0]
    if first == second:
        s = i_am_counting[cc[1]][1]       
        if first == third:
            t = i_am_counting[cc[2]][2]
        else:
            t = i_am_counting[cc[2]][0]
    elif second == third:
        s = i_am_counting[cc[1]][0]
        t = i_am_counting[cc[2]][1]
    else:
        s = i_am_counting[cc[1]][0]
        t = i_am_counting[cc[2]][0]
    print(f"{f} {cc[0]}\n{s} {cc[1]}\n{t} {cc[2]}")

# Not mine - what does -x[] even mean? I see what it does but how would I guess that or where would i find that information?
def use_counter(s):
    count = Counter(s)
    ss = sorted(count.items(), key= lambda x: (-x[1], x[0]))
    for x in ss[:3]:
        print(x)

if __name__ == '__main__':
    # s = input()
    # s = "bbbaaccdeajjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
    # s = "cbacbaeeeddd"
    # s = "aaaabbbbcccc"
    s = "szrmtbttyyaymadobvwniwmozojggfbtswdiocewnqsjrkimhovimghixqryqgzhgbakpncwupcadwvglmupbexijimonxdowqsjinqzytkooacwkchatuwpsoxwvgrrejkukcvyzbkfnzfvrthmtfvmbppkdebswfpspxnelhqnjlgntqzsprmhcnuomrvuyolvzlni"
    count(s)
    use_counter(s)
