#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из шестнадцатиричной системы счисления в двоичную.
записано целое беззнаковое число произвольной длины в шестнадцатиричной системе счисления, возможно с ведущими нулями
число в двоичной системе счисления, номинально равное исходному без ведущих нулей
40BA0F2
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input()
inta = long(a, base=16)

result = base_repr(inta, base=2)

print('{0} {1}'.format(a, result))