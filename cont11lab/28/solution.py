#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить первое и последнее (по счету) десятичные числа строк текста
928357av -careful 1234\nnothing\naim do 05 -150 man -19
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    if w == '':
        return False
    return all(c in digits for c in w)


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) > 0:
        print(words[0], words[-1])
