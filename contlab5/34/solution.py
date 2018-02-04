#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Получение двоичного числа, противоположного данному, в обратной кодировке.
записано число произвольной длины в двоичной системе счисления
двоичное число, противоположное данному, представленное в обратном коде
-111011
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=2)

if inta == 0:
    result = 0
elif inta < 0:
    result = '0'+ base_repr(-inta, base=2)
else:
    result = ''
    alen = len(base_repr(inta, base=2))
    result = result + base_repr((2**(alen + 1) - inta - 1), base=2)
print("{0} {1}".format(a, result))
