#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из шестнадцатиричной системы счисления в двоичную (логарифмическая сложность).
записано целое беззнаковое число произвольной длины в шестнадцатиричной системе счисления, возможно с ведущими нулями
число в двоичной системе счисления, номинально равное исходному без ведущих нулей
3D46
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=16)

result = base_repr(inta, base=2).strip()

print('{0} {1}'.format(a, result))
