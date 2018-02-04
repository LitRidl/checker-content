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
    l1 = randint(*params['word_len'][0])
    l2 = l1 # randint(*params['word_len'][1])

    a = rnd_word(l1, alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    b = rnd_word(l2, alphabet=HEX_DIGITS[:params['word_radix'][1]],
                 prefix=params['word_prefix'][0])
    if not params['leading_zero']:
        a, b = a.lstrip('0'), b.lstrip('0')
    return '{0} {1} '.format(a, b)


def generate_test2_par(params):
    while True:
        _a = randint(*(params['word_len'][0]))
        _b = randint(*(params['word_len'][1]))
        if _a > _b:
            break
    a = _a
    b = _b
    return '{0} {1} '.format(a, b)


def seq_tests1(var1_bounds, var2_bounds, base=10):
    test_idx = 2
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            res = '{0}'.format(base_repr(a, base))
            f.write(res)
            test_idx += 1
    return test_idx


def seq_tests2(var1_bounds, var2_bounds, base=10):
    test_idx = 2
    for a in range(*var1_bounds):
        for b in range(*var2_bounds):
            with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                res = '{0} {1}'.format(base_repr(a, base), base_repr(b, base))
                f.write(res)
                test_idx += 1
    return test_idx

def rnd_tests(test_first=66, nums=2, tests=40, base=10):
    params = {
        'word_len': [(2, 12), (2, 12)],
        'word_radix': [base, base],
        'word_prefix': [' ', ' '], # can be '     +-', for example
        'leading_zero': True
    }

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            if nums == 1:
                f.write(generate_test1(params))
            elif nums == 2:
                f.write(generate_test2(params))

NUMS = 2
BASE = 2
TESTS = 100 # 40

if __name__ == '__main__':
    test_idx = 66 # SPECIFY!!!
    if 's' in sys.argv[1]:
        if NUMS == 1:
            test_idx = seq_tests1([0, 40], [0, 0], base=BASE)
        if NUMS == 2:
            test_idx = seq_tests2([0, 8], [0, 8], base=BASE)
        print('Seq tests until {0}'.format(test_idx))
    if 'r' in sys.argv[1]:
        rnd_tests(test_first=test_idx, nums=NUMS, tests=TESTS, base=BASE)
