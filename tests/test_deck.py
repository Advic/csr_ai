import copy
import unittest

from game import deck
from game import spice


class TestActionArea(unittest.TestCase):
    def setUp(self):
        self.actionarea = deck.ActionArea()

    def test_faceup_area_size(self):
        assert len(self.actionarea.faceup) == 6

    def test_claiming_first_card(self):
        """Test that claiming cards with no cards will claim the first card"""
        faceup_org = copy.copy(self.actionarea.faceup)
        assert self.actionarea.claim([]) == faceup_org[0]
        assert self.actionarea.faceup[0:-1] == faceup_org[1:deck.ActionArea.FACEUP_ACTION_SIZE]
        assert len(self.actionarea.faceup) == deck.ActionArea.FACEUP_ACTION_SIZE

    def test_claiming_cards(self):
        """Test that claiming cards by paying spice works"""
        faceup_org = copy.copy(self.actionarea.faceup)
        assert self.actionarea.claim([spice.SpiceSet(1, 0, 0, 0)]) == faceup_org[1]
        assert self.actionarea.faceup[0:-1] == faceup_org[0:1] + faceup_org[2:deck.ActionArea.FACEUP_ACTION_SIZE]
        assert len(self.actionarea.faceup) == deck.ActionArea.FACEUP_ACTION_SIZE

    def test_claiming_deck_empty_deck(self):
        """Test that claiming cards when the deck is empty doesn't raise anything.
        A normal game should never really get to this point if players are skilled"""
        faceup_org = copy.copy(self.actionarea.faceup)
        self.actionarea._deck = []

        assert self.actionarea.claim([]) == faceup_org[0]
        assert len(self.actionarea.faceup) == deck.ActionArea.FACEUP_ACTION_SIZE - 1
        assert self.actionarea.faceup == faceup_org[1:]
