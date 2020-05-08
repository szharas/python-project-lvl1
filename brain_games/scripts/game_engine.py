#!/usr/bin/env python
import prompt


def play_game(question_generator, user_name):
    count = 0

    while count < 3:
        question, correct_answer = question_generator()

        print('Question: {}'.format(question))
        user_input = prompt.string('Your answer: ')

        if user_input == correct_answer:
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_input, correct_answer))
            print("Let's try again, {}!".format(user_name))

    print("Congratulations, {}!".format(user_name))


def main():
    play_game()


if __name__ == '__main__':
    main()
