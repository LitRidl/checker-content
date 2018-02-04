#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество слов с лексикографически возрастащими буквами латинского алфавита (регистр игнорируется: B и b считаются одинаковыми)
928357av careful\naim do man
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


words = [w.lower() for w in stdin.read().split() if len(w.strip()) > 0]
words = [''.join(c for c in w if c in ascii_letters) for w in words]

words_asc = 0

for word in words:
    if len(word) > 0 and all(a < b for a, b in zip(word, word[1:])):
        words_asc += 1

print(words_asc)
