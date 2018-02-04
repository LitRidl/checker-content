#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм кодирования слова в латинском алфавите по Цезарю со сдвигом, равным 13 (см. шифр rot13).
Входное слово представляет собой последовательность малых латинских букв a-z.
последовательность малых латинских букв, полученная из исходной путём применения шифра rot13
icanhazcheeseburger
'''

from __future__ import print_function
from numpy import base_repr

try:
    a = raw_input().strip()
except EOFError:
    a = ''

result = a.encode('rot_13')

print('{0}'.format(result))
