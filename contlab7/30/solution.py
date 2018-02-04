#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм вычисления логического произведения (&amp;&amp; в Си) двух беззнаковых двоичных чисел.
Входное слово представляет собой два двоичных числа (возможно, с ведущими нулями), разделённых символом "&amp;&amp;".
двоичное число 0 или 1, результат логического произведения исходных чисел
0010&&10101
'''

from __future__ import print_function
from numpy import base_repr

a, b = [long(x, base=2) for x in raw_input().strip().split('&&')]
result = '1' if a > 0 and b > 0 else '0'

print('{0}'.format(result))
