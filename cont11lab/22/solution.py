#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
подсчитать количество слов, содержащих не менее 3-х знаков
928357av car careful\naim do man
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


words = [w for w in stdin.read().split() if len(w.strip()) > 0]
qty = 0

for word in words:
    if len(word) >= 3:
        qty += 1

print(qty)
