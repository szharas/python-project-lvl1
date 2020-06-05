import prompt


ROUNDS_COUNT = 3


def welcome_user():
    print('\nWelcome to the Brain Games!')


def play_game(game):
    welcome_user()
    print(game.DESCRIPTION)
    print()
    user_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(user_name))

    count = 0  # number of correct answers to finish the game

    while count < ROUNDS_COUNT:
        question, correct_answer = game.generate_question_and_answer()

        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, correct_answer))
            print("Let's try again, {}!".format(user_name))

    print("Congratulations, {}!".format(user_name))
