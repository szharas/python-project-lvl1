#!/usr/bin/env python
from brain_games.games import calc
from brain_games.game_engine import play_game


def main():
    play_game(calc)


if __name__ == '__main__':
    main()
