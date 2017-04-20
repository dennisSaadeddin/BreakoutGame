from Game.Shared.GameConstants import GameConstants
from Game.Shared.GameObject import GameObject


class Brick(GameObject):

    def __init__(self, position, sprite, game):
        self.__game = game
        # I want to set up the position and sprite in the GameObject(parent or base class)
        # super is the way to interact with our base class
        # first parameter is the type of class we want to retrieve(Brick in this case)
        # the 2nd param means on our own instance
        # another way: GameObject.__init__(self, position, (), game)
        # python 3.x: super().__init__(bla bla)
        # use () if you haven't yet defined the parameter(aka placeholder)
        self.__hitPoints = 100
        self.__lives = 1
        super(Brick, self).__init__(position, GameConstants.BRICK_SIZE, sprite)

    # create the getters
    def getGame(self):
        return self.__game

    def isDestroyed(self):
        # this returns a boolean value if lives <= 0
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK