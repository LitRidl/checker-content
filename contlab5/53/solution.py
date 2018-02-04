#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Четверичное сложение двоичного и четверичного числа.
через пробел записано два беззнаковых числа произвольной длины первое в двоичной системе счисления, второе в четверичной системе счисления
число в четверичной системе счисления, являющееся суммой исходных чисел
11011 123
'''
from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = int(a, base=2)
intb = int(b, base=4)
result = base_repr(inta + intb, base=4)

print("{0} {1} {2}".format(a, b, result))
