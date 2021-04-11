import pygame
from game.src.core.GameLoop import GameLoop

from game.src.ui.gui.Button import Button
from game.src.core.pair.Coordinates import Coordinates
from game.src.core.pair.Dimensions import Dimensions
from game.src.ui.gui.Position import Position
from game.src.ui.gui.Margin import Margin
from game.src.media.music.Music import Music
class Menu:
    def __init__(self, window, seed=None):
        self.__seed = seed
        self.__window = window

        self.__running = True
        self.__startButton = Button("New Game", self.__newGame, Position.CENTER, None, Margin(50, 0, 0, 0))
        self.__settingsButton = Button("Settings", self.__settings, Position.BOTTOM, self.__startButton, Margin(50, 0, 0, 0))
        self.__quitButton = Button("Quit", self.__closeWindow, Position.BOTTOM, self.__settingsButton, Margin(50, 0, 0, 0))

        self.__background = pygame.image.load("game/resources/backgrounds/menuBackground.png").convert_alpha()
        self.__background = pygame.transform.scale(self.__background, self.__window.getSize().toTuple())  

        Music.play("Celestial", -1)

        self.run()

    def __isWindowClosed(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    def __windowResized(self, event):
        if event.type == pygame.VIDEORESIZE:
            self.__window.resizeScreen(event.w, event.h)
            self.__background = pygame.transform.scale(self.__background, self.__window.getSize().toTuple())
            #//FIXME demander de replacer les buttons apres le resize
            return True
        return False

    def __newGame(self):
        Music.stop(fadeOut=True)
        gameLoop = GameLoop(self.__window, self.__seed)
        self.__running = gameLoop.run()

    def __settings(self):
        print("settings")

    def __closeWindow(self):
        self.__running = False

    def __repaint(self):
        self.__window.getScreen().blit(self.__background, (0,0))
        self.__startButton.update(self.__window)
        self.__settingsButton.update(self.__window)
        self.__quitButton.update(self.__window)

        pygame.display.update()

    def run(self):
        self.__repaint()

        while self.__running:
            for event in pygame.event.get():
                self.__running = self.__isWindowClosed(event)
                if self.__windowResized(event):
                    self.__repaint()

                self.__startButton.checkEvent(event)
                self.__settingsButton.checkEvent(event)
                self.__quitButton.checkEvent(event)

            if(self.__startButton.checkHover() or self.__settingsButton.checkHover() or self.__quitButton.checkHover()):
                self.__repaint()
                
            self.__window.clock() 

        pygame.quit()