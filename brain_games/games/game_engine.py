import prompt


def play_game(game, user_name):
    count = 0

    while count < 3:
        question, correct_answer = game.generate_question()

        print('Question: {}'.format(question))
        user_input = prompt.string('Your answer: ')

        if user_input == correct_answer:
            print('Correct!')
            count += 1
        elif user_input == 'exit':
            break
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                user_input, correct_answer))
            print("Let's try again, {}!".format(user_name))

    print("Congratulations, {}!".format(user_name))

