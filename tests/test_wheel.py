from unittest import TestCase
from roulette.outcome import Outcome
from roulette.bin import Bin
from roulette.wheel import createWheel
from roulette.nonrandom import NonRandom

class TestWheel(TestCase):

    def setUp(self):
        self.sampleOutcomeOne = Outcome("1", 1)
        self.sampleOutcomeTwo = Outcome("Red", 17)
        self.outcomeOne = Outcome("0", 35)
        self.outcomeTwo = Outcome("00-0-1-2-3", 6)
        self.binOne = Bin(self.sampleOutcomeOne, self.sampleOutcomeTwo)
        self.binTwo = Bin(self.outcomeOne, self.outcomeTwo)
        self.rng = NonRandom()
        self.wheel = createWheel(self.rng)

    def test_binsCanBeAddedToWheel(self):
        binOne = self.wheel.get(0)
        binTwo = self.wheel.get(37)

        self.assertIsInstance(binOne, Bin)
        self.assertIsInstance(binTwo, Bin)

    def testOutcomesAddedToMap(self):
        self.assertEqual(self.outcomeOne, self.wheel.getOutcome("0"))
        self.assertEqual(Outcome("00", 35), self.wheel.getOutcome("00"))





