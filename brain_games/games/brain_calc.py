from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    question = ''
    correct_answer = ''

    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operator = choice('-+*')

    question = '{} {} {}'.format(operand_1, operator, operand_2)

    if operator == '+':
        correct_answer = str(operand_1 + operand_2)
    elif operator == '-':
        correct_answer = str(operand_1 - operand_2)
    elif operator == '*':
        correct_answer = str(operand_1 * operand_2)

    return question, correct_answer

