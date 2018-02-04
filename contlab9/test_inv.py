from __future__ import print_function
from random import shuffle, randint, choice
from os import path, listdir


def reader(task_idx):
    files = [f for f in listdir(
        '{0:02d}/tests/'.format(task_idx)) if f.endswith('.dat')]
    files.sort()
    for fname in files:
        with open('{0:02d}/tests/{1}'.format(task_idx, fname), 'r') as f:
            test_data = f.read().split()
            print('test({0}, {1}, {2})'.format(*test_data))


if __name__ == '__main__':
    reader(6)
