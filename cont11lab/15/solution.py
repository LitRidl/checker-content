#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
построчно подсчитать контрольные суммы (сумма кодов знаков, суммирование по модулю 255) всех слов исходного текста
928357av careful\naim do a 1 2
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def cs(w):
    s = 0
    for c in w:
        s = (s + ord(c)) % 255
    return s % 255


for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    if len(words) > 0:
        print(' '.join(str(cs(word)) for word in words))
