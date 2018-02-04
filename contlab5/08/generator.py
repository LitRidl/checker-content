from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr


HEX_DIGITS = '0123456789ABCDEF'


def rnd(l, r, base=10):
    return base_repr(randint(l, r), base=base)


def rnd_word(length, prefix=' ', alphabet=HEX_DIGITS):
    word = ''.join(choice(alphabet) for _ in range(length))
    return (choice(prefix) + word).lstrip(' ').lstrip('0') or '0'


def generate_test1(params):
    a = rnd_word(randint(*params['word_len'][0]), alphabet=HEX_DIGITS[:params['word_radix'][0]])
    return '{0} '.format(a)


def generate_test2(params):
    a = rnd_word(randint(*params['word_len'][0]), alphabet=HEX_DIGITS[:params['word_radix'][0]])
    b = rnd_word(randint(*params['word_len'][1]), alphabet=HEX_DIGITS[:params['word_radix'][1]])
    return '{0} {1} '.format(a, b)


def seq_tests1(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            res = '{0}'.format(base_repr(a, 2))
            f.write(res)
            test_idx += 1


def seq_tests2(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        for b in range(*var2_bounds):
            with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                res = '{0} {1}'.format(base_repr(a, 2), base_repr(b, 2))
                f.write(res)
                test_idx += 1

def rnd_tests():
    params = {
        'word_len': [(6, 50), (1, 20)],
        'word_radix': [2, 2],
        'word_prefix': ['', ''] # can be '     +-', for example
    }

    test_first = 52
    tests = 20

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(generate_test1(params))


if __name__ == '__main__':
    # seq_tests1([0, 50], [0, 10])
    rnd_tests()
