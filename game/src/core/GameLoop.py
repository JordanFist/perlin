import pygame

from game.src.core.Player import Player
from game.src.core.Map import Map
from game.src.ui.Window import Window
from game.src.ui.View import View
from game.src.ui.Display import Display

class GameLoop:
    def __init__(self, seed=None):
        self.__map = Map(seed) 

        self.__player = Player(self.__map.getSize())

        self.__window = Window()
        self.__view = View(self.__window.getSize())
        self.__display = Display()

        self.run()

    def __isWindowClosed(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    def __isKeyPressed(self, event, keysPressed):
        if event.type == pygame.KEYDOWN:
            keysPressed[event.key] = True
        if event.type == pygame.KEYUP:
            keysPressed[event.key] = False

    def __movePlayer(self, keysPressed):
        #print(self.__player.getPosition())
        res = False
        if keysPressed[pygame.K_RIGHT] and self.__player.getPosition()[0] < self.__map.getSize()[0] - (self.__window.getSize()[0] // 2):
            self.__player.moveRight()
            res = True
        if keysPressed[pygame.K_LEFT] and self.__player.getPosition()[0] > self.__window.getSize()[0] // 2:
            self.__player.moveLeft()
            res = True
        if keysPressed[pygame.K_UP] and self.__player.getPosition()[1] > self.__window.getSize()[1] // 2:
            self.__player.moveUp()
            res = True
        if keysPressed[pygame.K_DOWN] and self.__player.getPosition()[1] < self.__map.getSize()[1] - (self.__window.getSize()[1] // 2):
            self.__player.moveDown()
            res = True
        return res

    def __repaint(self):
        view = self.__view.get(self.__map.get(), self.__player.getIndex())
        self.__display.update(view, self.__window.screen, self.__player.getOffSet())

    def run(self):
        running = True

        keysPressed = {
            pygame.K_RIGHT:False,
            pygame.K_LEFT:False,
            pygame.K_UP:False,
            pygame.K_DOWN:False
        }

        self.__repaint()

        while running:
            for event in pygame.event.get():
                running = self.__isWindowClosed(event)
                self.__isKeyPressed(event, keysPressed)
                
            hasMoved = self.__movePlayer(keysPressed)
            if (hasMoved):
                self.__repaint()

            pygame.display.flip()