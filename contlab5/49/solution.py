#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из троичной системы счисления в девятиричную с логарифмической сложностью.
записано целое беззнаковое число произвольной длины в троичной системе счисления
число в девятеричной системе счисления, номинально равное исходному
12211011
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = int(a, base=3)

result = base_repr(inta, base=9)

print("{0} {1}".format(a, result))
