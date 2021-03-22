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

height = 100
width = 100

""" Returns a circular gradient with values between 0 and 1 """
def circularGradient():
    x = linspace(-1/sqrt(2), 1/sqrt(2), width)[:, None]
    y = linspace(-1/sqrt(2), 1/sqrt(2), height)[None, :]
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
    noise1 = PerlinNoise(octaves=3, seed=1)
    noise2 = PerlinNoise(octaves=6, seed=1)
    noise3 = PerlinNoise(octaves=12, seed=1)
    noise4 = PerlinNoise(octaves=24, seed=1)

    map = zeros((height, width))
    for i in range(height):
        for j in range(width):
            noise_val =          noise1([i/height, j/width])
            noise_val += 1/2 *   noise2([i/height, j/width])
            noise_val += 1/4 *   noise3([i/height, j/width])
            noise_val += 1/8 *   noise4([i/height, j/width])
            map[i][j] = noise_val
    return map

def generatePerlinMap():
    map = perlinMap()
    map = map - 1 * circularGradient()
    mini, maxi = minmax(map)
    map = bijection(map, mini, maxi)
    return map




#circularGradient = circularGradient()
#plt.imshow(circularGradient, cmap='gray')
#plt.show()


#map = perlin() - circularGradient
#map = generatePerlinMap()
#mini, maxi = minmax(map)
#print(mini, maxi)
#map = bijection(map, mini, maxi)
#print(minmax(map))
#plt.imshow(map, cmap='gray')
#plt.show()
