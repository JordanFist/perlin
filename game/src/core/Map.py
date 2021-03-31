from numpy import linspace, sqrt, inf, zeros, array
from perlin_noise import PerlinNoise
from game.src.ui.Sprite import Sprite

class Map:
    def __init__(self, seed=None):
        self.__MAP_SIZE = (100, 120) #row, col
        self.__GRADIENT_FACTOR = 2

        self.__seed = seed
        self.__map = zeros((self.__MAP_SIZE[0], self.__MAP_SIZE[1]))

        self.__generatePerlinMap()
    
    def get(self):
        return self.__map

    """ Returns the index of the position in the map (row, col) """
    def getIndex(self, position):
        return (position[1] // Sprite.GROUND_TILE_SIZE, position[0] // Sprite.GROUND_TILE_SIZE)

    """ Returns the size of the map in pixel (row, col) """
    def getSize(self):
        return array([self.__MAP_SIZE[0] * Sprite.GROUND_TILE_SIZE, self.__MAP_SIZE[1] * Sprite.GROUND_TILE_SIZE])

    def __generatePerlinMap(self):
        self.__perlinMap()
        self.__map = self.__map - self.__GRADIENT_FACTOR * self.__circularGradient()
        mini, maxi = self.__minMax()
        self.__map = self.__bijection(mini, maxi)
    
    """ Returns a circular gradient between 0 and 1 """
    def __circularGradient(self):
        x = linspace(-1/sqrt(2), 1/sqrt(2), self.__MAP_SIZE[0])[:, None]
        y = linspace(-1/sqrt(2), 1/sqrt(2), self.__MAP_SIZE[1])[None, :]
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
            print(  "Error: mini can't be equal to maxi",
                    "\nFile: " + __file__,
                    "\nFunction: bijection")            
            return None
            
        return (self.__map - mini) / (maxi - mini)

    def __perlinMap(self):
        noise1 = PerlinNoise(octaves = 3, seed = self.__seed)
        noise2 = PerlinNoise(octaves = 6, seed = self.__seed)
        noise3 = PerlinNoise(octaves = 12, seed = self.__seed)
        noise4 = PerlinNoise(octaves = 24, seed = self.__seed)

        for i in range(self.__MAP_SIZE[0]):
            for j in range(self.__MAP_SIZE[1]):
                noise_val =  1   *   noise1([i/self.__MAP_SIZE[0], j/self.__MAP_SIZE[1]])
                noise_val += 1/2 *   noise2([i/self.__MAP_SIZE[0], j/self.__MAP_SIZE[1]])
                noise_val += 1/4 *   noise3([i/self.__MAP_SIZE[0], j/self.__MAP_SIZE[1]])
                noise_val += 1/8 *   noise4([i/self.__MAP_SIZE[0], j/self.__MAP_SIZE[1]])
                self.__map[i][j] = noise_val