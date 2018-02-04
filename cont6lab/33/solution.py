#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Уменьшение на единицу целого неотрицательного числа в шестнадцатиричной системе счисления.
записано целое неотрицательное число произвольной длины в шестнадцатиричной системе счисления
целое число в шестнадцатичной системе счисления, результат декрементирования исходного
1000
'''

from __future__ import print_function
from numpy import base_repr


a = raw_input()
inta = long(a, base=16)

result = base_repr(inta - 1, base=16)

print('{0} {1}'.format(a, result))