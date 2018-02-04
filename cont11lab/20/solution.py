#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
перевести все мерные расстояние из миль(mi) в километры(km). Например: 1000mi -> 1609km
28147326av 100mi 205mi\nami in 0mi 5MI man 1000mi
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def cs(w):
    return str(int(round(1.609 * int(w[:-2], base=10)))) + 'km'


def work_ok(w):
    if w[0] in '-+':
        w = w[1:]
    return len(w) > 2 and w[-1] == 'i' and w[-2] =="m" and all(c in digits for c in w[:-2])


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if work_ok(w)]
    if len(words) > 0:
        print(' '.join(str(cs(word)) for word in words))
