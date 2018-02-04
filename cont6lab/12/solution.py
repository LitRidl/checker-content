#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление произведения двух неотрицательных чискл в шестнадцетеричной системе счисления.
через пробел записаны два целых беззнаковых числа произвольной длины в шестнадцатиричной системе счисления, возможно с ведущими нулями
число являющееся произведением исходных чисел без ведущих нулей
65D899 C3007D4
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().strip().split()
inta = long(a, base=16)

intb = long(b, base=16)

result = base_repr(inta * intb, base=16).strip()

print('{0} {1} {2}'.format(a, b, result))
