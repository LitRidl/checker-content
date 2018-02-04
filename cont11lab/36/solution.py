#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-испански
hgsdf 324 fgd -35\n3 22 77 67ad
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
17: "diecisiete",
18: "dieciocho",
19: "diecinueve",
20: "veinte",
21: "veintiún",
22: "veintidós",
23: "veintitrés",
24: "veinticuatro",
25: "veinticinco",
26: "veintiséis",
27: "veintisiete",
28: "veintiocho",
29: "veintinueve",
30: "treinta",
31: "treinta y uno",
32: "treinta y dos",
33: "treinta y tres",
34: "treinta y cuatro",
35: "treinta y cinco",
36: "treinta y seis",
37: "treinta y siete",
38: "treinta y ocho",
39: "treinta y nueve",
40: "cuarenta",
41: "cuarenta y uno",
42: "cuarenta y dos",
43: "cuarenta y tres",
44: "cuarenta y cuatro",
45: "Cuarenta y cinco",
46: "cuarenta y seis",
47: "cuarenta y siete",
48: "cuarenta y ocho",
49: "cuarenta y nueve",
50: "cincuenta",
51: "cincuenta y uno",
52: "cincuenta y dos",
53: "cincuenta y tres",
54: "cincuenta y cuatro",
55: "cincuenta y cinco",
56: "cincuenta y seis",
57: "cincuenta y siete",
58: "cincuenta y ocho",
59: "cincuenta y nueve",
60: "sesenta",
61: "sesenta y uno",
62: "sesenta y dos",
63: "sesenta y tres",
64: "sesenta y cuatro",
65: "sesenta y cinco",
66: "sesenta y seis",
67: "sesenta y siete",
68: "sesenta y ocho",
69: "sesenta y nueve",
70: "setenta",
71: "setenta y uno",
72: "setenta y dos",
73: "setenta y tres",
74: "setenta y cuatro",
75: "setenta y cinco",
76: "setenta y seis",
77: "setenta y siete",
}

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "menos "
        w = abs(w)
    wrd += num[w].lower()
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))