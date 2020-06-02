from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            return False
        # Iterate from 2 to n / 2
        for i in range(2, num // 2):
            if (num % i) == 0:
                return False
                break
            else:
                True


def generate_question_and_answer():
    number = randint(1, 1000)

    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer
