#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Подсчет числа различных букв слова в латинском алфавите.
записано слово в латинском алфавите
число различных букв слова исходного слова
AbdaanhhH
'''

from __future__ import print_function
from numpy import base_repr

a = raw_input().strip()

print('{0} {1}'.format(a, len(set(a.lower()))))
