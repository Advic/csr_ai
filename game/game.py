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
