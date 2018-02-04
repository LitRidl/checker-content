#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычиcление двоичного логарифма двочичного числа.
Входное слово представляет собой беззнаковое двоичное число.
двоичное число, являющееся двоичным логарифмом исходного числа
100000
'''

from __future__ import print_function
from math import log

str = raw_input()
a = long(str, base = 2)
res = log(a, 2)
print(bin(int(res))[2:])