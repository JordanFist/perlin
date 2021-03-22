from perlin import generatePerlinMap
from random import uniform

map = generatePerlinMap()
zoom = 5


def displayMap(map2):
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

#Pygame : 
import sys, pygame

pygame.init()
screen = pygame.display.set_mode((zoom * len(map), zoom * len(map)))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    displayMap(map)
    
    pygame.display.flip()