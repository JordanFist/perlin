from game.src.ui.Sprite import Sprite

class Player:
    def __init__(self, mapSize):
        self.__VELOCITY = 2

        self.__X  = mapSize[0] // 2
        self.__Y = mapSize[1] // 2
    
    """ Returns player position in pixel """
    def getPosition(self):
        return (self.__X, self.__Y)

    """ Returns player indexes in the map (row, col) """
    def getIndex(self):
        return (self.__Y // Sprite.GROUND_TILE_SIZE, self.__X // Sprite.GROUND_TILE_SIZE)
    
    """ Returns player offset (xOff, yOff) """
    def getOffSet(self):
        return (self.__X % Sprite.GROUND_TILE_SIZE, self.__Y % Sprite.GROUND_TILE_SIZE)
    
    def moveLeft(self):
        self.__X -= self.__VELOCITY
    
    def moveRight(self):
        self.__X += self.__VELOCITY

    def moveUp(self):
        self.__Y -= self.__VELOCITY

    def moveDown(self):
        self.__Y += self.__VELOCITY
    
