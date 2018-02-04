#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
получить восьмиричное-кодированное десятичное представление числа
1234567\n-192837\n+9\n100\n1111\n268953\n123123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax

code = {
    '0': '00',
    '1': '01',
    '2': '02',
    '3': '03',
    '4': '04',
    '5': '05',
    '6': '06',
    '7': '07',
    '8': '10',
    '9': '11'
}

def f(w):
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' and w[1:] != '0' else ''
        w = w[1:]
    return sign + ''.join(code[d] for d in w)


words = stdin.read().strip().split()

for word in words:
    print(f(word))