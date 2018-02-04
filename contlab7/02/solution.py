#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм вычисления разности двух троичных чисел.
Входное слово представляет собой два безннаковых троичных числа (возможно, с ведущими нулями), разделённые знаком "-", причём первое число не меньше второго
троичное число, разность двух троичных чисел без ведущих нулей
210-011
'''

from __future__ import print_function
from numpy import base_repr

a, b = [long(x, base=3) for x in raw_input().strip().split('-')]
result = base_repr(a - b, base=3)

print('{0}'.format(result))
