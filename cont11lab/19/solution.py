#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
перевести все мерные длины из дюймов(in) в миллиметры(mm). Например: 10in -> 254mm
28147326av 100in 205in\naim in 0in 5IN man
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def cs(w):
    return str(int(round(25.4 * int(w[:-2], base=10)))) + 'mm'


def work_ok(w):
    if w[0] in '-+':
        w = w[1:]
    return len(w) > 2 and w[-1] == 'n' and w[-2] =="i" and all(c in digits for c in w[:-2])


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if work_ok(w)]
    if len(words) > 0:
        print(' '.join(str(cs(word)) for word in words))
