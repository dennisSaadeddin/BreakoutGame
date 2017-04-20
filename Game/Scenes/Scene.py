import pygame

class Scene(object):
    """
    The scene is responsible for handling all the events and rendering the scene to screen.

    """
    def __init__(self, game):
        self.__game = game
        self.__texts = [] # we can append text to our collection of texts here

    # is called from withing the game loop
    # renders everything to the screen
    def render(self):
        for text in self.__texts:
            # for each text we want to interact with our game and use the screen
            # inside our game to blit the text onto screen
            self.__game.screen.blit(text[0], text[1])

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, string, x = 0, y = 0, color = [255, 255, 255], background = [0, 0, 0], size = 17):
        font = pygame.font.Font(None, size)
        self.__texts.append([font.render(string, True, color, background), (x, y)])