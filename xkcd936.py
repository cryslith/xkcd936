#!/usr/bin/python3


import argparse
import random
import math
import sys


def entropy(words, n):
    return n * math.log(len(words), 2)


def make_password(words, n):
    rand = random.SystemRandom()
    return ' '.join(rand.choice(words) for _ in range(n))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('words', nargs='?', default='/usr/share/dict/words')
    argparser.add_argument('n')
    args = argparser.parse_args()

    with open(args.words) as f:
        words = [w.strip() for w in f]
    n = int(args.n)

    print('theoretical maximum entropy: {} bits'.format(entropy(words, n)),
          file=sys.stderr)
    print('continue? [y/N] ', end='', file=sys.stderr)
    if input() in ('y', 'Y', 'yes', 'Yes'):
        print(make_password(words, n))

if __name__ == '__main__':
    main()
