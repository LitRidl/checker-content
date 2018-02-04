#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из двоичной системы счисления в шестнадцатиричную (логарифмическая сложность).
записано целое беззнаковое число произвольной длины в двоичной системе счисления, возможно с ведущими нулями
число в шестнадцатиричной системе счисления, номинально равное исходному без ведущих нулей
0100011110101
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=2)

result = base_repr(inta, base=16).strip()

print('{0} {1}'.format(a, result))
