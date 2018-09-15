import os

from game import deck


class Game:
    def __init__(self, game_id, nplayers, shuffle_players=True):
        """
        WIP

        Args:
            game_id: unique integer of game name
            nplayers: number of playyers
            shuffle_players:
        """

        # if isinstance(nplayers, Iterable):
        #     pass
        # elif isinstance(nplayers, int):
        #     pass

        self.trader_deck = deck.ActionArea()
        self.score_deck = deck.ScoreArea(nplayers)

    def loop(self):
        """
        Main loop
        """
        self.render()
        while True:
            i = self.get_input()
            self.render()

    def render(self):
        os.system('clear')
        print(self.score_deck)
        print(self.trader_deck)

    def get_input(self):
        return input('Enter your command: ')
