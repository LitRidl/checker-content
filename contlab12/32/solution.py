#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
проверить, содержит ли число равные количества нулей и единиц в машинном представлении
1234567
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *
from numpy import argmax, argwhere, amax

def f(s):
    zcount = 0
    ucount = 0
    for c in s:
        if c == '1': ucount += 1
        if c == '0': zcount += 1
    if ucount == zcount:
        return True
    else:
        return False

def g(s):
    res = ''
    for c in s:
        if c == '1': res += '0'
        else: res += '1'
    return '1' + res



words = stdin.read().strip().split()

for word in words:
    if word[0] in '-':
        word = word[3:]
        word = g(word)
    else:
        word = word[2:]
    print('True' if f(g(word)) else 'False')



