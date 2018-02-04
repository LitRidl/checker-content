#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Реверс троичного числа со знаком.
записано число произвольной длины в троичной системе счисления
реверсированная копия значимой части исходного числа с сохранением знака без ведущих нулей и знака +
-102100
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()

if a[0] == '-':
    result = a[0] + base_repr(long(a[:0:-1], 3), base=3)
elif a[0] == '+':
    result = base_repr(long(a[:0:-1], 3), base=3)
else:
    result = base_repr(long(a[::-1], 3), base=3)

print("{0} {1}".format(a, result))
