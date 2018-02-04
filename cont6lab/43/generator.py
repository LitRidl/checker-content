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
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    return '{0} '.format(a)


def generate_test2(params):
    a = rnd_word(randint(*params['word_len'][0]),
                 alphabet=HEX_DIGITS[:params['word_radix'][0]],
                 prefix=params['word_prefix'][0])
    b = rnd_word(randint(*params['word_len'][1]),
                 alphabet=HEX_DIGITS[:params['word_radix'][1]],
                 prefix=params['word_prefix'][0])
    return '{0} {1} '.format(a, b)



def int_to_roman(number):
   if not 0 < number < 4000:
      raise ValueError, "Argument must be between 1 and 3999"
   ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   result = ""
   for i in range(len(ints)):
      count = int(number / ints[i])
      result += nums[i] * count
      number -= ints[i] * count
   return result


def seq_tests1(var1_bounds, var2_bounds):
    test_idx = 2
    for a in range(*var1_bounds):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(int_to_roman(a))
            test_idx += 1


def seq_tests2(var1_bounds, var2_bounds):
    test_idx = 2
    for shift in range(*var1_bounds):
        for number in range(*var2_bounds):
            with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
                res = '{0} {1}'.format(base_repr(shift, 10), base_repr(number, 10))
                f.write(res)
                test_idx += 1

def rnd_tests():
    params = {
        'word_len': [(2, 20), (4, 20)],
        'word_radix': [10, 10],
        'word_prefix': [' ', ' '] # can be '     +-', for example
    }

    test_first = 65
    tests = 30

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(int_to_roman(randint(64, 3999)))


if __name__ == '__main__':
    #seq_tests1([1, 64], [0, 10])
    rnd_tests()
