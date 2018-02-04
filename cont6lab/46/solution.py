#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление факториала числа в троичной системе счисления.
записано целое беззнаковое число произвольной длины в троичной системе счисления.
число в троичной системе счисления, равное факториалу исходного числа
21
'''


from __future__ import print_function
from numpy import base_repr

def fact(inta):
    if (inta == 0):
        return 1
    res = 1
    while (inta != 1):
        res *= inta
        inta -= 1
    return res


a = raw_input().strip()
inta = long(a, base=3)

result = base_repr(fact(inta), base=3).strip()

print('{0} {1}'.format(a, result))
