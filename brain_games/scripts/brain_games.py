#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.scripts.game_engine import play_game
from brain_games.games import brain_even, brain_calc, brain_gcd, brain_progression, brain_prime


def greet():
    print('Welcome to the Brain Games!')


def start_brain_prime():
    main(brain_prime)


def start_brain_progression():
    main(brain_progression)


def start_brain_gcd():
    main(brain_gcd)


def start_brain_calc():
    main(brain_calc)


def start_brain_even():
    main(brain_even)


def main(game=None):
    greet()

    if game:
        print(game.DESCRIPTION)

    print()

    user_name = welcome_user()

    if game:
        print()
        play_game(game, user_name)


if __name__ == '__main__':
    main()
