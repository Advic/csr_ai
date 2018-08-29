from collections import namedtuple
from enum import Enum
from itertools import chain, repeat

from colored import fg, attr


class Spice(Enum):
    # todo: find a usage for this or remove
    TURMERIC = 1  # Yellow
    SAFFRON = 2  # Red
    CARDAMOM = 3  # Green
    CINNAMON = 4  # Brown


class SpiceSet(namedtuple('SpiceBase', ('turmeric', 'saffron', 'cardamom', 'cinnamon'))):
    # Colors for the 4 spices, in the same order as the namedtuple definition.
    # turmeric: yellow_1, saffron: red, cardamom: chartreuse_2b, cinnamon: dark_orange_3a
    _colors = [fg('yellow_1'), fg('red'), fg('chartreuse_2b'), fg('dark_orange_3a')]

    def __init__(self, *args, **kwargs):
        super(SpiceSet, self).__init__(**kwargs)

    def __add__(self, other):
        """Adds two SpiceSets"""
        return SpiceSet(self.turmeric + other.turmeric,
                        self.saffron + other.saffron,
                        self.cardamom + other.cardamom,
                        self.cinnamon + other.cinnamon)

    def __sub__(self, other):
        """Subtract two SpiceSets"""
        return SpiceSet(self.turmeric - other.turmeric,
                        self.saffron - other.saffron,
                        self.cardamom - other.cardamom,
                        self.cinnamon - other.cinnamon)

    @property
    def size(self):
        return self.turmeric + self.saffron + self.cardamom + self.cinnamon

    def __str__(self):
        """

        Returns: unicode string with ANSI color code, colored as the actual board game version is made

        """

        def colored_square(color):
            return color + chr(0x25A3) + attr('reset')

        return ''.join(reversed(
            list(chain.from_iterable(repeat(colored_square(clr), qty) for qty, clr in zip(self, self._colors)))))
