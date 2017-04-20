from Game.Bricks.Brick import Brick
from Game.Shared import GameConstants

class LifeBrick(Brick):

    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()
        game.increaseLives()

        # i want the parent class to handle what happens when the brick gets hit
        super(LifeBrick, self).hit()


    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK_LIFE