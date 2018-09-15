"""For the gold coins you get from scoring the left score cards"""

from collections import namedtuple

Coin = namedtuple("Coin", "points")

gold = Coin(3)
silver = Coin(1)
