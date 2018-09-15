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
        aa_faceup_original = copy.copy(self.actionarea.faceup)
        assert self.actionarea.claim([]) == aa_faceup_original[0]
        aa_faceup_new = self.actionarea.faceup
        assert aa_faceup_new[0:-1] == aa_faceup_original[1:6]
        assert len(aa_faceup_new) == 6

    def test_claiming_cards(self):
        """Test that claiming cards works"""
        aa_faceup_original = copy.copy(self.actionarea.faceup)
        assert self.actionarea.claim([spice.SpiceSet(1, 0, 0, 0)]) == aa_faceup_original[1]
        aa_faceup_new = self.actionarea.faceup
        assert aa_faceup_new[0:-1] == aa_faceup_original[0:1] + aa_faceup_original[2:6]
        assert len(aa_faceup_new) == 6
