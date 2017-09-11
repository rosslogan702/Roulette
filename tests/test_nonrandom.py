from unittest import TestCase
from roulette.nonrandom import NonRandom
from roulette.wheel import createWheel
from roulette.bin import Bin

class TestNonRandom(TestCase):

    def setUp(self):
        self.values = (5, 12, 14, 25, 32)
        self.rng = NonRandom(self.values)
        self.wheel = createWheel(self.rng)

    def test_spinningWheel(self):
        nextBin = self.wheel.next()
        self.assertIsInstance(nextBin, Bin)

    def test_NonRandomBinsSelected(self):
        print(self.wheel.next())
        print(self.wheel.next())
        print(self.wheel.next())
        print(self.wheel.next())
        print(self.wheel.next())


