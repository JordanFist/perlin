import pygame
from numpy import sqrt

from src.core.enums.Direction import Direction
from src.core.utils.Coordinates import Coordinates

""" 
The position of the player is represented by the top left corner position of his sprite 
His WALKIND_SPEED is in pixels/second
"""
class Player:
    def __init__(self, sprites, initialPosition):
        self.__SPEED_FACTOR = 1.5
        self.__WALKING_SPEED = 400 
        self.__RUNNING_SPEED = self.__SPEED_FACTOR * self.__WALKING_SPEED

        self.__sprite = sprites.init()
        self.__sprites = sprites
        self.__idle = True
        self.__direction = Direction.DOWN
        self.__position = initialPosition
        self.__speed = self.__WALKING_SPEED
        self.__VelocityX = 0
        self.__VelocityY = 0
    
    """ Returns player position in pixel """
    def getPosition(self):
        return self.__position

    def getNextPosition(self, direction, elapsedTime):
        if (direction == Direction.LEFT):
            return Coordinates(self.__position.x - self.__speed * elapsedTime, self.__position.y)
        elif (direction == Direction.RIGHT):
            return Coordinates(self.__position.x + self.__speed * elapsedTime, self.__position.y)
        elif (direction == Direction.UP):
            return Coordinates(self.__position.x, self.__position.y - self.__speed * elapsedTime)
        elif (direction == Direction.DOWN):
            return Coordinates(self.__position.x, self.__position.y + self.__speed * elapsedTime)

    def adjustPosition(self, elapsedTime):
        lenght = sqrt(self.__VelocityX ** 2 + self.__VelocityY ** 2)
        if (self.__VelocityX != 0 and self.__VelocityY != 0):
            tweakX = self.__VelocityX * self.__speed/lenght
            tweakY = self.__VelocityY * self.__speed/lenght
            self.__position.x += - self.__VelocityX * self.__speed * elapsedTime + tweakX * elapsedTime
            self.__position.y += - self.__VelocityY * self.__speed * elapsedTime + tweakY * elapsedTime

        self.__VelocityX = 0
        self.__VelocityY = 0
    
    def getVelocity(self):
        return self.__VELOCITY

    def getCollision(self):
        return self.__sprite.getCollision()

    def getNextCollision(self, direction, elapsedTime):
        pos = self.getNextPosition(direction, elapsedTime)
        nextCollision = pygame.Rect(pos.x + self.__sprite.COLLISION_MARGIN, pos.y + self.__sprite.COLLISION_MARGIN, 
                        self.__sprite.getSize().width - 2 * self.__sprite.COLLISION_MARGIN, self.__sprite.getSize().height - 2 * self.__sprite.COLLISION_MARGIN)
        return nextCollision

    def getSprite(self):
        return self.__sprite

    def changeSprite(self, index=None):
        rect = self.__sprite.getRect()
        if index == None:
            if self.__idle:
                return False
            self.__sprite = self.__sprites.idle(self.__direction)
            self.__idle = True
        else:
            self.__sprite = self.__sprites.get(index)
            self.__idle = False
        self.__sprite.setPosition(Coordinates(*rect.topleft))
        return True

    def run(self):
        self.__speed = self.__RUNNING_SPEED

    def walk(self):
        self.__speed = self.__WALKING_SPEED

    def update(self, position):
        self.__sprite.setPosition(position)

    def move(self, direction, elapsedTime):
        if direction == Direction.UP:
            self.__direction = Direction.UP
            self.__position.y -= self.__speed * elapsedTime
            self.__VelocityY -= 1
        if direction == Direction.DOWN:
            self.__direction = Direction.DOWN
            self.__position.y += self.__speed * elapsedTime
            self.__VelocityY += 1
        if direction == Direction.LEFT:
            self.__direction = Direction.LEFT
            self.__position.x -= self.__speed * elapsedTime
            self.__VelocityX -= 1
        if direction == Direction.RIGHT:
            self.__direction = Direction.RIGHT
            self.__position.x += self.__speed * elapsedTime
            self.__VelocityX += 1