#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из четверичной системы счисления в шестнадцатиричную.
записано целое беззнаковое число произвольной длины в четверичной системе счисления, возможно с ведущими нулями
число в шестнадцатиричной системе счисления, номинально равное исходному без ведущих нулей
00123210021
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=4)

result = base_repr(inta, base=16).strip()

print('{0} {1}'.format(a, result))
