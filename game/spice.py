#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import namedtuple
from itertools import chain, repeat

SPICE_CHARACTER = chr(0x25A3)


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

    def to_curses(self):
        """Return a string of curses pairs representing this SpiceSet ("""
        return list(reversed(list(chain.from_iterable(repeat(clr, qty) for clr, qty in enumerate(self, start=1)))))


class PlayerInventory(SpiceSet):
    def __str__(self):
        pass

    def __add__(self, other):
        # todo: add check for what happens if self + other > 10? Or do this no the input validation side?
        return super(SpiceSet, self).__add__(other)

    def render(self, win, x, y):
        win.addstr("╔═══════════╗", x, y)
        win.addstr("║ X X X X X ║", x, y + 1)
        win.addstr("║ X X X X X ║", x, y + 2)
        win.addstr("╚═══════════╝", x, y + 3)
        # todo: be careful, this only renders 10 spices

        xs = chain([2, 4, 6, 8, 10])
        ys = chain.from_iterable(repeat(x, 5) for x in [1, 2])
        for color, x, y in zip(self.to_curses(), xs, ys):
            win.add_str(SPICE_CHARACTER, x, y, color)
