#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''ОБРАЗЕЦ
выбрать тройки идущих подряд цифр числа, сумма которых максимальная
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax


def f(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 3:
        return [] # [w]
    tri = zip(w[0:], w[1:], w[2:])[::-1]
    tri_i = [int(x) + int(y) + int(z) for x, y, z in tri]
    idxs = argwhere(tri_i == amax(tri_i))
    return [''.join(str(x) for x in tri[idx]) for idx in idxs]


words = stdin.read().strip().split()

for word in words:
    print(*f(word))
