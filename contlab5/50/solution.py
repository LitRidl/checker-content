#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Перевод числа из девятиричной системы счисления в троичную с логарифмической сложностью.
записано целое беззнаковое число произвольной длины в девятиричной системе счисления
число в троичной системе счисления, номинально равное исходному
238046157
'''
from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = int(a, base=9)

result = base_repr(inta, base=3)

print("{0} {1}".format(a, result))
