from random import randint


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGHT = 10


def generate_question_and_answer():
    progression = []
    start_num = randint(1, 10)
    step = randint(1, 10)
    last_num = PROGRESSION_LENGHT * step + start_num

    for i in range(start_num, last_num, step):
        progression.append(i)

    random_choice = randint(0, PROGRESSION_LENGHT - 1)  # get index from 0 to 9
    correct_answer = str(progression[random_choice])
    progression[random_choice] = '..'
    question = ' '.join(str(e) for e in progression)

    return question, correct_answer
