#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление предиката x<y для двух чисел в алфавите {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
через пробел записано два беззнаковых числа произвольной длины в десятичной системе счисления
1 -- истина, 0 -- ложь
87654321 9876543
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = long(a, base=10)
intb = long(b, base=10)

result = int(inta < intb)

print('{0} {1} {2}'.format(a, b, result))
