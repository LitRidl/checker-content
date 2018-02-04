#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить все одиннадцатеричные числа с лексикографическим возрастанием цифр
nan 31 10A 012\n756 b10 -1A 5
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    return all(c in (digits + 'aA') for c in w) and all(a < b for a, b in zip(w, w[1:]))


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    words = [w.upper() for w in words if word_ok(w)]
    if len(words) > 0:
        print(' '.join(words))
