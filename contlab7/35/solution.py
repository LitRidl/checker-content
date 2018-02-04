#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Составить алгоритм двоичного подсчёта числа гласных в слове латинского алфавита (букву 'y' считать согласной).
Входное слово представляет собой последовательность малых латинских букв a-z.
двоичное число без ведущих нулей, равное количеству гласных букв во входном слове
icanhazcheeseburger
'''

from __future__ import print_function
from numpy import base_repr

def count_vowels(word):
    return sum(word.count(c) for c in 'aeiou')

try:
    a = raw_input().strip()
except EOFError:
    a = ''

result = base_repr(count_vowels(a), base=2)

print('{0}'.format(result))
