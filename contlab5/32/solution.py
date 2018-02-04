#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Уменьшение на единицу целого неотрицательного числа в восьмеричной системе счисления.
целое неотрицательное число произвольной длины в восьмеричной системе счисления
целое число в восьмеричной системе счисления, результат декрементирования исходного
0
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=8)

result = base_repr(inta - 1, base=8)

print("{0} {1}".format(a, result))
