#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление двоичного логического сдвига второго числа вправо на число разрядов, равное первому.
Через пробел записано два беззнаковых числа произвольной длины (возможно, с ведущими нулями) в двоичной системе счисления, разделенных знаком ">".
двоичное число, результат логического сдвига
11>1001001010
'''

from __future__ import print_function

a, b = raw_input().split('>')
lenb = len(b)

inta = long(a, base=2)

if inta == 0:
    result = b
else:
    result = b[:-inta]

result = result.rjust(lenb, '0')

print(result)
