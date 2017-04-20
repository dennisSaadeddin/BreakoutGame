import pygame

from Game.Shared import *

class Ball(GameObject):

    """
    The ball class has:
     - a reference to the game
     - the ball has a certain speed
     - a variable that holds the value the speed will be incremented by; the variable is multiplied by the speed
     - direction for x and y in which the ball moves
     - have a variable that tells us if the ball is moving

    """

    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = 5 # a constant speed
        self.__increment = [2, 2]
        self.__direction = [1, 1]
        self.__inMotion = 0

        super(Ball, self).__init__(position, GameConstants.BALL_SIZE, sprite)

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    def resetSpeed(self):
        self.setSpeed(5)

    def getSpeed(self):
        return self.__speed

    def isInMotion(self):
        return self.__inMotion

    def setMotion(self, isMoving):
        self.__inMotion = isMoving
        self.resetSpeed()

    # this will change the direction of the ball in case a brick was hit
    # we want to know what side of the brick was hit
    def changeDirection(self, gameObject):
        # get the position and size of the ball
        position = self.getPosition()
        size = self.getSize()

        #  do the same for the other object
        objectPosition = gameObject.getPosition()
        objectSize = gameObject.getSize()

        if position[1] > objectPosition[1] and \
                        position[1] < objectPosition[1] + objectSize[1] and \
                        position[0] > objectPosition[0] and \
                        position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] + objectSize[1]))
            self.__direction[1] *= -1

        elif position[1] + size[1] > objectPosition[1] and \
                                position[1] + size[1] < objectPosition[1] + objectSize[1] and \
                        position[0] > objectPosition[0] and \
                        position[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((position[0], objectPosition[1] - objectSize[1]))
            self.__direction[1] *= -1

        elif position[0] + size[0] > objectPosition[0] and \
                                position[0] + size[0] < objectPosition[0] + objectSize[0]:
            self.setPosition((objectPosition[0] - size[0], position[1]))
            self.__direction[0] *= -1

        else:
            self.setPosition((objectPosition[0] + objectSize[0], position[1]))
            self.__direction[0] *= -1
            self.__direction[1] *= -1

    def updatePosition(self):

        if not self.isInMotion():
            padPosition = self.__game.getPad().getPosition()
            self.setPosition((
                padPosition[0] + (GameConstants.PAD_SIZE[0] / 2),
                GameConstants.SCREEN_SIZE[1] - \
                GameConstants.PAD_SIZE[1] - \
                GameConstants.BALL_SIZE[1]
            ))

            return

        position = self.getPosition()
        size = self.getSize()

        newPosition = [position[0] + (self.__increment[0] * self.__speed) * self.__direction[0],
                       position[1] + (self.__increment[1] * self.__speed) * self.__direction[1]]

        # checks to see if we are outside of our application to the right hand side
        if newPosition[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:
            self.__direction[0] *= -1
            newPosition = [GameConstants.SCREEN_SIZE[0] - size[0], newPosition[1]]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)

        # check to see if we are outside of our application to the left hand side
        if newPosition[0] <= 0:
            self.__direction[0] *= -1
            newPosition = [0, newPosition[1]]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)

        # check to see if we are outside of our application to the bottom
        if newPosition[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], GameConstants.SCREEN_SIZE[1] - size[1]]

        # check to see if we are outside of our application to the top
        if newPosition[1] <= 0:
            self.__direction[1] *= -1
            newPosition = [newPosition[0], 0]
            self.__game.playSound(GameConstants.SOUND_HIT_WALL)


        self.setPosition(newPosition)


    # this will see whether the ball has touched the bottom of the screen
    def isBallDead(self):
        position = self.getPosition()
        size = self.getSize()

        if position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            # ball is dead
            return 1

        # ball is  not dead
        return 0