#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить предпоследнее десятичное число и вычислить сумму его цифр
928357av -careful 1234\nnothing\naim do 5 150 man -1234
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) == 0:
        return False
    return all(c in digits for c in w)


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if word_ok(w)]
    if len(words) >= 2:
        ans = words[-2]
        print(sum(int(c, base=10) for c in ans if c in digits))
