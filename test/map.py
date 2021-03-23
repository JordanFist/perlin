from perlin import *
from matrix import getViewMatrix

map = generatePerlinMap() 
windowSize = (1080, 720) #width=x, height=y
tileSize = 32
#reelMapSize = (mapSize[0] * tileSize, mapSize[1] * tileSize)
viewSize = (windowSize[0] // tileSize + 1, windowSize[1] // tileSize + 1)

def displayMap(map, xOff, yOff):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] > 0.95:
                pygame.draw.rect(screen, "white", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))
            elif map[i][j] > 0.85:
                pygame.draw.rect(screen, "grey", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))
            elif map[i][j] > 0.50:
                pygame.draw.rect(screen, "lightgreen", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))
            elif map[i][j] > 0.45:
                pygame.draw.rect(screen, "yellow", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))
            elif map[i][j] > 0.37:
                pygame.draw.rect(screen, "blue", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))
            else:
                pygame.draw.rect(screen, "darkblue", pygame.Rect(j * tileSize - xOff, i * tileSize - yOff, tileSize, tileSize))

            """elif map[i][j] > 0.9:
                pygame.draw.rect(screen, "white", pygame.Rect(tileSize*j, tileSize*i, tileSize*j+tileSize, tileSize*i+tileSize))
            elif map[i][j] > 0.9:
                pygame.draw.rect(screen, "white", pygame.Rect(tileSize*j, tileSize*i, tileSize*j+tileSize, tileSize*i+tileSize))
            """

def displayPlayer(windowSize):
    pygame.draw.rect(screen, "black", pygame.Rect(windowSize[0]//2, windowSize[1]//2, tileSize, tileSize))

velocity = 1
playerX = tileSize * mapSize[0] // 2 
playerY = tileSize * mapSize[1] // 2 

import sys, pygame

pygame.init()
screen = pygame.display.set_mode(windowSize)
done = False

#displayMap est appelé lorsqu'un mouvement se passe sinon non

movementsKeys = {
    pygame.K_RIGHT:False,
    pygame.K_LEFT:False,
    pygame.K_UP:False,
    pygame.K_DOWN:False
}




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            movementsKeys[event.key] = True
        if event.type == pygame.KEYUP:
            movementsKeys[event.key] = False
        

    if movementsKeys[pygame.K_RIGHT]:
        playerX += velocity
    if movementsKeys[pygame.K_LEFT]:
        playerX -= velocity
    if movementsKeys[pygame.K_UP]:
        playerY -= velocity
    if movementsKeys[pygame.K_DOWN]:
        playerY += velocity
    

    xOff = playerX % tileSize
    yOff = playerY % tileSize

    #displayMap(map, xOff, yOff)
    view = getViewMatrix(map, playerX, playerY, tileSize, viewSize)
    displayMap(view, xOff, yOff)
    displayPlayer(windowSize)

    pygame.display.flip()