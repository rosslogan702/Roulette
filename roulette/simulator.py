"""
Description:    Simulator class that runs a number of cycles of the roulette game
Author:         Ross Logan 2017
"""

class Simulator(object):

    def __init__(self, game, player):
        self.initDuration = 250
        self.initStake = 100
        self.samples = 50
        self.durations = []
        self.maxima = []
        self.player = player
        self.game = game

    def session(self):
        pass




