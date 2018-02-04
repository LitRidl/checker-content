#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить десятичные целые числа без знака и напечатать суммы их чётных цифр
928357av -careful 1234\nnothing\naim do 05 -150 1A man -17
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *



def word_ok(w):
    # if w[0] in '+-':
    #     w = w[1:]
    return all(c in digits for c in w)


def s(w):
    # if w[0] in '+-':
    #     w = w[1:]
    return sum(int(c) for c in w if c in '02468')


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) > 0:
        print(*[s(w) for w in words])
