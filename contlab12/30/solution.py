#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
попарно упорядочить цифры числа по возрастанию
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
    if len(w) == 1:
        return sign + w
    i = 1
    res = ''
    while i < len(w):
        if int(w[i-1]) < int(w[i]):
            res += w[i-1] + w[i]
        else:
            res += w[i] + w[i-1]
        i += 2
    if len(w) % 2 != 0:
        res += w[len(w) - 1]
    return sign + res



words = stdin.read().strip().split()

for word in words:
    r = f(word).lstrip('0') or '0'
    if r == '-0':
        r = '0'
    print(r)
