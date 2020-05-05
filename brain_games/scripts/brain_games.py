#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.scripts.check_even import start_game


def greet():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greet()
    start_game()


if __name__ == '__main__':
    main()
