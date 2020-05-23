import prompt


def play_game(game, user_name):
    NO_OF_TRIES = 3
    count = 0

    while count < NO_OF_TRIES:
        question, correct_answer = game.generate_question()

        print('Question: {}'.format(question))
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            count += 1
        elif answer == 'exit':
            break
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                answer, correct_answer))
            print("Let's try again, {}!".format(user_name))

    print("Congratulations, {}!".format(user_name))

