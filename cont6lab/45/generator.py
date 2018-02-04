from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr
import sys

HEX_DIGITS = '0123456789ABCDEF'


def rnd(l, r, base=10):
    return base_repr(randint(l, r), base=base)


def rnd_word(length, prefix=' ', alphabet=HEX_DIGITS):
    word = ''.join(choice(alphabet) for _ in range(length))
    return (choice(prefix) + word).lstrip(' ') or '0'


def generate_test1(params):
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    if not params['leading_zero']:
        a = a.lstrip('0')
    return '{0} '.format(a)


def generate_test2(params):
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    b = rnd_word(randint(*params['word_len'][1]),
                 alphabet=HEX_DIGITS[:params['word_radix'][1]],
                 prefix=params['word_prefix'][0])
    if not params['leading_zero']:
        a, b = a.lstrip('0'), b.lstrip('0')
    return '{1} {0}'.format(a, b)


def generate_test2_par(params):
    while True:
        _a = randint(*(params['word_len'][0]))
        _b = randint(*(params['word_len'][1]))
        if _a > _b:
            break
    a = _a
    b = _b
    return '{1} {0}'.format(a, b)



def rnd_tests(test_first=66, nums=2, tests=40, base=10):
    params = {
        'word_len': [(2, 8), (2, 11)],
        'word_radix': [base, base],
        'word_prefix': [' ', ' '], # can be '     +-', for example
        'leading_zero': True
    }

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            if nums == 3:
                a = generate_test1(params)
                b = 0
                c = 0
                pr = randint(0, 1)
                if (pr == 1):
                    b = str(long(a) * randint(1, 100)) + " "
                    if (a == 0):
                        c = "0"
                    else:
                        c = long(b) * (long(b) // long(a))
                        c = str(c).rstrip()
                else:
                    b = generate_test1(params)
                    c = generate_test1(params)
                    c = str(c).rstrip()
                f.write(a + str(b) + str(c))
            elif nums == 2:
                f.write(generate_test2(params))

NUMS = 3
BASE = 10

if __name__ == '__main__':
    test_idx = 2 # SPECIFY!!!
    rnd_tests(test_first=test_idx, nums=NUMS, tests=100, base=BASE)
