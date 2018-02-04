#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить беззнаковые восьмеричные числа и напечатать их цифры в двоичной системе
928357av -careful 1234\nnothing\naim do 05 -150 19 man -17
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *



def word_ok(w):
    return all(c in '01234567' for c in w)


def digs(w):
    m = ['000', '001', '010', '011', '100', '101', '110', '111']
    if w[0] in '+-':
        w = w[1:]
    res = ''
    for c in w:
        res += m[int(c, base=10)]
    return res


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) > 0:
        print(*[digs(w) for w in words])
