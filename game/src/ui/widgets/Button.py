import pygame
from game.src.ui.widgets.Text import Text
from game.src.ui.utils.Position import Position
from game.src.core.utils.Dimensions import Dimensions
from game.src.core.utils.Coordinates import Coordinates

class Button():
    LEFT_CLICK = 1

    def __init__(self, message, function, position, margin=None, relative=None, callOnRelease=True):
        self.__text = Text(message)

        self.__position = position
        self.__relative = relative
        self.__margin = margin
        self.__rect = Position.getRect(position, self.__text.getSize(), margin, relative)

        self.__function = function
        self.__clicked = False
        self.__hovered = False
        self.__callOnRelease = callOnRelease

    def get(self):
        return self.__text.get()

    def getPosition(self):
        return Coordinates(*self.__rect.topleft)

    def getSize(self):
        return Dimensions(*self.__rect.size)

    def getRect(self):
        return self.__rect
    
    def checkHover(self):
        if self.__rect.collidepoint(pygame.mouse.get_pos()):
            if not self.__hovered:
                self.__hovered = True
                return True
            return False
        else: 
            if self.__hovered:
                self.__hovered = False
                return True
            return False

    def checkEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == self.LEFT_CLICK:
            self.onClick(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == self.LEFT_CLICK:
            self.onRelease(event)

    def onClick(self, event):
        if self.__rect.collidepoint(event.pos):
            self.__clicked = True
            if not self.__callOnRelease:
                self.__function()

    def onRelease(self, event):
        if self.__clicked and self.__rect.collidepoint(event.pos) and self.__callOnRelease:
            self.__function()
        self.__clicked = False

    def update(self):
        if self.__hovered:
            self.__text.highlight()
        else:
            self.__text.default()

        self.__rect = Position.getRect(self.__position, self.__text.getSize(), self.__margin, self.__relative)
        textPosition = self.getPosition() + self.getSize() // 2 -  self.__text.getSize() // 2
        self.__text.update(textPosition)