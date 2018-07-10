from collections import namedtuple
from enum import Enum


class Spice(Enum):
    # todo: find a usage for this or remove
    TURMERIC = 1  # Yellow
    SAFFRON = 2  # Red
    CARDAMOM = 3  # Green
    CINNAMON = 4  # Brown


class SpiceSet(namedtuple('SpiceBase', ('turmeric', 'saffron', 'cardamom', 'cinnamon'))):
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
