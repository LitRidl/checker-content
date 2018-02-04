#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''ОБРАЗЕЦ
Нормированное вычисление суммы двух двоичных чисел без знака.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число, конъюнкция исходных чисел без ведущих нулей
11010 0111011
'''

from __future__ import print_function


def bit_and(a, b):
    return str(int(a) & int(b))

def bit_or(a, b):
    return str(int(a) | int(b))

def bit_xor(a, b):
    return str(int(a) ^ int(b))


a, b = raw_input().split()
max_len = max(len(a), len(b))

a, b = a.zfill(max_len), b.zfill(max_len)
result = ''.join([bit_and(a_bit, b_bit) for a_bit, b_bit in zip(a, b)]).lstrip('0') or '0'

print(result)
