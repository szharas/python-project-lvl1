from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    num = randint(1, 1000)
    question = str(num)
    correct_answer = ''

    # Iterate from 2 to n / 2
    for i in range(2, num // 2):
        if (num % i) == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return question, correct_answer


def main():
    generate_question()


if __name__ == '__main__':
    main()
