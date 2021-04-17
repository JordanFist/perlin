import pygame

from game.src.core.Map import Map
from game.src.core.Player import Player
from game.src.core.enums.Tiles import Tiles
from game.src.core.enums.Direction import Direction
from game.src.core.utils.Coordinates import Coordinates
from game.src.core.enums.States import States

from game.src.ui.Window import Window
from game.src.ui.display.DisplayGame import DisplayGame
from game.src.ui.Camera import Camera
from game.src.ui.background.BackgroundGame import BackgroundGame
from game.src.ui.sprite.Sprite import Sprite
from game.src.ui.sprite.SpriteStore import SpriteStore

class GameLoop:
    def __init__(self, window, seed=None):
        self.__window = window

        self.__map = Map(seed) 
        self.__spriteStore = SpriteStore()
        self.__background = BackgroundGame(self.__map, self.__spriteStore)

        initialPlayerPosition = Coordinates(self.__map.getSize().width // 2, self.__map.getSize().height // 2)
        self.__player = Player(self.__spriteStore.getPlayer(), initialPlayerPosition)
        self.__camera = Camera(self.__player, self.__map.getSize())
        self.__display = DisplayGame(self.__window, self.__background, self.__camera)
        self.__display.add(self.__player)

    def __resize(self, event):
        self.__window.resize(event.w, event.h)
        self.__camera.resetCamera()
        self.__display.flip()

    def __canWalk(self, direction):
        playerCorners = self.__player.getNextCorners(direction)
        return  self.__map.isInMap(playerCorners[2]) and self.__map.isInMap(playerCorners[3]) and \
                self.__map.getType(playerCorners[2]) > Tiles.SHALLOW_WATER and \
                self.__map.getType(playerCorners[3]) > Tiles.SHALLOW_WATER

    def __playerMoved(self, keysPressed):
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

    def run(self):
        running = States.CONTINUE
        self.__display.flip()

        while running == States.CONTINUE:   
            updated = False
            for event in pygame.event.get():
                running = self.__window.isClosed(event)

                if self.__window.isResized(event):
                    self.__resize(event)

            if self.__playerMoved(pygame.key.get_pressed()):
                self.__display.toUpdate(self.__player)
                updated = True

            if updated:
                self.__display.update()

            self.__window.clock()    
        
        if (running == States.QUIT):
            self.__window.close()
