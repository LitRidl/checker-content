from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr


HEX_DIGITS = '0123456789ABCDEF'


def rnd(l, r, base=10):
    return base_repr(randint(l, r), base=base)


def rnd_word(length, prefix='', alphabet=HEX_DIGITS):
    word = ''.join(choice(HEX_DIGITS[:base]) for _ in range(length))
    return (choice(prefix) + word).lstrip(' ')


def generate_test(params):
    return


if __name__ == '__main__':
    params = {
        'word_len': [(1, 50), (1, 50)],
        'word_radix': [10, 10],
        'word_prefix': ['', ''] # can be '     +-', for example
    }

    test_first = 2
    tests = 20

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(generate_test(params))