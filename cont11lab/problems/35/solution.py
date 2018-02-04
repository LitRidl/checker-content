#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-французскин
hgsdf 324 fgd -35\n3 77 67ad
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

INT_MAX = 2 ** 31 - 1

def check(w):
    try:
        a = long(w)
        if (17 <= abs(a) <= 77):
            return True
    except:
        pass
    return False

num = {
17: "dix-sept",
18: "dix-huit",
19: "dix-neuf",
20: "vingt",
21: "vingt et un",
22: "vingt-deux",
23: "vingt-trois",
24: "vingt-quatre",
25: "vingt-cinq",
26: "vingt-six",
27: "vingt-sept",
28: "vingt-huit",
29: "vingt-neuf",
30: "trente",
31: "trente et un",
32: "trente-deux",
33: "trente-trois",
34: "trente-quatre",
35: "trente-cinq",
36: "trente-six",
37: "trente-sept",
38: "trente-huit",
39: "trente-neuf",
40: "quarante",
41: "quarante et un",
42: "quarante-deux",
43: "quarante-trois",
44: "quarante-quatre",
45: "quarante-cinq",
46: "quarante-six",
47: "quarante-sept",
48: "quarante-huit",
49: "quarante-neuf",
50: "cinquante",
51: "cinquante et un",
52: "cinquante-deux",
53: "cinquante-trois",
54: "cinquante-quatre",
55: "cinquante-cinq",
56: "cinquante-six",
57: "cinquante-sept",
58: "cinquante-huit",
59: "cinquante-neuf",
60: "soixante",
61: "soixante et un",
62: "soixante-deux",
63: "soixante trois",
64: "soixante-quatre",
65: "soixante-cinq",
66: "soixante-six",
67: "soixante-sept",
68: "soixante-huit",
69: "soixante-neuf",
70: "soixante-dix",
71: "soixante et onze",
72: "soixante-douze",
74: "soixante-treize",
74: "soixante-quatorze",
75: "soixante-quinze",
76: "soixante-seize",
77: "soixante dix-sept",
}

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "moins "
        w = abs(w)
    wrd += num[w].lower()
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))