import os
import pathlib
import pygame

class SpriteStore:
    def __init__(self, tileSize):
        self.__tileSize = tileSize

        self.__path = f"{pathlib.Path(__file__).parent.absolute()}\\game\\resources"
        self.__groundPath = self.__path + "\\ground"
        
        self.__groundFiles = []
        for elem in os.listdir(self.__groundPath):
            image = pygame.image.load(f"{self.__groundPath}/{elem}")
            #image = pygame.transform.scale(image, (self.__tileSize, self.__tileSize))
            self.__groundFiles.append(image)
            
    
    def getGroundFiles(self):
        return self.__groundFiles

    def get(self, tileNumber):
        return self.__groundFiles[tileNumber]

"""a = Sprite(32)


pygame.init()

ecran = pygame.display.set_mode((500,500))

while True:
    ecran.blit(a.getGrassSprite(),(32, 32))
    pygame.draw.rect(ecran, "blue", (0,0,32,32))
    pygame.display.flip()
"""
