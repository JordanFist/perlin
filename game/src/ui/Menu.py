import pygame
from game.src.core.GameLoop import GameLoop

from game.src.ui.gui.Button import Button
from game.src.core.pair.Coordinates import Coordinates
from game.src.core.pair.Dimensions import Dimensions

class Menu:
    def __init__(self, window):
        self.__window = window
        #Définir les bouttons
        buttonSize = Dimensions(100, 50)

        buttonStartPosition = Coordinates(self.__window.getSize().width // 2 - buttonSize.width // 2,  self.__window.getSize().height // 2 - buttonSize.height // 2 )
        self.__startButton = Button(buttonStartPosition, buttonSize, "Start") 

        buttonQuitPosition = buttonStartPosition + Coordinates(0, 50)
        self.__quitButton = Button(buttonQuitPosition, buttonSize, "Quit")

        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                
            if self.__startButton.isPressed(event):
                print("Start button is pressed")
                GameLoop(self.__window)
            elif self.__quitButton.isPressed(event):
                running = False
            
            if self.__startButton.mouseHover():
                self.__startButton.repaint(self.__window)
            elif self.__quitButton.mouseHover():
                self.__quitButton.repaint(self.__window)
            
    
            self.__window.getScreen().fill("black")

            self.__startButton.repaint(self.__window)
            self.__quitButton.repaint(self.__window)

            pygame.display.update()
            


            
