import unittest

from game import spice
from copy import deepcopy


class TestSpiceSet(unittest.TestCase):

    def test_spiceset_normal(self):
        ss = spice.SpiceSet(1, 2, 3, 4)
        assert ss.turmeric == 1
        assert ss.saffron == 2
        assert ss.cardamom == 3
        assert ss.cinnamon == 4

    def test_spiceset_to_curses(self):
        assert spice.SpiceSet(0, 0, 0, 1).to_curses() == [4]
        assert spice.SpiceSet(0, 0, 1, 0).to_curses() == [3]
        assert spice.SpiceSet(0, 1, 0, 0).to_curses() == [2]
        assert spice.SpiceSet(1, 0, 0, 0).to_curses() == [1]
        assert spice.SpiceSet(1, 0, 1, 1).to_curses() == [4, 3, 1]

    def test_spiceset_sum(self):
        ss = spice.SpiceSet(1, 2, 3, 4)
        assert sum(ss) == 10

    def test_empty_spiceset_raises(self):
        with self.assertRaises(TypeError):
            spice.SpiceSet()

    def test_spiceset_equality(self):
        """Check that SpiceSet objects are compared by value, not by reference"""
        a = spice.SpiceSet(1, 3, 1, 2)
        b = spice.SpiceSet(1, 3, 1, 2)
        assert a is not b
        assert a == b

    def test_spiceset_equality_deepcopy(self):
        """Check that SpiceSet objects are compared by value, not by reference, using copy.deepcopy"""
        a = spice.SpiceSet(1, 3, 1, 2)
        b = deepcopy(a)
        assert a is not b
        assert a == b
