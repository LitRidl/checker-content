#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного логарифма двоичного числа.
записано беззнаковое число произвольной длины в двоичной системе счисления
двоичное число, двоичный логарифм исходного числа
10000
'''
from __future__ import print_function
from math import log
from numpy import base_repr

a = raw_input().strip()
inta = int(a, base=2)
result = base_repr(int(log(inta, 2)), base=2)

print('{0} {1} '.format(a, result))
