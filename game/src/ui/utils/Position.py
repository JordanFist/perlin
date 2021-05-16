import pygame

from src.ui.Window import Window
from src.ui.utils.Margin import Margin

class Position:
    TOP = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 3
    TOP_LEFT = 4
    TOP_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM_RIGHT = 7
    CENTER = 8

    @classmethod
    def getRect(cls, position, size, margin=None, relativeRect=None):
        rect = None
        if not margin:
            margin = Margin(0, 0, 0, 0)
        if relativeRect:
            if (position == cls.TOP):
                rect = pygame.Rect( relativeRect.x + relativeRect.width // 2 - size.width // 2 - margin.right + margin.left,
                                    relativeRect.y - size.height // 2 + margin.top - margin.bottom, 
                                    size.width, size.height) 
            if (position == cls.BOTTOM):
                rect = pygame.Rect( relativeRect.x + relativeRect.width // 2 - size.width // 2 - margin.right + margin.left,
                                    relativeRect.y + relativeRect.height - size.height // 2 + margin.top - margin.bottom, 
                                    size.width, size.height) 
        else:
            if (position == cls.CENTER):
                rect = pygame.Rect( Window.getSize().width // 2 - size.width // 2 - margin.right + margin.left,
                                    Window.getSize().height // 2 - size.height // 2 + margin.top - margin.bottom, 
                                    size.width, size.height) 
            if (position == cls.BOTTOM):
                rect = pygame.Rect( Window.getSize().width // 2 - size.width // 2 - margin.right + margin.left,
                                    Window.getSize().height - size.height + margin.top - margin.bottom, 
                                    size.width, size.height) 
        return rect