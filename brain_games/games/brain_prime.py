from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    # Iterate from 2 to n / 2
    for i in range(2, num // 2):
        if (num % i) == 0:
            return False
            break
        else:
            True


def generate_question():
    num = randint(1, 1000)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'

    return question, correct_answer
