#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление разности двух десятичных чисел без знака, при условии, что первое число больше второго.
через пробел записаны два беззнаковых числа произвольной длины в десятичной системе счисления
десятичное число, разность исходных чисел без ведущих нулей
87654321 9876543
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = long(a, base=10)
intb = long(b, base=10)

if inta <= intb:
    raise Exception('inta <= intb!')

result = base_repr(inta - intb, base=10)

print('{0} {1} {2}'.format(a, b, result))

