from unittest import TestCase
from roulette.outcome import Outcome
from roulette.bin import Bin

class TestBin(TestCase):
    def setUp(self):
        self.outcomeOne = Outcome("0", 35)
        self.outcomeTwo = Outcome("00", 35)
        self.outcomeThree = Outcome("00-0-1-2-3", 6)

    def test_binConstruction(self):
        bin = Bin(self.outcomeOne, self.outcomeTwo, self.outcomeThree)
        print(bin.__str__())
        self.assertIsNotNone(bin)

