#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Нахождение максимального числа в последовательности.
через пробел записаны три числа в двоичной системе счисления.
максимальное число последовательности в двоичной системе счисления без ведущих нулей
101 110 0
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()

b = []

for i in a.split():
    b.append(long(i, base=2))


result = base_repr(max(b), base = 2).strip()

print('{0} {1}'.format(a, result))
