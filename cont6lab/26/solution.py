#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление поразрядной конъюнкции двух двоичных чисел (слова одинаковой длины).
через пробел записано два беззнаковых числа произвольной равной длины в двоичной системе счисления
двоичное число, результат поразрядной конъюнкции исходных чисел без ведущих нулей
110100 111011
'''

from __future__ import print_function
from numpy import base_repr

def bit_and(a, b):
    return int(a) & int(b)

def bit_or(a, b):
    return str(int(a) | int(b))

def bit_xor(a, b):
    return str(int(a) ^ int(b))

a, b = raw_input().split()
inta = long(a, base=2)
intb = long(b, base=2)

result = base_repr(bit_and(inta, intb), base=2)

print('{0} {1} {2}'.format(a, b, result))
