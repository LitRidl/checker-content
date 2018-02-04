#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
удалить все цифры на чётных позициях
1234567\n-192837\n+9\n100\n1111\n268953\n123123\n-0
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
    return sign + (w[::-1][1::2][::-1] or '0')


words = stdin.read().strip().split()

for word in words:
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)

