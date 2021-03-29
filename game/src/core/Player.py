from numpy import sqrt
from game.src.ui.Sprite import Sprite
from game.src.core.Direction import Direction

class Player:
    def __init__(self, mapSize):
        self.__SPEED = 4

        self.__X  = mapSize[0] // 2
        self.__Y = mapSize[1] // 2
        self.__VelocityX = 0
        self.__VelocityY = 0
    
    """ Returns player position in pixel """
    def getPosition(self):
        return (self.__X, self.__Y)

    """ Returns player indexes in the map (row, col) """
    def getIndex(self):
        return (self.__Y // Sprite.GROUND_TILE_SIZE, self.__X // Sprite.GROUND_TILE_SIZE)

    def getNextPosition(self, direction):
        if (direction == Direction.LEFT):
            return (self.__X - self.__SPEED, self.__Y)
        elif (direction == Direction.RIGHT):
            return (self.__X + self.__SPEED, self.__Y)
        elif (direction == Direction.UP):
            return (self.__X, self.__Y - self.__SPEED)
        elif (direction == Direction.DOWN):
            return (self.__X, self.__Y + self.__SPEED)

    def getNextIndex(self, direction):
        pos = self.getNextPosition(direction)
        return (pos[1] // Sprite.GROUND_TILE_SIZE, pos[0] // Sprite.GROUND_TILE_SIZE)
    
    """ Returns player offset (xOff, yOff) """
    def getOffSet(self):
        return (self.__X % Sprite.GROUND_TILE_SIZE, self.__Y % Sprite.GROUND_TILE_SIZE)
    
    def getVelocity(self):
        return self.__VELOCITY

    def adjustPosition(self):
        lenght = sqrt(self.__VelocityX ** 2 + self.__VelocityY ** 2)
        if (self.__VelocityX != 0 and self.__VelocityY != 0):
            tweakX = int(self.__VelocityX * self.__SPEED/lenght)
            tweakY = int(self.__VelocityY * self.__SPEED/lenght)
            self.__X = self.__X - self.__VelocityX * self.__SPEED + tweakX
            self.__Y = self.__Y - self.__VelocityY * self.__SPEED + tweakY

        self.__VelocityX = 0
        self.__VelocityY = 0

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
    
