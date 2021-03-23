import sys, os
from Player import Player
from Map import Map
path = os.path.dirname(os.path.abspath(__file__))+"/../ui" //REVIEW - Revoir ça, cherche plus propre
sys.path.append(path)
from Window import Window
#from View import View
#from Display import Display

class GameLoop:
    def __init__(self):
        self.__player = Player()
        self.__map = Map()
        self.__window = Window()
        #self.__view = View()
        #self.__display = Display()
        self.run()
    
    def run(self):
        #init variables
        running = True
        movementsKeys = {
            pygame.K_RIGHT:False,
            pygame.K_LEFT:False,
            pygame.K_UP:False,
            pygame.K_DOWN:False
        }

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    movementsKeys[event.key] = True
                if event.type == pygame.KEYUP:
                    movementsKeys[event.key] = False
                

            if movementsKeys[pygame.K_RIGHT]:
                self.__player.moveRight()
            if movementsKeys[pygame.K_LEFT]:
                self.__player.moveLeft()
            if movementsKeys[pygame.K_UP]:
                self.__player.move
            if movementsKeys[pygame.K_DOWN]:
                
            

            xOff = playerX % tileSize
            yOff = playerY % tileSize

            #displayMap(map, xOff, yOff)
            view = getViewMatrix(map, playerX, playerY, tileSize, viewSize)
            displayMap(view, xOff, yOff)
            displayPlayer(windowSize)

            pygame.display.flip()



a = GameLoop()