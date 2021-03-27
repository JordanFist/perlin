import pygame

from game.src.core.Player import Player
from game.src.core.Map import Map
from game.src.ui.Window import Window
from game.src.ui.View import View
from game.src.ui.Display import Display
from game.src.ui.Sprite import Sprite
from game.src.ui.SpriteStore import SpriteStore

class GameLoop:
    def __init__(self, seed=None):
        self.__map = Map(seed) 

        self.__player = Player(self.__map.getSize())

        self.__window = Window()
        self.__view = View(self.__window.getSize())
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

    def __movePlayer(self, keysPressed):
        res = False
        if keysPressed[pygame.K_d] and self.__player.getPosition()[0] + self.__player.getVelocity() < self.__map.getSize()[0] - (self.__window.getSize()[0] // 2) - Display.DISPLAY_OFFSET * Sprite.GROUND_TILE_SIZE:
            self.__player.moveRight()
            res = True
        if keysPressed[pygame.K_q] and self.__player.getPosition()[0] - self.__player.getVelocity() > self.__window.getSize()[0] // 2 + Display.DISPLAY_OFFSET * Sprite.GROUND_TILE_SIZE:
            self.__player.moveLeft()
            res = True
        if keysPressed[pygame.K_z] and self.__player.getPosition()[1] - self.__player.getVelocity() > self.__window.getSize()[1] // 2 + Display.DISPLAY_OFFSET * Sprite.GROUND_TILE_SIZE:
            self.__player.moveUp()
            res = True
        if keysPressed[pygame.K_s] and self.__player.getPosition()[1] + self.__player.getVelocity() < self.__map.getSize()[1] - (self.__window.getSize()[1] // 2) - Display.DISPLAY_OFFSET * Sprite.GROUND_TILE_SIZE:
            self.__player.moveDown()
            res = True
        return res

    def __repaint(self):
        view = self.__view.get(self.__map.get(), self.__player.getIndex())
        self.__display.update(view, self.__window.getScreen(), self.__player.getOffSet(), self.__spriteStore)

    def run(self):
        running = True

        keysPressed = {
            pygame.K_d:False,
            pygame.K_q:False,
            pygame.K_z:False,
            pygame.K_s:False
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
            self.__window.clock()
