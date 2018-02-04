#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
перенести ведущие нули десятичного представления в младшие разряды. Условимся считать, что в число помещаеся 10 разрядов; если разрядов меньше, то недостающие разряды -- ведущие нули.
-1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def f(w):
    n = 0
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' else ''
        w = w[1:]
    while (w[n] == "0" and n != len(w) - 1):
        n += 1
    return sign + w[n:] + "0" * n


words = stdin.read().strip().split()

for word in words:
    sign = ''
    if word[0] in '+-':
        sign = '-' if word[0] == '-' else ''
        word = word[1:]
    word = word.rjust(10, '0')
    word = sign + word
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)
