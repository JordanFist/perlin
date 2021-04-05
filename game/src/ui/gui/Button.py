import pygame
from game.src.ui.gui.Text import Text


class Button:
    def __init__(self, coord, size, text):
        self.__rect = pygame.Rect(coord.x, coord.y, size.width, size.height)

        self.__text = Text(text, coord, size)
    
    def repaint(self, window):
        if self.mouseHover():
            self.__text.highlight()
        else:
            self.__text.default()
        window.getScreen().blit(self.__text.get(), self.__text.getPosition().toTuple())
        

    def isPressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.mouseHover():
            return True
        return False
    
    def mouseHover(self):
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False
    
        