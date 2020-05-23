from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    # find the greatest common divisor
    while b:
        a, b = b, a % b
    return a


def generate_question():
    question = ''
    correct_answer = ''

    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = '{} {}'.format(num_1, num_2)
    correct_answer = str(gcd(num_1, num_2))

    return question, correct_answer
