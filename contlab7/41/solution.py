#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление троичного логарифма троичного числа.
Входное слово представляет собой беззнаковое троичное число.
троичное число, являющееся двоичным логарифмом исходного числа
1000
'''

from __future__ import print_function
from math import log


def baseb(n, b):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return baseb(e, b) + str(q)

inp = raw_input()
a = long(inp, base = 3)
res = log(a, 3)

print(baseb(int(res), 3))