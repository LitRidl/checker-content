#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-итальянски
hgsdf 324 fgd -35\n3 23 77 67ad
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

INT_MAX = 2 ** 31 - 1

def check(w):
    try:
        a = int(w)
        if (17 <= abs(a) <= 77):
            return True
    except:
        pass
    return False

num = {
17: "diciassette",
18: "diciotto",
19: "diciannove",
20: "venti",
21: "Ventuno",
22: "Ventidue",
23: "ventitré",
24: "ventiquattro",
25: "venticinque",
26: "Ventisei",
27: "ventisette",
28: "ventotto",
29: "Ventinove",
30: "trenta",
31: "trentuno",
32: "trentadue",
33: "trentatré",
34: "trentaquattro",
35: "trentacinque",
36: "trentasei",
37: "trentasette",
38: "trentotto",
39: "trentanove",
40: "quaranta",
41: "quarantuno",
42: "Quarantadue",
43: "quarantatre",
44: "quarantaquattro",
45: "quarantacinque",
46: "quarantasei",
47: "quarantasette",
48: "quarantotto",
49: "quarantanove",
50: "cinquanta",
51: "cinquantuno",
52: "fiftytwo",
53: "cinquantatre",
54: "cinquantaquattro",
55: "cinquantacinque",
56: "cinquantasei",
57: "cinquantasette",
58: "cinquantotto",
59: "cinquantanove",
60: "sessanta",
61: "sessantuno",
62: "sessantadue",
63: "sessantatre",
64: "sessantaquattro",
65: "sessantacinque",
66: "sessantasei",
67: "sessantasette",
68: "sessantotto",
69: "sessantanove",
70: "settanta",
71: "settantuno",
72: "settantadue",
73: "settantatre",
74: "settantaquattro",
75: "settantacinque",
76: "settantasei",
77: "settantasette",
}

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "meno "
        w = abs(w)
    wrd += num[w].lower()
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))