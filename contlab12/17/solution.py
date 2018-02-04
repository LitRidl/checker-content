#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
поменять местами первую и последнюю цифры
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
    return sign + (w[-1] + w[1:-1] + w[0]).lstrip('0')


words = stdin.read().strip().split()

for word in words:
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)

