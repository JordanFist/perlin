from numpy import linspace, sqrt, inf, zeros
from perlin_noise import PerlinNoise


class Map:
    def __init__(self, mapSize, seed=None):
        self.mapSize = mapSize
        self.__seed = seed
        self.__map = zeros( (mapSize[0], mapSize[1]) )

        self.__generatePerlinMap()
    
    def getMap(self):
        return self.__map
    
    def __generatePerlinMap(self):
        self.__map = self.__perlinMap()
        self.__map = self.__map - 2 * self.__circularGradient()
        mini, maxi = self.__minMax()
        self.__map = self.__bijection(mini, maxi)
           
    def __perlinMap(self):
        noise1 = PerlinNoise(octaves=3, seed=self.__seed)
        noise2 = PerlinNoise(octaves=6, seed=self.__seed)
        noise3 = PerlinNoise(octaves=12, seed=self.__seed)
        noise4 = PerlinNoise(octaves=24, seed=self.__seed)

        for i in range(self.mapSize[1]):
            for j in range(self.mapSize[0]):
                noise_val =  1   *   noise1([i/self.mapSize[1], j/self.mapSize[0]])
                noise_val += 1/2 *   noise2([i/self.mapSize[1], j/self.mapSize[0]])
                noise_val += 1/4 *   noise3([i/self.mapSize[1], j/self.mapSize[0]])
                noise_val += 1/8 *   noise4([i/self.mapSize[1], j/self.mapSize[0]])
                self.__map[i][j] = noise_val
        return self.__map
    
    def __minMax(self):
        mini = inf
        maxi = -inf
        for array in self.__map:
            mini = min(mini, min(array))
            maxi = max(maxi, max(array))
        return mini, maxi

    def __bijection(self, mini, maxi):
        if (mini == maxi):
            print("mini can't be equal to maxi")
            return None
        return (self.__map - mini) / (maxi - mini)

    def __circularGradient(self):
        x = linspace(-1/sqrt(2), 1/sqrt(2), self.mapSize[1])[:, None]
        y = linspace(-1/sqrt(2), 1/sqrt(2), self.mapSize[0])[None, :]
        return sqrt(x ** 2 + y ** 2) 

