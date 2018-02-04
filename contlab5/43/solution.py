#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из двоичной системы счисления в восьмеричную.
записано целое беззнаковое число произвольной длины в двоичной системе счисления
число в восьмеричной системе счисления, номинально равное исходному
0111011
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=2)

result = base_repr(inta, base=8)

print("{0} {1}".format(a, result))