#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Возведение двоичного числа в квадрат.
записано целое беззнаковое число произвольной длины в двоичной системе счисления.
число в двоичной системе счисления, номинально равное квадрату исходного числа
101
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()
inta = long(a, base=2)

result = base_repr(inta * inta, base=2).strip()

print('{0} {1}'.format(a, result))
