from __future__ import print_function
from random import shuffle, randint, choice, random
from string import *

def test(text, end='\n'):
    with open('tests/{0:03d}.dat'.format(test.idx), 'w') as f:
        global comm
        if (comm == 1):
            a = " }"
        elif (comm == 3):
            a = " *)"
        else:
            a = ""
        f.write(text.lstrip().decode('string_escape')+ a + end)
    test.idx += 1



def suf(w, prob=0.0):
    # s = choice('cCC') if random() < prob else ''
    # return w + s
    a = random()
    if a < prob and comm == 0:
        global comm
        if (random() < 0.5):
            s = choice(["{", " {", "{ "])
            comm = 1
        else:
            s = choice(["(*", " (*", "(* "])
            comm = 3
    elif (a < prob and comm == 1):
        s = choice(["}", " }", "} "])
        global comm
        comm = 0
    elif (a < prob and comm == 3):
        s = choice(["*)", " *)", "*) "])
        global comm
        comm = 0
    else:
        s = ''
    return w + s if random() < 0.5 else s + w


def word(alphabet=ascii_letters + digits, rng=[1, 10],
         sign_prob=0.0, num_prob=0.0, word_prob=0.0):
    sign = choice('+-') if random() < sign_prob else ''
    if random() < word_prob:
        sign, alphabet = '', ascii_letters
        if random() <= 0.2:
            alphabet = ascii_lowercase
        elif random() <= 0.2:
            alphabet = ascii_uppercase
        rng = [1, 30]
    elif random() < num_prob:
        alphabet = hexdigits[:randint(2, 16)]
        if random() <= 0.3:
            alphabet = digits
        rng = [1, 9]
    return sign + suf(''.join(choice(alphabet) for _ in range(randint(*rng))), 0.01)


if __name__ == '__main__':
    comm = 0
    test.idx = 2
    test('')
    test('+')
    test('-')
    test('-+')
    test('+-')

    # Random whitespace files
    for _ in range(5):
        test(word('  \t\n\r', [1, 10]), end='')

    # One random letter, signed/unsigned
    for x in (ascii_letters + digits):
        test(x, end=choice(['', '', '\n']))
        test('-' + x, end=choice(['', '', '\n']))
        test('+' + x, end=choice(['', '', '\n']))

    # One random word, then random number
    for _ in range(30):
        test(word(sign_prob=0.2), end=choice(['', '', '\n']))
        test(word(hexdigits, sign_prob=0.5), end=choice(['', '', '\n']))

    # Random numeric tests
    for _ in range(50):
        text = ''
        for line in range(randint(1, 20)):
            words = [word(sign_prob=0.4, num_prob=1.0) for _ in range(0, 100)]
            text += ' '.join(words) + '\n'
        test(text.rstrip(), end=choice(['', '', '\n']))

    # Big digit/letter set in one line
    text1 = ' '.join(choice(hexdigits) for _ in range(3000))
    text2 = ' '.join(choice(ascii_letters) for _ in range(3000))
    test(text1 + '\n' + text2, end=choice(['', '', '\n']))

    # Random al word tests
    for _ in range(50):
        text = ''
        for line in range(randint(1, 20)):
            words = [word(sign_prob=0.4, word_prob=1.0) for _ in range(0, 100)]
            text += ' '.join(words) + '\n'
        test(text.rstrip(), end=choice(['', '', '\n']))

    # Random alnum tests
    for _ in range(300):
        text = ''
        for line in range(randint(1, 100)):
            words = [word(sign_prob=0.4, num_prob=0.4, word_prob=0.3) for _ in range(0, 200)]
            text += ' '.join(words) + '\n'
        test(text.rstrip(), end=choice(['', '', '\n']))
