from __future__ import print_function
from random import shuffle, randint, choice, random
import string


def random_word(word_length):
    return ''.join(choice(2 * string.ascii_lowercase + string.letters) for i in range(word_length))


with open('wordlist.txt', 'r') as f:
    words = [w.strip() for w in f.readlines()]


def dictionary_word():
    word = choice(words)
    if random() > 0.5:
        word = word.capitalize()
    return word


def random_delimiters(delimiters_qty):
    return ''.join(choice(' \n \r \t  ') for i in range(delimiters_qty))


def random_text(params):
    text = ''

    if random() >= 0.5:
        text += random_delimiters(randint(*params['delimiters_qty']))

    for _ in xrange(randint(*params['words_qty'])):
        text += random_word(randint(*params['word_length']))
        #text += dictionary_word()
        text += random_delimiters(randint(*params['delimiters_qty']))

    if random() >= 0.5:
        text = text.rstrip()

    return text


if __name__ == '__main__':
    params = {
        'words_qty': (1, 15),
        'word_length': (1, 500),
        'delimiters_qty': (1, 2)
    }

    test_first = 1
    tests = 60

    for test_idx in range(test_first, test_first + tests):
        with open('tests/{0:03d}.dat'.format(test_idx), 'w') as f:
            f.write(dictionary_word())