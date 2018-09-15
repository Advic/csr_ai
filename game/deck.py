import abc
from random import shuffle

from . import exceptions
from . import spice
from .card import ScoreCard, AcquireCard, TradeCard, UpgradeCard


class Deck(metaclass=abc.ABCMeta):
    def __init__(self):
        # List of face-down cards
        self._deck = None

    @abc.abstractclassmethod
    def claim(self, n):
        """Claim face-up card number N (0-indexed)"""
        pass


class FaceUpActionCard:
    """Composition of an ActionCard and a SpiceSet"""

    def __init__(self, card, spiceset=spice.SpiceSet(0, 0, 0, 0)):
        self.card = card
        self.spiceset = spiceset


class ActionArea(Deck):
    """Central area for purchasable action cards"""
    FACEUP_ACTION_SIZE = 6

    def __init__(self):
        super().__init__()
        self._deck = [
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
        shuffle(self._deck)
        self._faceup = [FaceUpActionCard(self._deck.pop()) for _ in range(self.FACEUP_ACTION_SIZE)]

    @property
    def faceup(self):
        """Returns the faceup cards"""
        return self._faceup

    def claim(self, payment):
        """
        Claim a card from the faceup play area by paying spice.
        Which card is determined by the amount of spice paid.

        Args:
            payment: list(SpiceSet), list of SpiceSets to pay for the card
                Each SpiceSet must have a size of 1
                Spice is put onto cards in the order of payment (0th payment on card 0, 1st payment on card 1, etc.)


        Returns:

        """
        if len(payment) > len(self.faceup) - 1:
            raise exceptions.InvalidPlayerAction("Received overpayment of length %d", payment)
        if not all([len(spiceset) == 1 for spiceset in payment]):
            raise exceptions.InvalidPlayerAction("Payment SpiceSets must all have a value of 1")

        # Add payments to faceup cards
        for faceup, spiceset in zip(self._faceup, payment):
            faceup.spiceset += payment

        ret = self._faceup[len(payment)]
        del self._faceup[len(payment)]
        self._faceup.append(FaceUpActionCard(self._deck.pop()))
        return ret


class ScoreArea(Deck):
    def __init__(self):
        super().__init__()
        self._deck = [
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
        shuffle(self._deck)
        self.scoring_area = [self._deck.pop() for _ in range(5)]
