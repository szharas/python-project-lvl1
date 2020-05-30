#!/usr/bin/env python
from brain_games.games import gcd
from brain_games.games.game_engine import play_game


def main():
    play_game(gcd)


if __name__ == '__main__':
    main()
