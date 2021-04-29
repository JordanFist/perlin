from numpy import linspace, sqrt, inf, zeros, array
from perlin_noise import PerlinNoise
from numpy import array

from src.core.Node import Node
from src.core.enums.Tiles import Tiles
from src.core.utils.Coordinates import Coordinates
from src.core.utils.Dimensions import Dimensions
from src.core.utils.Indexes import Indexes
from src.core.utils.Converter import Converter

class Map:
    def __init__(self, seed=None):
        self.__MAP_SIZE = Dimensions(100, 100)
        self.__GRADIENT_FACTOR = 2

        self.__seed = seed
        self.__map = zeros(( self.__MAP_SIZE.height, self.__MAP_SIZE.width ))

        self.__generatePerlinMap()
    
    def get(self):
        return self.__map

    def getIndex(self, position):
        row, col = (int(Converter.pixelToIndex(position.y)), int(Converter.pixelToIndex(position.x)))
        return Indexes(row, col)

    def getType(self, position):
        if type(position) == Coordinates:
            row, col = (int(Converter.pixelToIndex(position.y)), int(Converter.pixelToIndex(position.x)))
            return self.__map[row][col].getTileID()
        if type(position) == Indexes:
            return self.__map[position.row][position.col].getTileID()

    """ Returns the size of the map in pixel """
    def getSize(self):
        return Converter.indexToPixel(self.__MAP_SIZE)

    def isInMap(self, position):
        if type(position) == Coordinates:
            if (position.x >= 0 and position.x < self.getSize().width and position.y >= 0 and position.y < self.getSize().height):
                return True
            return False
        if type(position) == Indexes:
            if (position.row >= 0 and position.row < self.__MAP_SIZE.height and position.col >= 0 and position.col < self.__MAP_SIZE.width):
                return True
            return False

    def __generatePerlinMap(self):
        self.__perlinMap()
        self.__map = self.__map - self.__GRADIENT_FACTOR * self.__circularGradient()
        mini, maxi = self.__minMax()
        self.__map = self.__bijection(mini, maxi)
        self.__map = self.__intToNodes()
    
    """ Returns a circular gradient between 0 and 1 """
    def __circularGradient(self):
        x = linspace(-1/sqrt(2), 1/sqrt(2), self.__MAP_SIZE.width)[None, :]
        y = linspace(-1/sqrt(2), 1/sqrt(2), self.__MAP_SIZE.height)[:, None]
        return sqrt(x ** 2 + y ** 2) 

    def __minMax(self):
        mini = inf
        maxi = -inf
        for array in self.__map:
            mini = min(mini, min(array))
            maxi = max(maxi, max(array))
        return mini, maxi

    def __bijection(self, mini, maxi):
        if (mini == maxi):
            raise Exception("mini can't be equal to maxi")
        return (self.__map - mini) / (maxi - mini)

    def __intToNodes(self):
        map = []
        for i in range(self.__MAP_SIZE.height):
            row = []
            for j in range(self.__MAP_SIZE.width):
                row.append(Node(Tiles.getPatches(self.__map, i, j)))
            map.append(row)
        return map

    def __perlinMap(self):
        noise1 = PerlinNoise(octaves = 3, seed = self.__seed)
        noise2 = PerlinNoise(octaves = 6, seed = self.__seed)
        noise3 = PerlinNoise(octaves = 12, seed = self.__seed)
        noise4 = PerlinNoise(octaves = 24, seed = self.__seed)

        for i in range(self.__MAP_SIZE.height):
            for j in range(self.__MAP_SIZE.width):
                noise_val =  1   *   noise1([i/self.__MAP_SIZE.height, j/self.__MAP_SIZE.width])
                noise_val += 1/2 *   noise2([i/self.__MAP_SIZE.height, j/self.__MAP_SIZE.width])
                noise_val += 1/4 *   noise3([i/self.__MAP_SIZE.height, j/self.__MAP_SIZE.width])
                noise_val += 1/8 *   noise4([i/self.__MAP_SIZE.height, j/self.__MAP_SIZE.width])
                self.__map[i][j] = noise_val