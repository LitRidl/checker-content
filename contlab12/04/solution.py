#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
выбрать цифры, равные сумме двух предыдущих
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax
from collections import Counter


def f(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 3:
        return [] # [w]
    tri = zip(w[0:], w[1:], w[2:])[::-1]
    return [x for x, y, z in tri if int(x) == int(y) + int(z)]


words = stdin.read().strip().split()

for word in words:
    print(*f(word))
