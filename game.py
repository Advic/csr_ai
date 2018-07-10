from collections import Iterable
from random import shuffle

import cards


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

        self.trader_deck = cards.ACTION_DECK
        shuffle(self.trader_deck)
        self.market = [self.trader_deck.pop() for _ in range(6)]

        # Instantiate players
        # Give players their starting hands (Acquire(YY), Convert(2))
        # Assign one to go first
        # Distribute starting resources
        # Instantiate trader_deck and action market
        # Instantiate scoring area and coin piles

    def initialize_players(self):
        pass
