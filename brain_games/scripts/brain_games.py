#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.scripts.game_engine import play_game
import brain_games.games.brain_even
import brain_games.games.brain_calc


def greet():
    print('Welcome to the Brain Games!')


def brain_calc():
    main(brain_games.games.brain_calc)


def brain_even():
    main(brain_games.games.brain_even)


def main(game=None):
    greet()

    if game:
        print(game.DESCRIPTION + '\n')

    user_name = welcome_user()

    if game:
        print()
        play_game(game, user_name)


if __name__ == '__main__':
    main()
