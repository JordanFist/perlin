from numpy import *
from perlin import *   

def getViewMatrix(map, playerX, playerY, tileSize, viewSize):
    indexX = playerY // tileSize 
    indexY = playerX // tileSize 

    viewHeight = viewSize[0] // 2 + 1
    viewWidth = viewSize[1] // 2 + 1

    #print(indexX - viewWidth, indexX + viewWidth, indexY - viewHeight, indexY + viewHeight )
        
    return map[indexX - viewWidth : indexX + viewWidth, indexY - viewHeight : indexY + viewHeight]


"""
matrix = zeros((100,100))

nbr = 0
for i in range(100):
    for j in range(100):
        nbr += 1
        matrix[i][j] = nbr
print(matrix)

print(getSubMatrix(matrix, (50, 50), (500, 500), 16))
"""