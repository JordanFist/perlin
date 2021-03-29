import pygame

from game.src.core.Player import Player
from game.src.core.Map import Map
from game.src.core.View import View
from game.src.core.TilesEnum import TilesEnum
from game.src.core.Direction import Direction


from game.src.ui.Window import Window
from game.src.ui.Display import Display
from game.src.ui.Sprite import Sprite
from game.src.ui.SpriteStore import SpriteStore

class GameLoop:
    def __init__(self, seed=None):
        self.__map = Map(seed) 

        self.__player = Player(self.__map.getSize())

        self.__window = Window()
        self.__view = View()
        self.__display = Display()

        self.__spriteStore = SpriteStore()

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

    def __canWalk(self, direction):
        row, col = self.__player.getNextIndex(direction)
        return  self.__view.isInMap(self.__map, self.__player, direction) and \
                TilesEnum.getID(self.__map.get()[row][col]) > TilesEnum.SHALLOW_WATER

    def __playerInteraction(self, keysPressed):
        hasMoved = False
        if keysPressed[pygame.K_q] and self.__canWalk(Direction.LEFT):
            self.__player.moveLeft()
            hasMoved = True
        if keysPressed[pygame.K_d] and self.__canWalk(Direction.RIGHT):
            self.__player.moveRight()
            hasMoved = True
        if keysPressed[pygame.K_z] and self.__canWalk(Direction.UP):
            self.__player.moveUp()
            hasMoved = True
        if keysPressed[pygame.K_s] and self.__canWalk(Direction.DOWN):
            self.__player.moveDown()
            hasMoved = True
        self.__player.adjustPosition()
        return hasMoved

    def __repaint(self):
        self.__view.setView(self.__map, self.__player)
        self.__display.update(self.__view, self.__window, self.__player, self.__spriteStore)

    def run(self):
        running = True

        keysPressed = {
            pygame.K_q:False,
            pygame.K_d:False,
            pygame.K_z:False,
            pygame.K_s:False
        }

        self.__repaint()

        while running:            
            for event in pygame.event.get():
                running = self.__isWindowClosed(event)
                self.__isKeyPressed(event, keysPressed)
                
            hasMoved = self.__playerInteraction(keysPressed)
            if (hasMoved):
                self.__repaint()

            pygame.display.flip()
            self.__window.clock()
