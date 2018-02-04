#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
инкрементировать (увеличить на единицу) все четные цифры
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax

def t(d):
    if d in '02468':
        return str(int(d) + 1)
    return d

def f(w):
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' and w[1:] != '0' else ''
        w = w[1:]
    return sign + (''.join(t(d) for d in w) or '0')


words = stdin.read().strip().split()

for word in words:
    print(f(word))
