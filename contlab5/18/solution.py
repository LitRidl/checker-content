#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного циклического сдвига второго числа влево на число разрядов, равное первому.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, полученное из второго путем циклического сдвига, с сохранением ведущих нулей
101 11010
'''

from __future__ import print_function

a, b = raw_input().split()
inta = long(a, base=2)
shift = inta % len(b)

if shift == 0:
    result = b
else:
    result = b[shift:] + b[0:shift]

print("{0} {1} {2}".format(a, b, result))