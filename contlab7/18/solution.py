#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление поразрядной дизъюнкции исходных чисел.
Входное слово представляет собой два беззнаковых двоичных числа (возможно, с ведущими нулями), разделенные знаком "|".
двоичное число, результат поразрядной дизъюнкции
100010|110011
'''

from __future__ import print_function
from numpy import base_repr

def bit_or(a, b):
    return int(int(a) | int(b))

a, b = raw_input().split('|')
inta = int(a, base=2)
intb = int(b, base=2)

result = base_repr(bit_or(inta, intb), base=2)

print (result)