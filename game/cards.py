#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Module for trader cards"""

import abc

from game import spice


class InvalidCardAction(Exception):
    """
    Raised when a
    """

    def __init__(self, *args, **kwargs):
        super(InvalidCardAction, self).__init__(*args, **kwargs)


class ActionCard:
    __metaclass__ = abc.ABCMeta

    # boolean: True if this card class can be used multiple times in one turn
    repeatable = False

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        """

        Returns: visual representation of card (ASCII art-style)
        NB: all TradeCards have <= 5 cubes of input and output, all ScoreCards have <= 6 cubes of cost, so I'm
            arbitrarily defining card size as 9 characters wide and 7 characters tall
        """
        pass


class TradeCard(ActionCard):
    # Might move this logic to Player.
    repeatable = True

    def __init__(self, input_spices, output_spices):
        """
        Type of card which trades one set of spices for another.
        Can be used multiple times in the same turn.
        Args:
            input_spices: SpiceSet, spices which are consumed by this card
            output_spices: SpiceSet, spices which are produced by this card
        """
        super(TradeCard, self).__init__()
        self.input = input_spices
        self.output = output_spices

    # def __str__(self):
    #     """
    #
    #     Returns:
    #
    #     """
    #     return dedent("""\
    #         ╔═══════╗
    #         ║       ║
    #         ║       ║
    #         ║   ↦   ║
    #         ║       ║
    #         ║       ║
    #         ╚═══════╝
    #     """)

    def trade(self, spices):
        """
        Trade spices for other spices

        Args:
            spices: SpiceSet, input set of spices

        Returns:
            SpiceSet, set of spices after using this action

        Raises:
            InvalidCardAction: When this action cannot be performed on the spices
                (e.g. not enough spices to trade)

        """
        return_spices = spices - self.input + self.output

        if any(map(lambda x: x < 0, return_spices)):
            raise InvalidCardAction("Not enough spices to use this TradeCard (%s) -> (%s)")

        return return_spices


class UpgradeCard(ActionCard):
    UPGRADE_LOOKUP = {
        spice.SpiceSet(1, 0, 0, 0): spice.SpiceSet(0, 1, 0, 0),
        spice.SpiceSet(0, 1, 0, 0): spice.SpiceSet(0, 0, 1, 0),
        spice.SpiceSet(0, 0, 1, 0): spice.SpiceSet(0, 0, 0, 1),
    }

    def __init__(self, num):
        """
        Type of card which upgrades multiple spices into higher-tier spices.
        Args:
            num: int, Number of spices which are upgraded by one use of this card. Should be 2 or 3.
        """
        super(UpgradeCard, self).__init__()
        self.num = num

    def upgrade(self, spices, upgrades):
        """
        Upgrade spices into better spices

        Args:
            spices: SpiceSet, input set of spices
            upgrades: list(SpiceSet), iterable of self.num elements where each element is a SpiceSet with one element.
                Should be ordered from cheapest to most expensive spice.

        Returns:
            SpiceSet, set of spices after using this action

        Raises:
            InvalidCardAction: When this action cannot be performed on the spices
                (e.g. not enough spices to upgrade)

        """

        if len(upgrades) > self.num:
            raise InvalidCardAction("Number of upgrades must be <= %s", self.num)

        for upgrade in upgrades:
            # Validate upgrade
            try:
                spices += self.UPGRADE_LOOKUP[upgrade] - upgrade
            except KeyError:
                raise InvalidCardAction("Invalid upgrade input: %s", str(upgrades))

        return spices


class AcquireCard(ActionCard):
    def __init__(self, acquire_spices):
        """
        Type of card which acquires (gains) a fixed set of spices for no cost.
        Args:
            acquire_spices: SpiceSet, spices which are acquired by using this card.
        """
        super(AcquireCard, self).__init__()
        self.acquire_spices = acquire_spices

    def acquire(self, spices):
        """Use this card to gain spices"""
        return spices + self.acquire_spices


class ScoreCard:
    def __init__(self, spice_cost, points):
        """

        Args:
            spice_cost: SpiceSet, amount of spice the must be paid to claim this card
            points:
        """
        self._spice_cost = spice_cost
        self._points = points

    @property
    def cost(self):
        return self._spice_cost

    @property
    def points(self):
        return self._points


