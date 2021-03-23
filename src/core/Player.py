class Player:
    def __init__(self, mapSize, tileSize, velocity = 1):
        self.__X  = mapSize[0] * tileSize // 2
        self.__Y = mapSize[1] * tileSize // 2
        self.__velocity = velocity
    
    def getPosition(self):
        return (self.__X, self.__Y)
    
    def moveLeft(self):
        self.__X -= self.__velocity
    
    def moveRight(self):
        self.__X += self.__velocity

    def moveUp(self):
        self.__Y -= self.__velocity

    def moveDown(self):
        self.__Y += self.__velocity
    
