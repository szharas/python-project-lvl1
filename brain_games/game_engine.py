import prompt
from brain_games.cli import welcome_user


NUMBER_OF_CORRECT_ANSWERS = 3  # number of correct answers to finish the game


def play_game(game):
    user_name = welcome_user(game.DESCRIPTION)
    count = 0

    while count < NUMBER_OF_CORRECT_ANSWERS:
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
