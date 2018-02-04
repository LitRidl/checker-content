#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
распечатать каждое третье двоичное число
928357av -careful 10\nnothing\naim do 110 -10 man +1010 1 010
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def word_ok(w):
    if w[0] in '+-':
        w = w[1:]
    return all(c in '01' for c in w)


text = stdin.read()
words = [w.strip() for w in text.strip().split() if len(w.strip()) > 0]
words = [w for w in words if word_ok(w)]
if len(words) > 0:
    print(*words[::3])
