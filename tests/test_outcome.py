from unittest import TestCase

from roulette.outcome import Outcome


class TestOutcome(TestCase):

    def setUp(self):
        self.sampleOutcomeOne = Outcome("1", 1)
        self.sampleOutcomeTwo = Outcome("Red", 17)
        self.sampleOutcomeThree = Outcome("Red", 17)

    def test_sameNameReturnsTrue(self):
        self.assertEqual(True, self.sampleOutcomeTwo.__eq__(self.sampleOutcomeThree))
        self.assertEqual(True, self.sampleOutcomeThree.__eq__(self.sampleOutcomeTwo))

    def test_sameNameReturnsSameHash(self):
        self.assertEqual(True, self.sampleOutcomeTwo.__hash__() == self.sampleOutcomeThree.__hash__())
        self.assertEqual(True, self.sampleOutcomeThree.__hash__() == self.sampleOutcomeTwo.__hash__())

    def test_winAmount(self):
        self.assertEqual(170, self.sampleOutcomeTwo.winAmount(10))
        self.assertEqual(34, self.sampleOutcomeThree.winAmount(2))
