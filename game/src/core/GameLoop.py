import pygame

from src.core.Map import Map
from src.core.Player import Player
from src.core.enums.Tiles import Tiles
from src.core.enums.Direction import Direction
from src.core.enums.States import States
from src.core.utils.Coordinates import Coordinates

from src.ui.Window import Window
from src.ui.Camera import Camera
from src.ui.display.DisplayGame import DisplayGame
from src.ui.background.BackgroundGame import BackgroundGame
from src.ui.sprite.Sprite import Sprite
from src.ui.sprite.Sprites import Sprites
from src.ui.sprite.SpriteStore import SpriteStore

class GameLoop:
    def __init__(self, window, seed=None):
        self.__window = window

        self.__map = Map(seed) 
        self.__spriteStore = SpriteStore()
        self.__background = BackgroundGame(self.__map, self.__spriteStore)

        initialPlayerPosition = Coordinates(self.__map.getSize().width // 2, self.__map.getSize().height // 2)
        self.__player = Player(Sprites(self.__spriteStore.getPlayer()), initialPlayerPosition)
        self.__camera = Camera(self.__player, self.__map.getSize())
        self.__display = DisplayGame(self.__window, self.__background, self.__camera)
        self.__display.add(self.__player)

    def __resize(self, event):
        self.__window.resize(event.w, event.h)
        self.__camera.resetCamera()
        self.__display.flip()

    def __canWalk(self, direction, elapsedTime):
        collision = self.__player.getNextCollision(direction, elapsedTime)
        bottomLeft = Coordinates(*collision.bottomleft)
        bottomRight = Coordinates(*collision.bottomright)
        return  self.__map.isInMap(bottomLeft) and self.__map.isInMap(bottomRight) and \
                self.__map.getType(bottomLeft) > Tiles.SHALLOW_WATER and \
                self.__map.getType(bottomRight) > Tiles.SHALLOW_WATER

    def __playerInteraction(self, keysPressed, elapsedTime, frame):
        hasMoved = False
        keys = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]
        for key in keys:
            direction = Direction.keyToDir(key)
            if keysPressed[key] and self.__canWalk(direction, elapsedTime):
                self.__player.move(direction, elapsedTime)
                hasMoved = self.__player.changeSprite(direction * Sprites.NUMBER_OF_ANIMATION_FRAMES + frame)

        if keysPressed[pygame.K_LSHIFT]: #//REVIEW update ONE_FRAME_DURATION while running
            self.__player.run()
        if not keysPressed[pygame.K_LSHIFT]:
            self.__player.walk()

        if not hasMoved:
            hasMoved = self.__player.changeSprite()
        
        self.__player.adjustPosition(elapsedTime)
        return hasMoved

    def run(self):
        running = States.CONTINUE
        self.__display.flip()

        nextFrame = self.__window.getTicks()
        frame = 0

        while running == States.CONTINUE:               
            updated = False
            for event in pygame.event.get():
                if self.__window.isClosed(event):
                    running = States.QUIT

                if self.__window.isResized(event):
                    self.__resize(event)
            
            if self.__window.getTicks() > nextFrame:
                frame = (frame + 1) % Sprites.NUMBER_OF_ANIMATION_FRAMES          
                nextFrame += Window.ONE_FRAME_DURATION

            if self.__playerInteraction(pygame.key.get_pressed(), self.__window.getTime(), frame):
                self.__display.toUpdate(self.__player)
                updated = True

            if updated:
                self.__display.update()

            self.__window.clock()
        
        if (running == States.QUIT):
            self.__window.close()