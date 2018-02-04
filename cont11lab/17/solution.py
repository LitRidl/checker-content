#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить все числа, записанные в троичной системе счисления и кратные 3
nan 12 120 031\n56 b10 -1000
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) == 0:
        return False
    return all(c in '012' for c in w) and w[-1] == '0'


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) > 0:
        print(' '.join(str(w) for w in words))
