#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Вычисление предиката "u подслово w" в латинском алфавите.
через пробел записаны два слова произвольной длины в латинском алфавите
1 -- если первое слово является подсловом второго, 0 -- если нет
aabb abaabbab
'''

from __future__ import print_function


a, b = raw_input().strip().split()

if a in b:
    result = 1
else:
    result = 0

print('{0} {1} {2}'.format(a, b, result))
