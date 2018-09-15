import unittest

from game import spice


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
