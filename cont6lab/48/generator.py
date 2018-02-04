from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr
import sys

HEX_DIGITS = '0123456789ABCDEF'


def rnd(l, r, base=10):
    return base_repr(randint(l, r), base=base)


def rnd_word(length, prefix=' ', alphabet=HEX_DIGITS):
    word = ''.join(choice(alphabet) for _ in range(length))
    return (choice(prefix) + word).lstrip(' ') or '0' # .lstrip('0')


def generate_test1(params):
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    return '{0}'.format(a)


def generate_test2(params):
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    b = rnd_word(randint(*params['word_len'][1]),
                 alphabet=HEX_DIGITS[:params['word_radix'][1]],
                 prefix=params['word_prefix'][0])
    return '{0} {1}'.format(a, b)


def generate_test2_par(params):
    while True:
        _a = randint(*(params['word_len'][0]))
        _b = randint(*(params['word_len'][1]))
        if _a > _b:
            break
    a = _a
    b = _b
    return '{0} {1}'.format(a, b)



def rnd_tests(test_first=66, nums=2, tests=40):
    params = {
        'word_len': [(2, 5), (2, 11)],
        'word_radix': [2, 2],
        'word_prefix': [' ', ' '] # can be '     +-', for example
    }

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            if nums == 1:
                f.write(generate_test1(params))
            elif nums == 2:
                f.write(generate_test2(params))


if __name__ == '__main__':
    rnd_tests(test_first=2, nums=1, tests=100)