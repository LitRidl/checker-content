#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление разности двух двоичных чисел без знака, при условии, что первое число больше второго с логарифмической сложностью.
через пробел записано два беззнаковых числа произвольной длины в двоичной системе счисления
двоичное число без ведущих нулей, являющееся разностью исходных чисел
111011 11010
'''
from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = int(a, base=2)
intb = int(b, base=2)
result = base_repr(inta - intb, base=2)

print("{0} {1} {2}".format(a, b, result))
