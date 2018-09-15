import copy
import unittest

from game import deck


class TestActionArea(unittest.TestCase):
    def test_claiming_cards(self):
        """Test that claiming cards works"""
        aa = deck.ActionArea()
        assert len(aa.faceup) == 6
        aa_faceup_original = copy.copy(aa.faceup)
        assert aa.claim(2) == aa_faceup_original[2]
        aa_faceup_new = aa.faceup
        assert aa_faceup_new[0:-1] == aa_faceup_original[0:2] + aa_faceup_original[3:6]
