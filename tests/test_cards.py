import game.deck
from game import cards


def test_deck():
    """Test that cards.ACTION_DECK actually instantiates"""
    assert len(game.deck.TRADER_DECK) == 43

# def test_strs():
#     sddrt
