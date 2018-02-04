#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление предиката взаимной простоты двух чисел в натуральной системе счисления.
 через пробел записаны два целых беззнаковых числа произвольной длины в натуральной системе счисления
1 -- если исходные числа взаимно простые, 0 -- если нет
IIIIII III
'''

from __future__ import print_function
from numpy import base_repr



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = raw_input().strip().split()
inta = long(len(a))

intb = long(len(b))

if gcd(inta, intb) <= 1:
    result = 1
else:
    result = 0

print('{0} {1} {2}'.format(a, b, result))
