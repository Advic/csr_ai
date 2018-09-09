#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses
from collections import Iterable
from random import shuffle

from game import cards


class Game:
    def __init__(self, id, players=None, shuffle_players=True):
        """
        WIP

        Args:
            id: unique integer of game name
            players:
            shuffle_players:
        """

        if isinstance(players, Iterable):
            pass
        elif isinstance(players, int):
            pass

        self.action_deck = cards.ACTION_DECK
        shuffle(self.action_deck)
        self.action_market = [self.action_deck.pop() for _ in range(6)]

        # todo: gold and silver coins for 0th and 1st element of scoring_area
        self.score_deck = cards.SCORE_DECK
        shuffle(self.score_deck)
        self.scoring_area = [self.score_deck.pop() for _ in range(5)]

        # Instantiate players
        # Give players their starting hands (Acquire(YY), Convert(2))
        # Assign one to go first
        # Distribute starting resources
        # Instantiate action_deck and action_market
        # Instantiate scoring_area and coin piles

    def initialize_players(self):
        pass


def main(stdscr):
    # Clear screen
    stdscr.clear()
    win = curses.newwin(51, 215, 0, 0)

    # Initialize colors corresponding to spice colors
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

    assert curses.has_colors()
    win.addstr(0, 0, "\u25a3", curses.color_pair(1))
    win.addstr(0, 1, "\u25a3", curses.color_pair(2))
    win.addstr(0, 2, "\u25a3", curses.color_pair(3))
    win.addstr(0, 3, "\u25a3", curses.color_pair(4))

    win.refresh()
    win.getkey()


def render_game():
    pass


def get_action():
    pass


if __name__ == "__main__":
    curses.wrapper(main)
