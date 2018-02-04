#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Нормированное вычисление суммы двух двоичных чисел без знака.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, сумма исходных чисел без ведущих нулей
11010 111011
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = long(a, base=2)
intb = long(b, base=2)

result = base_repr(inta + intb, base=2)

print("{0} {1} {2}".format(a, b, result))
