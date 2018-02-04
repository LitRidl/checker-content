#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Получение двоичного числа, противоположного данному, в дополнительной кодировке.
записано целое беззнаковое число произвольной длины в двоичной системе счисления
двоичное число, противоположное данному, представленное в дополнительном коде
001001010101111
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()

if a[0] == '0':
    a_copy = '1' + a[1:]
else:
    a_copy = '0' + a[1:]
inta = int(a_copy, base=2)

p = len(base_repr(inta, base=2))

result = base_repr(2 ** (p + 1) - inta, base=2)
print('{0} {1} '.format(a, result))
