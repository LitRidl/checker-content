#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм подсчёта количества десятеричных чисел.
Входное слово представляет собой произвольную непустую последовательность беззнаковых десятичных чисел, разделённых знаком "#".
количество десятичных чисел, записанное в двоичной системе счисления
013#123#0#1000000
'''

from __future__ import print_function
from numpy import base_repr

nums = [long(x, base=10) for x in raw_input().strip().split('#')]
result = base_repr(len(nums), base=2)

print('{0}'.format(result))
