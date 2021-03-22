from perlin import generatePerlinMap
from random import uniform



from matrix import *

map = generatePerlinMap()
zoom = 16


def displayMap(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] > 0.95:
                pygame.draw.rect(screen, "white", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            elif map[i][j] > 0.85:
                pygame.draw.rect(screen, "grey", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            elif map[i][j] > 0.50:
                pygame.draw.rect(screen, "lightgreen", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            elif map[i][j] > 0.45:
                pygame.draw.rect(screen, "yellow", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            elif map[i][j] > 0.37:
                pygame.draw.rect(screen, "blue", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            else:
                pygame.draw.rect(screen, "darkblue", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))

            """elif map[i][j] > 0.9:
                pygame.draw.rect(screen, "white", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            elif map[i][j] > 0.9:
                pygame.draw.rect(screen, "white", pygame.Rect(zoom*j, zoom*i, zoom*j+zoom, zoom*i+zoom))
            """




import sys, pygame

def displayPlayer(screenSize):
    pygame.draw.circle(screen, "black", (screenSize[0]/2, screenSize[1]/2), zoom/2)

pygame.init()
height = 500
width = 500
screenSize = (height, width)
screen = pygame.display.set_mode(screenSize)
done = False

velocity = 0.1

coordX = len(map)//2
coordY = len(map)//2


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            coordY += velocity
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            coordY -= velocity
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            coordX -= velocity
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            coordX += velocity
    
    
    displayMap(getSubMatrix(map, (coordX, coordY), screenSize, zoom))
    displayPlayer(screenSize)
    

    pygame.display.flip()