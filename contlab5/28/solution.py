#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Натурализация двоичного числа в позиционной записи (перевод в натуральную систему счисления).
записано беззнаковое число произвольной длины в двоичной системе счисления
число в натуральной системе счисления
11011
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = int(a, base=2)
result = '|' * inta

print('{0} {1} '.format(a, result))
