import os
import fileinput
import pygame
import random

from Game.Shared.GameConstants import GameConstants
from Game.Bricks import *

class Level(object):

    def __init__(self, game):
        self.__game = game
        self.__bricks = []
        self.__amountOfBricksLeft = 0
        self.__currentLevel = 0

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricks(self):
        return self.__amountOfBricksLeft

    def brickHit(self):
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self):
        self.__currentLevel += 1
        fileName = os.path.join("Game", "Assets", "Levels", "level" + str(self.__currentLevel) + ".dat")

        # if the level does not exist in the Levels folder create a random one
        if not os.path.exists(fileName):
            self.loadRandom()
        # else load the one that exists
        else:
            self.load(fileName)


    # NOTE: The game will load a random level only at first, then the method reset()
    #       will load the level 0
    def loadRandom(self):
        self.__bricks = []

        # coordinates for the bricks
        x, y = 0, 0

        maxBricks = int(GameConstants.SCREEN_SIZE[0] / GameConstants.BRICK_SIZE[0])
        rows = random.randint(2, 8)

        amountOfSuperPowerBricks = 0

        for row in range(0, rows):
            for brick in range(0, maxBricks):

                brickType = random.randint(0, 3)
                # the game screen can only hold 8 bricks
                if brickType == 1 or amountOfSuperPowerBricks >= 6:
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif brickType == 2:
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                elif brickType == 3:
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1
                    amountOfSuperPowerBricks += 1

                # increase the position of x in order to populate the screen with bricks
                x += GameConstants.BRICK_SIZE[0]

            # reset the position used for the next line
            # and increase the y by the brick's height value
            x = 0
            y += GameConstants.BRICK_SIZE[1]

    def load(self, level):
        self.__currentLevel = level
        self.__bricks = []

        # coordinates for the bricks
        x, y = 0, 0

        for line in fileinput.input(os.path.join("Game", "Assets", "Levels", "level" + str(level) + ".dat")):
            for currentBrick in line:
                # the game screen can only hold 8 bricks
                if currentBrick == "1":
                    brick = Brick([x, y], pygame.image.load(GameConstants.SPRITE_BRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2":
                    brick = SpeedBrick([x, y], pygame.image.load(GameConstants.SPRITE_SPEEDBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3":
                    brick = LifeBrick([x, y], pygame.image.load(GameConstants.SPRITE_LIFEBRICK), self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                # increase the position of x in order to populate the screen with bricks
                x += GameConstants.BRICK_SIZE[0]

            # reset the position used for the next line
            # and increase the y by the brick's height value
            x = 0
            y += GameConstants.BRICK_SIZE[1]