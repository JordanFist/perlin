import pygame
from game.src.ui.gui.Text import Text
from game.src.ui.gui.Position import Position
from game.src.ui.Window import Window
from game.src.core.pair.Dimensions import Dimensions
from game.src.core.pair.Coordinates import Coordinates
from game.src.ui.gui.Margin import Margin

class Button():
    LEFT_CLICK = 1

    def __init__(self, message, function, position, relative=None, margin=None, callOnRelease=True):
        self.__rect = None
        self.__text = Text(message)

        self.__position = position
        self.__relative = relative
        if (relative):
            self.__relativePosition = relative.getPosition()
            self.__relativeSize = relative.getSize()
        self.__margin = margin
        self.setPosition()

        self.__function = function
        self.__clicked = False
        self.__hovered = False
        self.__callOnRelease = callOnRelease

    def getPosition(self):
        return Coordinates(*self.__rect.topleft)

    def getSize(self):
        return Dimensions(*self.__rect.size)
    
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
        if self.__clicked and self.__callOnRelease: #//FIXME add check collision
            self.__function()
        self.__clicked = False

    def update(self, window):
        if self.__hovered:
            self.__text.highlight()
            self.setPosition()
        else:
            self.__text.default()
            self.setPosition()
        textPosition = self.getPosition() + self.getSize() // 2 -  self.__text.getSize() // 2
        self.__text.update(window, textPosition)
        pygame.draw.rect(window.getScreen(), "red", self.__rect, 1) 

    def setPosition(self):
        if not self.__margin:
            self.__margin = Margin(0, 0, 0, 0)
        if self.__relative:
            if (self.__position == Position.BOTTOM):
                self.__rect = pygame.Rect(  self.__relativePosition.x + self.__relativeSize.width // 2 - self.__text.getSize().width // 2 - self.__margin.right + self.__margin.left,
                                            self.__relativePosition.y + self.__relativeSize.height + self.__margin.top - self.__margin.bottom, 
                                            self.__text.getSize().width, self.__text.getSize().height) 
        else:
            if (self.__position == Position.CENTER):
                self.__rect = pygame.Rect(  Window.getSize().width // 2 - self.__text.getSize().width // 2 - self.__margin.right + self.__margin.left,
                                            Window.getSize().height // 2 - self.__text.getSize().height // 2 + self.__margin.top - self.__margin.bottom, 
                                            self.__text.getSize().width, self.__text.getSize().height) 