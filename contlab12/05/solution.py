#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
выбрать цифры, равные модулю разности двух предыдущих
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax
from collections import Counter


def f(w):
    res = []
    if w[0] in '-+':
        w = w[1:]
    if len(w) < 3:
        return res
    i = 0
    while i < len(w):
        if i >= 2:
            x = int(w[i])
            y = int(w[i-1])
            z = int(w[i-2])
            if x == abs(y - z):
                res.append(x)
        i += 1
    return res

words = stdin.read().strip().split()

for word in words:
    print(*f(word))
