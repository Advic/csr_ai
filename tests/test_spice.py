from game import spice


def test_spiceset():
    ss = spice.SpiceSet(1, 2, 3, 4)
    assert ss.turmeric == 1
    assert ss.saffron == 2
    assert ss.cardamom == 3
    assert ss.cinnamon == 4


def test_spiceset_sum():
    ss = spice.SpiceSet(1, 2, 3, 4)
    assert sum(ss) == 10
