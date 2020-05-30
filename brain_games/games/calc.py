from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    operand_1 = randint(1, 100)
    operand_2 = randint(1, 100)
    operator = choice('-+*')

    if operator == '+':
        result = add(operand_1, operand_2)
    elif operator == '-':
        result = sub(operand_1, operand_2)
    elif operator == '*':
        result = mul(operand_1, operand_2)

    question = '{} {} {}'.format(operand_1, operator, operand_2)
    correct_answer = str(result)

    return question, correct_answer
