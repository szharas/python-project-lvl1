from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    question = ''
    correct_answer = ''
    operators = ['add', 'substract', 'multiply']

    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operator = choice(operators)

    if operator == 'add':
        question = '{} + {}'.format(operand_1, operand_2)
        correct_answer = str(operand_1 + operand_2)
    elif operator == 'substract':
        question = '{} - {}'.format(operand_1, operand_2)
        correct_answer = str(operand_1 - operand_2)
    elif operator == 'multiply':
        question = '{} * {}'.format(operand_1, operand_2)
        correct_answer = str(operand_1 * operand_2)

    return question, correct_answer


def main():
    generate_question()


if __name__ == '__main__':
    main()
