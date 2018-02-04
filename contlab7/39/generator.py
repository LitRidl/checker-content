from __future__ import print_function
from random import shuffle, randint, choice
from numpy import base_repr
import sys
from string import lowercase

LATIN = lowercase
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
    return '{0}'.format(a)


def generate_test2(params, fmt, filter_good, same_len):
    while True:
        l1 = randint(*params['word_len'][0])
        l2 = randint(*params['word_len'][1]) if not same_len else l1

        a = rnd_word(l1, alphabet=HEX_DIGITS[:params['word_radix'][0]],
                     prefix=params['word_prefix'][0])
        b = rnd_word(l2, alphabet=HEX_DIGITS[:params['word_radix'][1]],
                     prefix=params['word_prefix'][0])
        if filter_good(long(a, base=params['word_radix'][0]),
                       long(b, base=params['word_radix'][1])):
            break
    if not params['leading_zero']:
        a, b = a.lstrip('0'), b.lstrip('0')
    return fmt.format(a, b)


def seq_tests1(var1_bounds, var2_bounds, base, start):
    test_idx = start
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            res = '{0}'.format(base_repr(a, base))
            f.write(res)
            test_idx += 1
    return test_idx


def seq_tests2(var1_bounds, var2_bounds, base, start, fmt, filter_good, same_len):
    test_idx = start
    for a in range(*var1_bounds):
        for b in range(*var2_bounds):
            if filter_good(a, b):
                with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                    _a, _b = base_repr(a, base), base_repr(b, base)
                    max_len = max(len(_a), len(_b))
                    if same_len:
                        _a, _b = _a.zfill(max_len), _b.zfill(max_len)
                    res = fmt.format(_a, _b)
                    f.write(res)
                    test_idx += 1
    return test_idx


def rnd_tests(test_first, nums, tests, base, word_len, word_prefix,
             leading_zero, fmt_pair, same_len, filter_good):
    params = {
        'word_len': word_len,
        'word_radix': [base, base],
        'word_prefix': word_prefix,  # can be '     +-', for example
        'leading_zero': leading_zero
    }

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            if nums == 1:
                f.write(generate_test1(params))
            elif nums == 2:
                f.write(generate_test2(params, fmt=fmt_pair,
                        same_len=same_len, filter_good=filter_good))


def special_task(test_idx):
    words_qty = range(0, 15) # Sequential
    words_qty.extend([randint(16, 30) for _ in range(150)]) # 50 rnd tests

    for qty in words_qty:
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            nums = [rnd_word(length=randint(1, 6), prefix=' ', alphabet=HEX_DIGITS[:10])
                             for _ in range(qty)]
            f.write('#'.join(num for num in nums))
        test_idx += 1

    with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
        f.write('#'.join('0' for _ in range(39)))
        test_idx += 1

    with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
        f.write('#'.join('0' for _ in range(71)))
        test_idx += 1


TEST_STARTING=2

NUMS_PER_TEST=1
NUMS_RADIX=10

SEQ1_RANGE=[[0, 150 + 1], None]
SEQ2_RANGE=[[0, 25 + 1], [0, 25 + 1]]

FILTER2_GOOD=lambda a, b: True
FMT_PAIR='{0} {1}'
SAME_LEN=False

RND_TESTS=400
RND_WORD_LEN=[(3, 30)] * 2  # word len in chars
RND_LEADING_ZERO=True
RND_WORD_PREFIX=[' '] * 2


if __name__ == '__main__':
    test_idx=TEST_STARTING

    if len(sys.argv) <= 1:
        print('Usage: {0} sr', sys.argv[0])
        sys.exit(0)

    if '!' in sys.argv[1]:
        print('Special task discovered.')
        special_task(test_idx=test_idx)
        sys.exit(0)

    if 's' in sys.argv[1]:
        if NUMS_PER_TEST == 1:
            test_idx=seq_tests1(
                *SEQ1_RANGE, base=NUMS_RADIX, start=TEST_STARTING)
        elif NUMS_PER_TEST == 2:
            test_idx=seq_tests2(
                *SEQ2_RANGE, base=NUMS_RADIX, start=TEST_STARTING,
                fmt=FMT_PAIR, same_len=SAME_LEN, filter_good=FILTER2_GOOD)
        print('Seq tests from {0} to {1} ({2} total seq)'.format(TEST_STARTING,
                                                             test_idx, test_idx - TEST_STARTING))
    if 'r' in sys.argv[1]:
        print('Rnd tests from {0} to {1} ({2} total rnd)'.format(
            test_idx, test_idx + RND_TESTS, RND_TESTS))
        rnd_tests(test_first=test_idx, nums=NUMS_PER_TEST, tests=RND_TESTS,
                  base=NUMS_RADIX, word_len=RND_WORD_LEN, word_prefix=RND_WORD_PREFIX,
                  leading_zero=RND_LEADING_ZERO, fmt_pair=FMT_PAIR, same_len=SAME_LEN,
                  filter_good=FILTER2_GOOD)
