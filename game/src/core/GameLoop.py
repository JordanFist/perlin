import pygame

from game.src.core.Map import Map
from game.src.core.Player import Player
from game.src.core.Camera import Camera
from game.src.core.TilesEnum import TilesEnum
from game.src.core.Direction import Direction
from game.src.core.pair.Coordinates import Coordinates


from game.src.ui.Window import Window
from game.src.ui.Display import Display
from game.src.ui.Background import Background
from game.src.ui.Sprite import Sprite
from game.src.ui.SpriteStore import SpriteStore

class GameLoop:
    def __init__(self, window, seed=None):
        self.__window = window

        self.__map = Map(seed) 
        self.__spriteStore = SpriteStore()
        self.__background = Background(self.__map, self.__spriteStore)

        initialPlayerPosition = Coordinates(self.__map.getSize().width // 2, self.__map.getSize().height // 2)
        self.__player = Player(self.__spriteStore.getPlayer(), initialPlayerPosition)
        self.__camera = Camera(self.__player, self.__map.getSize())
        self.__display = Display(self.__window, self.__camera, self.__background, self.__spriteStore)

        self.run()

    def __isWindowClosed(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    def __windowResized(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.__window.resizeScreen(event.w, event.h)
            self.__camera.__init__(self.__player, self.__map.getSize())
            return True
        return False

    def __canWalk(self, direction):
        playerCorners = self.__player.getNextCorners(direction)
        return  self.__map.isInMap(playerCorners[1]) and self.__map.isInMap(playerCorners[2]) and \
                self.__map.getType(playerCorners[1]) > TilesEnum.SHALLOW_WATER and \
                self.__map.getType(playerCorners[2]) > TilesEnum.SHALLOW_WATER

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

    def __repaint(self):
        self.__display.update(self.__player)
        pygame.display.update()

    def run(self):
        running = True
        self.__repaint()

        while running:   
            for event in pygame.event.get():
                running = self.__isWindowClosed(event)
                if self.__windowResized(event):
                    self.__repaint()

            if self.__playerMoved(pygame.key.get_pressed()):
                self.__repaint()

            self.__window.clock()
        
