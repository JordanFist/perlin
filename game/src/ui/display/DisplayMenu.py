from src.ui.display.DisplayGame import DisplayGame
import pygame

from src.ui.display.Display import Display

class DisplayMenu(Display):
    def __init__(self, window, background, displayGame=None):
        super().__init__(window, background)
        self.__displayGame = displayGame

    def updateBackground(self):
        self._background.rescale(self._window)
        self._window.getScreen().blit(self._background.get(), (0,0))

    def flip(self):
        if self.__displayGame != None:
            self.__displayGame.flip(True)
        self.updateBackground()
        for widget in self._objectsOnScreen:
            widget.update()
            self._window.getScreen().blit(widget.get(), widget.getRect()) #text as the same rect as its button so we can get the rect of the button
        pygame.display.update()