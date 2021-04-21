from numpy import sqrt

from src.core.enums.Direction import Direction
from src.core.utils.Coordinates import Coordinates

""" 
The position of the player is represented by the top left corner position of his sprite 
"""
class Player:
    def __init__(self, sprite, initialPosition):
        self.__SPEED = 2

        self.__sprite = sprite
        self.__position = initialPosition
        self.__VelocityX = 0
        self.__VelocityY = 0
    
    """ Returns player position in pixel """
    def getPosition(self):
        return self.__position

    def getNextPosition(self, direction):
        if (direction == Direction.LEFT):
            return Coordinates(self.__position.x - self.__SPEED, self.__position.y)
        elif (direction == Direction.RIGHT):
            return Coordinates(self.__position.x + self.__SPEED, self.__position.y)
        elif (direction == Direction.UP):
            return Coordinates(self.__position.x, self.__position.y - self.__SPEED)
        elif (direction == Direction.DOWN):
            return Coordinates(self.__position.x, self.__position.y + self.__SPEED)

    def adjustPosition(self):
        lenght = sqrt(self.__VelocityX ** 2 + self.__VelocityY ** 2)
        if (self.__VelocityX != 0 and self.__VelocityY != 0):
            tweakX = self.__VelocityX * self.__SPEED/lenght
            tweakY = self.__VelocityY * self.__SPEED/lenght
            self.__position.x += - self.__VelocityX * self.__SPEED + tweakX
            self.__position.y += - self.__VelocityY * self.__SPEED + tweakY

        self.__VelocityX = 0
        self.__VelocityY = 0
    
    def getVelocity(self):
        return self.__VELOCITY

    def getNextCorners(self, direction):
        pos = self.getNextPosition(direction)
        topLeft = Coordinates(pos.x, pos.y)
        topRight = Coordinates(pos.x + self.__sprite.getSize().width, pos.y)
        bottomLeft = Coordinates(pos.x, pos.y + self.__sprite.getSize().height)
        bottomRight = Coordinates(pos.x + self.__sprite.getSize().width, pos.y + self.__sprite.getSize().height)
        return [topLeft, topRight, bottomRight, bottomLeft] 

    def getSprite(self):
        return self.__sprite

    def update(self, position):
        self.__sprite.setPosition(position)

    def moveLeft(self):
        self.__position.x -= self.__SPEED
        self.__VelocityX -= 1
    
    def moveRight(self):
        self.__position.x += self.__SPEED
        self.__VelocityX += 1

    def moveUp(self):
        self.__position.y -= self.__SPEED
        self.__VelocityY -= 1

    def moveDown(self):
        self.__position.y += self.__SPEED
        self.__VelocityY += 1
    
