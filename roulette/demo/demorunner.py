"""
Description: Class to perform a demonstration of the roulette game class
Author: Ross Logan 2017
"""
from roulette.wheel import Wheel
from roulette.nonrandom import NonRandom
from roulette.passenger57 import PassengerFiftySeven
from roulette.table import Table
from roulette.roulettegame import RouletteGame

class DemoRunner(object):

    def __init__(self):
        self.wheel = Wheel(NonRandom())
        self.table = Table()
        self.player = PassengerFiftySeven(self.table)
        self.game = RouletteGame(self.wheel, self.table)

    def runGame(self):
        for cycle in range(0,3):
            self.game.cycle(self.player)

