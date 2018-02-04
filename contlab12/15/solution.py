#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
проверить, все ли цифры в смежных разрядах различны
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax


def f(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 2:
        return True
    return all(a != b for a, b in zip(w, w[1:]))

words = stdin.read().strip().split()

for word in words:
    print('True' if f(word) else 'False')

