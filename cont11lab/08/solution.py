#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Раскодировать текст, закодированный по Цезарю с переменным ключом, равным номеру слова в строке
AbCd AbCd AbCd\n0123 0123 0123
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def caesar_char(c, shift):
    alphabet = ascii_lowercase + ascii_uppercase + digits
    a_lower = ascii_lowercase[26 - shift % 26:] + ascii_lowercase[:26 - shift % 26]
    a_upper = ascii_uppercase[26 - shift % 26:] + ascii_uppercase[:26 - shift % 26]
    a_digits = digits[10 - shift % 10:] + digits[:10 - shift % 10]
    table = maketrans(alphabet, a_lower + a_upper + a_digits)
    return c.translate(table)


def caesar(word, shift):
    return ''.join(caesar_char(c, shift) for c in word)

for line in stdin:
    words = [w for w in line.strip().split() if len(w.strip()) > 0]
    if len(words) > 0:
        print(' '.join(caesar(word, shift) for shift, word in enumerate(words)))