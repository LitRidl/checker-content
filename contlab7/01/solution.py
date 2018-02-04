#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм вычисления суммы двух троичных чисел.
Входное слово представляет собой два беззнаковых троичных числа (возможно, с ведущими нулями), разделённые знаком "+".
троичное число, сумма двух троичных чисел без ведущих нулей
0010+221
'''

from __future__ import print_function
from numpy import base_repr

a, b = [long(x, base=3) for x in raw_input().strip().split('+')]
result = base_repr(a + b, base=3)

print('{0}'.format(result))
