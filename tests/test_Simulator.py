from unittest import TestCase
from roulette.simulator import Simulator
from roulette.roulettegame import RouletteGame
from roulette.passenger57 import PassengerFiftySeven
from roulette.nonrandom import NonRandom
from roulette.wheel import Wheel
from roulette.table import Table

class TestSimulator(TestCase):

    def setUp(self):
        self.rng = NonRandom()
        self.wheel = Wheel(self.rng)
        self.table = Table()
        self.game = RouletteGame(self.wheel, self.table)
        self.player = PassengerFiftySeven(self.table)
        self.simulator = Simulator(self.game, self.player)

    def testSession(self):
        stakeValues = self.simulator.session()

        self.assertEqual(self.player.stake, 98)
        self.assertEqual(self.player.roundsToGo, 1)
        self.assertEqual(stakeValues[0], self.player.stake)

