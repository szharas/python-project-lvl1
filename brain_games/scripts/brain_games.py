#!/usr/bin/env python
from brain_games.cli import welcome_user
# from brain_games.scripts.check_even import start_game
from brain_games.scripts.game_engine import play_game
from brain_games.games.brain_even import brain_even_game
from brain_games.games.brain_calc import brain_calc_game


def greet():
    print('Welcome to the Brain Games!')


def brain_calc():
    DESCRIPTION, question_generator = brain_calc_game()
    main(DESCRIPTION, question_generator)


def brain_even():
    DESCRIPTION, question_generator = brain_even_game()
    main(DESCRIPTION, question_generator)


def main(DESCRIPTION=None, game=None):
    greet()
    if DESCRIPTION:
        print(DESCRIPTION + '\n')
    user_name = welcome_user()

    if game:
        play_game(game, user_name)


if __name__ == '__main__':
    main()
