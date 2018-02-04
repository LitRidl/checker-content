#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''ОБРАЗЕЦ
Составить алгоритм вычисления суммы двух троичных чисел.
входное слово представляет собой два троичных числа (возможно, с ведущими нулями) без знака, разделённые знаком "+"
троичное число, сумма двух троичных чисел без ведущих нулей
0010 221
'''

from __future__ import print_function
from numpy import base_repr

a, b = [long(x, base=3) for x in raw_input().strip().split('+')]
result = base_repr(a + b, base=3)

print('{0}'.format(result))
