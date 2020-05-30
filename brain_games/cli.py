import prompt


def welcome_user(description=None):
    print('Welcome to the Brain Games!')
    if description:
        print(description)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
