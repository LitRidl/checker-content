#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно выделить предпоследнее шестнадцатиричное число в строке
928357av careful beef\nnothing\naim do 5 -dead man BEEF
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 1:
        return False
    return all(c in hexdigits for c in w)


for line in stdin:
    words = [w.strip() for w in line.strip().split() if len(w.strip()) > 0]
    words = [w.upper() for w in words if word_ok(w)]
    if len(words) > 0:
        ans = words[-2] if len(words) > 1 else words[-1]
        print(ans)
