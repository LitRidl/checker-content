#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного логического сдвига первого числа вправо на число разрядов, равное второму.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления, возможно с ведущими нулями
двоичное число, полученное из первого путем логического сдвига
11010 011
'''

from __future__ import print_function

a, b = raw_input().split()
intb = long(b, base=2)
lena = len(a)

if intb == 0:
    result = a
else:
    result = a[:-intb]

result = result.rjust(lena, '0')

print("{0} {1} {2}".format(a, b, result))