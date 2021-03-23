from numpy import linspace, sqrt, inf, zeros
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
from time import time

""" 
-1 est noir et 1 et blanc
le noir reprensente l'eau, le blanc les sommets

diviser par height ou width dans la fonction noise permet 
de gerer le zoom sur le bruit i * scale plus scale est grand plus
on dezoom

il faut stocker la map si on veut plus tard une camera
"""

mapSize = (100, 100) #width, height

""" Returns a circular gradient with values between 0 and 1 """
def circularGradient():
    x = linspace(-1/sqrt(2), 1/sqrt(2), mapSize[1])[:, None]
    y = linspace(-1/sqrt(2), 1/sqrt(2), mapSize[0])[None, :]
    return sqrt(x ** 2 + y ** 2)  

def bijection(map, mini, maxi):
    if (mini == maxi):
        print("mini can't be equal to maxi")
        return None
    return (map - mini) / (maxi - mini)

def minmax(map):
    mini = inf
    maxi = -inf
    for array in map:
        mini = min(mini, min(array))
        maxi = max(maxi, max(array))
    return mini, maxi


def perlinMap():
    noise1 = PerlinNoise(octaves=3, seed=None)
    noise2 = PerlinNoise(octaves=6, seed=None)
    noise3 = PerlinNoise(octaves=12, seed=None)
    noise4 = PerlinNoise(octaves=24, seed=None)

    map = zeros((mapSize[1], mapSize[0]))
    for i in range(mapSize[1]):
        for j in range(mapSize[0]):
            noise_val =          noise1([i/mapSize[1], j/mapSize[0]])
            noise_val += 1/2 *   noise2([i/mapSize[1], j/mapSize[0]])
            noise_val += 1/4 *   noise3([i/mapSize[1], j/mapSize[0]])
            noise_val += 1/8 *   noise4([i/mapSize[1], j/mapSize[0]])
            map[i][j] = noise_val
    return map

def generatePerlinMap():
    map = perlinMap()
    map = map - 2 * circularGradient()
    mini, maxi = minmax(map)
    map = bijection(map, mini, maxi)
    return map



#circularGradient = circularGradient()
#plt.imshow(circularGradient, cmap='gray')
#plt.show()


#map = perlin() - circularGradient
map = generatePerlinMap()
#mini, maxi = minmax(map)
#print(mini, maxi)
#map = bijection(map, mini, maxi)
#print(minmax(map))
plt.imshow(map, cmap='gray')
plt.show()
