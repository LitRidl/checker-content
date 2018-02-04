#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление НОД (наибольшего общего делителя) двух двоичных чисел.
через пробел записано два беззнаковых числа произвольной длины без ведущих нулей в двоичной системе счисления
НОД двух чисел, записанный в двоичной системе счисления без ведущих нулей
10101 1111
'''

from __future__ import print_function
from numpy import base_repr
from fractions import gcd

a, b = raw_input().split()
inta = long(a, base=2)
intb = long(b, base=2)

result = base_repr(gcd(inta, intb), base=2)

print('{0} {1} {2}'.format(a, b, result))
