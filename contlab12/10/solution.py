#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
выполнить циклический сдвиг на 3 знака влево десятичного числа
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax

def f(w, n):
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' and w[1:] != '0' else ''
        w = w[1:]
    if len(w) == 1:
        return sign + w
    if len(w) == 2:
        return sign + w[1] + w[0]
    return sign + w[int(n):] + w[:int(n)]


words = stdin.read().strip().split()
shift = 3

for word in words:
    r = f(word, shift)
    if r == '-0':
        r = '0'
    print(r)


