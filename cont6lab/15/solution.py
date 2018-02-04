#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Деление двух неотрицательных десятичных чисел.
через пробел записаны два целых беззнаковых числа произвольной длины в десятичной системе счисления
целая часть числа, являющееся результатом деления первого числа на второе; если второе число равно 0, то вывести 0
3086412 5684
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().strip().split()
inta = long(a)

intb = long(b)

if intb == 0:
    result = '0'
else:
    result = (inta / intb)

print('{0} {1} {2}'.format(a, b, result))
