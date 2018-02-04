#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
приписать в начало и конец по единице
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
    return sign + '1' + w + '1'


words = stdin.read().strip().split()

for word in words:
    print(f(word))
