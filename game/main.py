#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import curses
from collections import Iterable
from random import shuffle

from game import cards


class Game:
    WINDOW_HEIGHT = 51
    WINDOW_WIDTH = 251

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

        self.trader_deck = cards.TRADER_DECK
        shuffle(self.trader_deck)
        self.trader_market = [self.trader_deck.pop() for _ in range(6)]

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

        # Initialize curses
        stdscr = curses.initscr()
        stdscr.keypad(1)
        self.win = curses.newwin(self.WINDOW_HEIGHT, self.WINDOW_WIDTH, 0, 0)

        # curses.noecho()
        curses.cbreak()
        curses.start_color()

        # Clear screen
        self.win.clear()

        # Initialize colors corresponding to spice colors
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)

    def __del__(self):
        self.win.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()

    def initialize_players(self):
        pass

    def loop(self):
        """
        Main loop
        """
        self.render('')
        while True:
            i = self.get_input()
            self.render(i)

    def get_input(self):
        self.win.move(self.WINDOW_HEIGHT - 1, 0)
        ret = self.win.getstr()
        self.win.deleteln()
        return ret

    def render(self, i):
        self.win.clear()
        self.win.addstr(0, 0, "\u25a3", curses.color_pair(1))
        self.win.addstr(0, 1, "\u25a3", curses.color_pair(2))
        self.win.addstr(0, 2, "\u25a3", curses.color_pair(3))
        self.win.addstr(0, 3, "\u25a3", curses.color_pair(4))
        self.win.addstr(1, 0, i)
        self.win.refresh()


if __name__ == "__main__":
    game = Game(0)
    game.loop()
