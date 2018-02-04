#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно напечатать значения пятеричных чисел, не являющихся троичными числами, в десятичной системе
nan 13  011\n56 b10 -40
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    return all(c in '01234' for c in w) and ('3' in w or '4' in w)


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    words = [int(w, base=5) for w in words if word_ok(w)]
    if len(words) > 0:
        print(' '.join(str(w) for w in words))
