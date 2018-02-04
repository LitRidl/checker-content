#!/usr/bin/python
# -*- coding: utf-8 -*-

u'''
посчитать среднюю длину слова в тексте, закодированном в UTF-8 (округлить до близжайшего целого, в большую, если близжайшего нет)
4367а компьютер абв\nКод СИ
'''

from __future__ import print_function
from sys import stdin, stdout
from string import *

words = [w.decode("utf-8") for w in stdin.read().strip().split()]

if (len(words) != 0):
    print(int(round((sum(len(w) for w in words) + 0.0) / len(words))))
else:
    print(0)