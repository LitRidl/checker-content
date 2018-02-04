#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
после каждых двух цифр (не внахлёст) вставить абсолютное значение их разности
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax


def f(w):
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' and w[1:] != '0' else ''
        w = w[1:]
    if len(w) < 2:
        return sign + w
    w = w[::-1]
    bi = zip(w[::2], w[1::2])
    res = []
    for x, y in bi:
        res.append(x + y + str(abs(int(x) - int(y))))
    return sign + (((w[-1] if len(w) % 2 else '') + ''.join(r[::-1] for r in res[::-1])).lstrip('0') or '0')


words = stdin.read().strip().split()

for word in words:
    print(f(word))
