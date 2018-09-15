from game import spice
from game.card import ScoreCard, AcquireCard, TradeCard, UpgradeCard


class TraderDeck:
    def __init__(self):
        shuffle(self.trader_deck)
        self.trader_market = [self.trader_deck.pop() for _ in range(6)]


SCORE_DECK = [
    ScoreCard(spice.SpiceSet(2, 2, 0, 0), 6),
    ScoreCard(spice.SpiceSet(3, 2, 0, 0), 7),
    ScoreCard(spice.SpiceSet(0, 4, 0, 0), 8),
    ScoreCard(spice.SpiceSet(2, 0, 2, 0), 8),
    ScoreCard(spice.SpiceSet(2, 3, 0, 0), 8),
    ScoreCard(spice.SpiceSet(3, 0, 2, 0), 9),
    ScoreCard(spice.SpiceSet(0, 2, 2, 0), 10),
    ScoreCard(spice.SpiceSet(0, 5, 0, 0), 10),
    ScoreCard(spice.SpiceSet(2, 0, 0, 2), 10),
    ScoreCard(spice.SpiceSet(2, 0, 3, 0), 11),
    ScoreCard(spice.SpiceSet(3, 0, 0, 2), 11),
    ScoreCard(spice.SpiceSet(0, 0, 4, 0), 12),
    ScoreCard(spice.SpiceSet(0, 2, 0, 2), 12),
    ScoreCard(spice.SpiceSet(0, 3, 2, 0), 12),
    ScoreCard(spice.SpiceSet(0, 2, 3, 0), 13),
    ScoreCard(spice.SpiceSet(0, 0, 2, 2), 14),
    ScoreCard(spice.SpiceSet(0, 3, 0, 2), 14),
    ScoreCard(spice.SpiceSet(2, 0, 0, 3), 14),
    ScoreCard(spice.SpiceSet(0, 0, 5, 0), 15),
    ScoreCard(spice.SpiceSet(0, 0, 0, 4), 16),
    ScoreCard(spice.SpiceSet(0, 2, 0, 3), 16),
    ScoreCard(spice.SpiceSet(0, 0, 3, 2), 17),
    ScoreCard(spice.SpiceSet(0, 0, 2, 3), 18),
    ScoreCard(spice.SpiceSet(0, 0, 0, 5), 20),
    ScoreCard(spice.SpiceSet(2, 1, 0, 1), 9),
    ScoreCard(spice.SpiceSet(0, 2, 1, 1), 12),
    ScoreCard(spice.SpiceSet(1, 0, 2, 1), 12),
    ScoreCard(spice.SpiceSet(2, 2, 2, 0), 13),
    ScoreCard(spice.SpiceSet(2, 2, 0, 2), 15),
    ScoreCard(spice.SpiceSet(2, 0, 2, 2), 17),
    ScoreCard(spice.SpiceSet(0, 2, 2, 2), 19),
    ScoreCard(spice.SpiceSet(1, 1, 1, 1), 12),
    ScoreCard(spice.SpiceSet(3, 1, 1, 1), 14),
    ScoreCard(spice.SpiceSet(1, 3, 1, 1), 16),
    ScoreCard(spice.SpiceSet(1, 1, 3, 1), 18),
    ScoreCard(spice.SpiceSet(1, 1, 1, 3), 20),
]
TRADER_DECK = [
    # Acquire Cards
    AcquireCard(spice.SpiceSet(0, 0, 0, 1)),
    AcquireCard(spice.SpiceSet(0, 0, 1, 0)),
    AcquireCard(spice.SpiceSet(0, 2, 0, 0)),
    AcquireCard(spice.SpiceSet(2, 1, 0, 0)),
    AcquireCard(spice.SpiceSet(1, 0, 1, 0)),
    AcquireCard(spice.SpiceSet(1, 1, 0, 0)),
    AcquireCard(spice.SpiceSet(3, 0, 0, 0)),
    AcquireCard(spice.SpiceSet(4, 0, 0, 0)),

    # Trade Cards
    TradeCard(spice.SpiceSet(0, 0, 0, 1), spice.SpiceSet(0, 0, 2, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 1), spice.SpiceSet(1, 1, 1, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 1), spice.SpiceSet(3, 0, 1, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 1), spice.SpiceSet(0, 3, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 1), spice.SpiceSet(2, 2, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 2), spice.SpiceSet(1, 1, 3, 0)),
    TradeCard(spice.SpiceSet(0, 0, 0, 2), spice.SpiceSet(0, 3, 2, 0)),
    TradeCard(spice.SpiceSet(0, 0, 1, 0), spice.SpiceSet(0, 2, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 1, 0), spice.SpiceSet(1, 2, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 1, 0), spice.SpiceSet(4, 1, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 2, 0), spice.SpiceSet(0, 0, 0, 2)),
    TradeCard(spice.SpiceSet(0, 0, 2, 0), spice.SpiceSet(0, 2, 0, 1)),
    TradeCard(spice.SpiceSet(0, 0, 2, 0), spice.SpiceSet(2, 1, 0, 1)),
    TradeCard(spice.SpiceSet(0, 0, 2, 0), spice.SpiceSet(2, 3, 0, 0)),
    TradeCard(spice.SpiceSet(0, 0, 3, 0), spice.SpiceSet(0, 0, 0, 3)),
    TradeCard(spice.SpiceSet(2, 0, 1, 0), spice.SpiceSet(0, 0, 0, 2)),
    TradeCard(spice.SpiceSet(0, 1, 0, 0), spice.SpiceSet(3, 0, 0, 0)),
    TradeCard(spice.SpiceSet(0, 2, 0, 0), spice.SpiceSet(2, 0, 0, 1)),
    TradeCard(spice.SpiceSet(0, 2, 0, 0), spice.SpiceSet(0, 0, 2, 0)),
    TradeCard(spice.SpiceSet(0, 2, 0, 0), spice.SpiceSet(3, 0, 1, 0)),
    TradeCard(spice.SpiceSet(0, 3, 0, 0), spice.SpiceSet(0, 0, 0, 2)),
    TradeCard(spice.SpiceSet(0, 3, 0, 0), spice.SpiceSet(1, 0, 1, 1)),
    TradeCard(spice.SpiceSet(0, 3, 0, 0), spice.SpiceSet(0, 0, 3, 0)),
    TradeCard(spice.SpiceSet(0, 3, 0, 0), spice.SpiceSet(2, 0, 2, 0)),
    TradeCard(spice.SpiceSet(1, 1, 0, 0), spice.SpiceSet(0, 0, 0, 1)),
    TradeCard(spice.SpiceSet(2, 0, 0, 0), spice.SpiceSet(0, 0, 1, 0)),
    TradeCard(spice.SpiceSet(2, 0, 0, 0), spice.SpiceSet(0, 2, 0, 0)),
    TradeCard(spice.SpiceSet(3, 0, 0, 0), spice.SpiceSet(0, 0, 0, 1)),
    TradeCard(spice.SpiceSet(3, 0, 0, 0), spice.SpiceSet(0, 1, 1, 0)),
    TradeCard(spice.SpiceSet(3, 0, 0, 0), spice.SpiceSet(0, 3, 0, 0)),
    TradeCard(spice.SpiceSet(4, 0, 0, 0), spice.SpiceSet(0, 0, 1, 1)),
    TradeCard(spice.SpiceSet(4, 0, 0, 0), spice.SpiceSet(0, 0, 2, 0)),
    TradeCard(spice.SpiceSet(5, 0, 0, 0), spice.SpiceSet(0, 0, 0, 2)),
    TradeCard(spice.SpiceSet(5, 0, 0, 0), spice.SpiceSet(0, 0, 3, 0)),

    # Upgrade Card
    UpgradeCard(3),
]
