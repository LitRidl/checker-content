#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление поразрядной дизъюнкции двух двоичных чисел без знака.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, поразрядной дизъюнкция исходных чисел без ведущих нулей
11010 111011
'''

from __future__ import print_function
from numpy import base_repr

def bit_and(a, b):
    return int(a) & int(b)

def bit_or(a, b):
    return int(int(a) | int(b))

def bit_xor(a, b):
    return str(int(a) ^ int(b))

a, b = raw_input().split()
inta = int(a, base=2)
intb = int(b, base=2)

result = base_repr(bit_or(inta, intb), base=2)

print('{0} {1} {2}'.format(a, b, result))
