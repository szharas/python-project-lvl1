#!/usr/bin/env python
from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_question():
    question = randint(1, 100)
    is_even = question % 2 == 0
    correct_answer = 'yes' if is_even else 'no'

    return question, correct_answer


def main():
    generate_question()


if __name__ == '__main__':
    main()
