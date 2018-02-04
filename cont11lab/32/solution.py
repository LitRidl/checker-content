#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
Выделить все дясятичные числа от 17 до 77 по модулю и распечатать их значения в словесной форме по-русски
hgsdf 324 fgd -34\n3 77 67ad
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

def check(w):
    try:
        a = int(w)
        if (17 <= abs(a) <= 77):
            return True
    except:
        pass
    return False

def print_num(w):
    w = int(w)
    wrd = ""
    if (w < 0):
        wrd += "минус "
        w = abs(w)
    if (w == 17):
        return wrd + "семнадцать"
    elif (w == 18):
        return wrd + "восемнадцать"
    elif (w == 19):
        return wrd + "девятнадцать"
    a = w // 10
    if (a == 2):
        wrd += "двадцать"
    elif (a == 3):
        wrd += "тридцать"
    elif (a == 4):
        wrd += "сорок"
    elif (a == 5):
        wrd += "пятьдесят"
    elif (a == 6):
        wrd += "шестьдесят"
    elif (a == 7):
        wrd += "семьдесят"

    a = w % 10

    if (a == 1):
        wrd += " один"
    if (a == 2):
        wrd += " два"
    elif (a == 3):
        wrd += " три"
    elif (a == 4):
        wrd += " четыре"
    elif (a == 5):
        wrd += " пять"
    elif (a == 6):
        wrd += " шесть"
    elif (a == 7):
        wrd += " семь"
    elif (a == 8):
        wrd += " восемь"
    elif (a == 9):
        wrd += " девять"
    return wrd


for line in stdin:
    words = [w for w in line.strip().split() if check(w)]
    if(len(words) > 0):
        print(' '.join(print_num(w) for w in words))