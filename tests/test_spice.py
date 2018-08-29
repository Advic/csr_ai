from game import spice


def test_spiceset():
    ss = spice.SpiceSet(1, 2, 3, 4)
    assert ss.turmeric == 1
    assert ss.saffron == 2
    assert ss.cardamom == 3
    assert ss.cinnamon == 4


def test_spiceset_str():
    assert str(spice.SpiceSet(0, 0, 0, 1)) == "\x1b[38;5;130m\u25A0\x1b[0m"  # Cinnamon: brown square
    assert str(spice.SpiceSet(0, 0, 1, 0)) == "\x1b[38;5;112m\u25A0\x1b[0m"  # Cardamom: green square
    assert str(spice.SpiceSet(0, 1, 0, 0)) == "\x1b[38;5;1m\u25A0\x1b[0m"  # Saffron: red square
    assert str(spice.SpiceSet(1, 0, 0, 0)) == "\x1b[38;5;226m\u25A0\x1b[0m"  # Turmeric: yellow square
    y_g_b = "\x1b[38;5;130m\u25A0\x1b[0m \x1b[38;5;112m\u25A0\x1b[0m \x1b[38;5;226m\u25A0\x1b[0m"
    assert str(spice.SpiceSet(1, 0, 1, 1)) == y_g_b


def test_spiceset_sum():
    ss = spice.SpiceSet(1, 2, 3, 4)
    assert sum(ss) == 10
