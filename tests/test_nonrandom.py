from unittest import TestCase
from roulette.nonrandom import NonRandom
from roulette.wheel import Wheel
from roulette.bin import Bin

class TestNonRandom(TestCase):

    def setUp(self):
        self.rng = NonRandom()
        self.wheel = Wheel(self.rng)
        self.seed = 1

    def test_spinningWheel(self):
        nextBin = self.wheel.next()
        self.assertIsInstance(nextBin, Bin)

