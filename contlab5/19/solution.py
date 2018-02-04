#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного циклического сдвига первого числа вправо на число разрядов, равное второму.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, полученное из первого путем циклического сдвига, с сохранением ведущих нулей
11010 101
'''

from __future__ import print_function

a, b = raw_input().split()
intb = long(b, base=2)
lenght = len(a)

shift = intb % lenght
if shift == 0:
    result = a
else:
    result = a[lenght - shift:] + a[:-shift]

print("{0} {1} {2}".format(a, b, result))