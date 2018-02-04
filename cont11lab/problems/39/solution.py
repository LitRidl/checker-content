#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
посчитать количество шестнадцатеричных слов в строке, изображающих отрицательные числа в 64-битной архитектуре (изображеним отрицательного 16-ричного числа считаются числа, лежащие во второй части числового диапазона и не имеющие знака)
F163A7F34DC53790 +5ABCDEAAAAAAAAAA 6sdg ashdg\n6543264321AEFC00 -234\n8000000000000000 -8FFFFFFFFFFFFFFF
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *


def check(w):
    try:
        a = long(w, base = 16)
        if (len(w) == 16 and long(w[0], base = 16)):
            return True
    except:
        pass
    return False

for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    print(len(words))
