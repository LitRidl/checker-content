#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Реверс девятеричного числа со знаком.
записано число произвольной длины в девятеричной системе счисления, возможно со знаком и ведущими нулями
реверсированная копия значимой части исходного числа с сохранением знака без ведущих нулей и знака +
-870322100
'''
from __future__ import print_function
from numpy import base_repr

a = raw_input()

if a[0] == '-':
    result = a[0] + base_repr(long(a[:0:-1], 9), base=9)
elif a[0] == '+':
    result = base_repr(long(a[:0:-1], 9), base=9)
else:
    result = base_repr(long(a[::-1], 9), base=9)

a = a.rstrip()

print('{0} {1}'.format(a, result))