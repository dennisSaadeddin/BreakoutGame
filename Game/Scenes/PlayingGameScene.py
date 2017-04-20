import pygame

from Game.Scenes.Scene import Scene
from Game.Shared import GameConstants

class PlayingGameScene(Scene):
    
    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self):

        super(PlayingGameScene, self).render()

        game = self.getGame()
        # this is the array with all the balls
        balls = game.getBalls()
        level = game.getLevel()

        if level.getAmountOfBricks() <= 0:
            for ball in balls:
                ball.setMotion(0)
            # load the next level -> check class Level()
            level.loadNextLevel()

        if game.getLives() <= 0:
            game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAMEOVER_SCENE)


        # gets the pad to be used inside the for loop
        pad = game.getPad()
        for ball in game.getBalls():

            # this will check if multiple balls intersect and will change the
            # direction if they do
            for ball2 in balls:
                if ball != ball2 and ball.intersects(ball2):
                    ball.changeDirection(ball2)

            for brick in game.getLevel().getBricks():
                if not brick.isDestroyed() and ball.intersects(brick):
                    game.playSound(brick.getHitSound())
                    brick.hit()
                    level.brickHit()
                    game.increaseScore(brick.getHitPoints())
                    ball.changeDirection(brick)
                    break

            if ball.intersects(pad):
                game.playSound(GameConstants.SOUND_HIT_PAD)
                ball.changeDirection(pad)



            ball.updatePosition()

            # if the ball has touched the bottom of the screen, it is dead
            if ball.isBallDead():
                ball.setMotion(0)
                game.reduceLives()

            game.screen.blit(ball.getSprite(), ball.getPosition())

        for brick in game.getLevel().getBricks():
            # if the brick in not destroyed, then render it
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        # set the pad position and render it to the screen
        # the pad will only move along the OX axis
        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1]))
        game.screen.blit(pad.getSprite(), pad.getPosition())


        self.clearText()

        self.addText("Your score: " + str(game.getScore()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 60,
                     size = 30)

        self.addText("Your lives: " + str(game.getLives()),
                     x = 0,
                     y = GameConstants.SCREEN_SIZE[1] - 30,
                     size = 30)



    def handleEvents(self, events):
        # IMPORTANT NOTE: When you override a class, you have
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in self.getGame().getBalls():
                    ball.setMotion(1)