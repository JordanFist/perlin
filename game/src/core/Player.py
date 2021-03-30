from numpy import sqrt
from game.src.core.Direction import Direction

""" 
The position of the player is represented by the top left corner position of his sprite 
"""
class Player:
    def __init__(self, sprite, initialPositionPlayer):
        self.__SPEED = 4

        self.__sprite = sprite
        self.__X  = initialPositionPlayer[0]
        self.__Y = initialPositionPlayer[1]
        self.__VelocityX = 0
        self.__VelocityY = 0
    
    """ Returns player position in pixel """
    def getPosition(self):
        return (int(self.__X), int(self.__Y))

    def getNextPosition(self, direction):
        if (direction == Direction.LEFT):
            return (int(self.__X - self.__SPEED), int(self.__Y))
        elif (direction == Direction.RIGHT):
            return (int(self.__X + self.__SPEED), int(self.__Y))
        elif (direction == Direction.UP):
            return (int(self.__X), int(self.__Y - self.__SPEED))
        elif (direction == Direction.DOWN):
            return (int(self.__X), int(self.__Y + self.__SPEED))

    def adjustPosition(self):
        lenght = sqrt(self.__VelocityX ** 2 + self.__VelocityY ** 2)
        if (self.__VelocityX != 0 and self.__VelocityY != 0):
            tweakX = self.__VelocityX * self.__SPEED/lenght
            tweakY = self.__VelocityY * self.__SPEED/lenght
            self.__X = self.__X - self.__VelocityX * self.__SPEED + tweakX
            self.__Y = self.__Y - self.__VelocityY * self.__SPEED + tweakY

        self.__VelocityX = 0
        self.__VelocityY = 0
    
    def getVelocity(self):
        return self.__VELOCITY

    def getNextCorners(self, direction):
        pos = self.getNextPosition(direction)
        topLeft = (pos[0], pos[1])
        topRight = (pos[0] + self.__sprite.getWidth(), pos[1])
        bottomLeft = (pos[0], pos[1] + self.__sprite.getHeight())
        bottomRight = (pos[0] + self.__sprite.getWidth(), pos[1] + self.__sprite.getHeight())
        return [topLeft, bottomLeft, bottomRight, topRight]

    def moveLeft(self):
        self.__X -= self.__SPEED
        self.__VelocityX -= 1
    
    def moveRight(self):
        self.__X += self.__SPEED
        self.__VelocityX += 1

    def moveUp(self):
        self.__Y -= self.__SPEED
        self.__VelocityY -= 1

    def moveDown(self):
        self.__Y += self.__SPEED
        self.__VelocityY += 1
    
