#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
проверить, есть ли одинаковые цифры в смежных разрядах
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax


def f(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 2:
        return False
    return any(a == b for a, b in zip(w, w[1:]))


words = stdin.read().strip().split()

for word in words:
    print('True' if f(word) else 'False')
