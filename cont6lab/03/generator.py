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
    return '{0} {1} '.format(a, b)


def seq_tests1(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            res = '{0}'.format(base_repr(a, 9))
            f.write(res)
            test_idx += 1


def seq_tests2(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        for b in range(*var2_bounds):
            if a <= b:
                continue
            with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                res = '{0} {1}'.format(base_repr(a, 9), base_repr(b, 9))
                f.write(res)
                test_idx += 1

def rnd_tests():
    params = {
        'word_len': [(2, 7), (2, 11)],
        'word_radix': [9, 9],
        'word_prefix': [' ', ' '] # can be '     +-', for example
    }

    test_first = 57
    tests = 40

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(generate_test2(params))


if __name__ == '__main__':
    if sys.argv[1] == 's' or len(sys.argv):
        seq_tests2([0, 11], [0, 11])
    if sys.argv[1] == 'r':
        rnd_tests()
