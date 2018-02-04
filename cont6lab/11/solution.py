#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из шестнадцатиричной системы счисления в четверичную (логарифмическая сложность).
записано целое беззнаковое число произвольной длины в шестнадцатиричной системе счисления, возможно с ведущими нулями
число в четверичной системе счисления, номинально равное исходному без ведущих нулей
C352F0
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=16)

result = base_repr(inta, base=4).strip()

print('{0} {1}'.format(a, result))
