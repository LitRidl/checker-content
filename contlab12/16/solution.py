#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
проверить, есть ли цифры, не встречающиеся ни разу
1234567\n-192837\n+9\n100\n1111\n268953\n1234567809
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax


def f(w):
    if w[0] in '+-':
        w = w[1:]
    if len(w) < 1:
        return True
    return not all(d in w for d in '0123456789')


words = stdin.read().strip().split()

for word in words:
    print('True' if f(word) else 'False')
