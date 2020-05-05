#!/usr/bin/env python
import prompt
from random import randint


def start_game():
    count = 0
    while count < 3:
        random_num = randint(1, 100)
        is_even = random_num % 2 == 0
        correct_answer = 'yes' if is_even else 'no'

        print('Question: {}'.format(random_num))
        user_input = prompt.string('Your answer: ')

        if is_even and user_input == correct_answer:
            print('Correct!')
            count += 1
        elif not is_even and user_input == correct_answer:
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_input, correct_answer))


def main():
    start_game()


if __name__ == '__main__':
    main()
