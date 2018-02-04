#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного арифметического сдвига первого числа вправо на число разрядов, равное второму.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, полученное из первого путем арифметического сдвига, с сохранением ведущих нулей
11010 101
'''

from __future__ import print_function

a, b = raw_input().split()
len = len(a)

intb = long(b, base=2)

if intb != 0:
    result = a[:-intb] or ""
    result = result.rjust(len, a[0])
else:
    result = a

print("{0} {1} {2}".format(a, b, result))