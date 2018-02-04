#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно перевести все целые температуры из шкалы Цельсия C в шкалу Фаренгейта F (например, 100С в 212F. Округление до ближайшего)
928357av 100C 205C\naim C 0C 5c man
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def cs(w):
    return str(int(round(1.8 * int(w[:-1], base=10) + 32))) + 'F'


def work_ok(w):
    if w[0] in '-+':
        w = w[1:]
    return len(w) > 1 and w[-1] == 'C' and all(c in digits for c in w[:-1])


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    words = [w for w in words if work_ok(w)]
    if len(words) > 0:
        print(' '.join(str(cs(word)) for word in words))
