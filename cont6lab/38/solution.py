#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление логического произведения (&amp;&amp; в Си) двоичных чисел.
через пробел записано два беззнаковых числа произвольной равной длины в двоичной системе счисления
0 или 1 -- результат логического произведения
11010 111011
'''

from __future__ import print_function
from numpy import base_repr

a, b = raw_input().split()
inta = long(a, base=2)
intb = long(b, base=2)

result = int(inta * intb != 0)

print('{0} {1} {2}'.format(a, b, result))
