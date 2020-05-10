#!/usr/bin/env python
from random import randint
from math import gcd


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question():
    question = ''
    correct_answer = ''

    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = '{} {}'.format(num_1, num_2)
    correct_answer = str(gcd(num_1, num_2))

    return question, correct_answer


def main():
    generate_question()


if __name__ == '__main__':
    main()
