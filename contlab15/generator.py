from __future__ import print_function
from random import shuffle, randint

tests = 30
max_size = 15
size = [1, max_size]
lim = [-5, +5]

print('{0} {1}'.format(tests, max_size))

def print_as_matrix(data, size):
    for idx, item in enumerate(data):
        print('{0} '.format(item), end='')
        if (idx + 1) % size == 0:
            print('', end='\n')

for i in range(1, tests / 2 + 1):
    print('{0}'.format(i))
    data = [randint(lim[0], lim[1]) for _ in range(0, i * i)]
    shuffle(data)
    print_as_matrix(data, i)

for i in range(tests / 2, 0, -1):
    print('{0}'.format(i))
    data = [randint(lim[0], lim[1]) for _ in range(0, i * i)]
    shuffle(data)
    print_as_matrix(data, i)
