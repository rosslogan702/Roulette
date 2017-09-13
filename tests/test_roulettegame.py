from unittest import TestCase
from roulette.roulettegame import RouletteGame
from roulette.table import Table
from roulette.nonrandom import NonRandom
from roulette.passenger57 import PassengerFiftySeven
from roulette.wheel import createWheel

class TestRouletteGame(TestCase):

    def setUp(self):
        self.rng = NonRandom()
        self.rng.setSeed(3)
        self.wheel = createWheel(self.rng)
        self.table = Table()
        self.player = PassengerFiftySeven(self.table)
        self.game = RouletteGame(self.wheel, self.table)

    def testSingleGameCycle(self):
        self.game.cycle(self.player)

        self.assertEqual(True, self.player.playerWon)

    def testThreeGameCycle(self):
        betsWon = []
        for spin in range(0, 3):
            self.game.cycle(self.player)
            betsWon.append(self.player.playerWon)

        self.assertEqual(True, betsWon[0])
        self.assertEqual(False, betsWon[1])
        self.assertEqual(False, betsWon[2])




