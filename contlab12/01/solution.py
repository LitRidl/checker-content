#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
удалить среднюю цифру числа
1234567
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
    if len(w) % 2 == 0:
        return sign + w
    return sign + w[:int(len(w)/2)] + w[int(len(w)/2) + 1:]


words = stdin.read().strip().split()

for word in words:
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)