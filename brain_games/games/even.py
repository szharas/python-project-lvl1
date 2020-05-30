from random import randint


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def generate_question_and_answer():
    number = randint(1, 100)
    is_even = number % 2 == 0

    question = str(number)
    correct_answer = 'yes' if is_even else 'no'

    return question, correct_answer
