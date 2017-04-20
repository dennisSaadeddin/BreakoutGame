import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants

class Breakout(object):
    """

    All the sub-folders inside the Game module act as module for the Game module.

    """

    def __init__(self):
        # pass will let the class(in this case constructor) exist without being used
        # pass
        self.__lives = 5
        self.__score = 0

        # create a new instance of the level class
        self.__level = Level(self)
        # load the level
        self.__level.loadRandom()

        # the first tuple is position of the pad
        # second argument is the sprite
        self.__pad = Pad((GameConstants.SCREEN_SIZE[0] / 2, \
                          GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]), \
                          pygame.image.load(GameConstants.SPRITE_PAD))
        self.__balls = [
            Ball((400, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
        ]

        # here we start initializing pygames
        pygame.init()
        pygame.mixer.init()
        # this is the title of the game's page
        pygame.display.set_caption("The Breakout - 2017")

        self.__clock = pygame.time.Clock()

        # the set_mode parameters are the screen size, whether the screen can be full screen or not
        # (i.e. double buffer) and the depth of color - 32 bit
        # also you can add a pipe( | ) between  pygame.DOUBLEBUF and pygame.FULLSCREEN
        # to allow the user to set full screen
        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        pygame.mouse.set_visible(0)

        # the difference between () and [] is that with () we create a tuple => we can't add any new values
        # but with [] we create a collection => we can add new values
        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        # this means that the current scene is the first one
        self.__currentScene = 3

        self.__sounds = (
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAME_OVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_LIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_BRICK_SPEED),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_WALL),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_HIT_PAD)
        )

    # the game loop will be inside this function
    def start(self):
        while 1:
            # clock ticks is FPS
            self.__clock.tick(100)

            self.screen.fill((0, 0, 0))

            # retrieve the current scene and retrieve and handle the events of the current scene
            # when retrieving an element from a tuple, we call it within []
            currentScene = self.__scenes[self.__currentScene]
            # get() will get the event that occurred and pass it down to the handleEvents function
            currentScene.handleEvents(pygame.event.get())
            # and now render the scene
            currentScene.render()

            # update the display with the modifications
            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def increaseLives(self):
        self.__lives += 1

    def reduceLives(self):
        self.__lives -= 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)

if __name__ == "__main__":
    Breakout().start()