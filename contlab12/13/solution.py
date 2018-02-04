#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
перенести ведущие нули десятичного представления в середину двоичной записи числа. Условимся считать, что в число помещаеся 10 разрядов; если разрядов меньше, то недостающие разряды -- ведущие нули.
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import base_repr


def f(w):
    n = 0
    sign = ''
    if w[0] in '+-':
        sign = '-' if w[0] == '-' else ''
        w = w[1:]
    intw = long(w, base=10)
    res = str(base_repr(intw, base=2))
    while (w[n] == "0" and n != len(w) - 1):
        n += 1
    return sign + res[:len(res)//2] + "0" * n + res[len(res)//2:]


words = stdin.read().strip().split()

for word in words:
    if word[0] in '+-':
        sign = '-' if word[0] == '-' else ''
        word = word[1:]
    word = word.rjust(10, '0')
    r = f(word)
    if r == '-0':
        r = '0'
    print(r)